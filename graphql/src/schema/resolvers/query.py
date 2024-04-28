import strawberry
from .contacts_query import ContactsQuery

@strawberry.type
class Query:
	@strawberry.field
	def contacts(self) -> ContactsQuery:
		return ContactsQuery()