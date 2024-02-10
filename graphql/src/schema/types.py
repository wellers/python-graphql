from dataclasses import dataclass
import strawberry
from .db import db
from .scalars import PyObjectId

@strawberry.type
class Contact:
	id: PyObjectId
	title: str
	forename: str
	surname: str

	@staticmethod
	def to_schema(contact):
		return Contact(
			id=PyObjectId(contact["_id"]), 
			title=contact["title"], 
			forename=contact["forename"], 
			surname=contact["surname"])


@strawberry.type
class ContactsFindResult:
	success: bool
	message: str
	docs: list[Contact]

@strawberry.type
class ContactsInsertResult:
	success: bool
	message: str

@strawberry.input
@dataclass
class ContactsFindFilter:
	search_term: str

@strawberry.input
class ContactInput:
	title: str
	forename: str
	surname: str

@strawberry.input
@dataclass
class ContactsInsertInput:
	contacts: list[ContactInput]

@strawberry.type
class ContactsQuery:
	@strawberry.field(name = "contacts_find")
	def contacts_find(filter: ContactsFindFilter) -> ContactsFindResult:
		if len(filter.search_term) > 0:
			filter = { "$or": [{ "forename": { "$regex": filter.search_term, "$options": "i" } }, { "surname": { "$regex": filter.search_term, "$options": "i" } }] }
		else:
			filter = {}

		results = list(db.contacts.find(filter))

		docs = [Contact.to_schema(result) for result in results]

		return ContactsFindResult(
			success=True, 
			message="Records matching filter.", 
			docs=docs
		)

@strawberry.type
class ContactsMutation:
	@strawberry.field(name = "contacts_insert")
	def contacts_insert(input: ContactsInsertInput) -> ContactsInsertResult:
		contacts = [contact.__dict__ for contact in input.contacts]
		
		inserted = db.contacts.insert_many(contacts)

		return ContactsInsertResult(
			success=True, 
			message=f"Contact(s) - {len(inserted.inserted_ids)} has been added."
		)

@strawberry.type
class Query:
	@strawberry.field
	def contacts(self) -> ContactsQuery:
		return ContactsQuery

@strawberry.type
class Mutation:
	@strawberry.field
	def contacts(self) -> ContactsMutation:
		return ContactsMutation