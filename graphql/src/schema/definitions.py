from dataclasses import dataclass
import strawberry
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
@dataclass
class ContactsFindResult:
	success: bool
	message: str
	docs: list[Contact]

@strawberry.type
@dataclass
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