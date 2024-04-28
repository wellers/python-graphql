import strawberry
from schema.definitions import ContactsFindResult, Contact, ContactsFindFilter, ContactsInsertInput, ContactsInsertResult
from schema.db import connect

@strawberry.type
class ContactsQuery:
	@strawberry.field(name = "contacts_find")
	async def contacts_find(self, filter: ContactsFindFilter) -> ContactsFindResult:
		search = {}
		if len(filter.search_term) > 0:
			search = { 
				"$or": [{ 
					"forename": { "$regex": filter.search_term, "$options": "i" } 
				}, { 
					"surname": { "$regex": filter.search_term, "$options": "i" } 
				}] 
			}

		db = connect()

		docs = db.contacts.find(search)		
		docs = await docs.to_list(length=None)

		docs = [Contact.to_schema(result) for result in docs]

		return ContactsFindResult(
			success=True, 
			message="Records matching filter.", 
			docs=docs
		)

@strawberry.type
class ContactsMutation:
	@strawberry.field(name = "contacts_insert")
	async def contacts_insert(self, input: ContactsInsertInput) -> ContactsInsertResult:
		contacts = [contact.__dict__ for contact in input.contacts]
		
		db = connect()

		inserted = await db.contacts.insert_many(contacts)

		return ContactsInsertResult(
			success=True, 
			message=f"Contact(s) - {len(inserted.inserted_ids)} has been added."
		)

@strawberry.type
class Query:
	@strawberry.field
	def contacts(self) -> ContactsQuery:
		return ContactsQuery()

@strawberry.type
class Mutation:
	@strawberry.field
	def contacts(self) -> ContactsMutation:
		return ContactsMutation()