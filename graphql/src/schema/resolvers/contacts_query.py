import strawberry
from schema.definitions import ContactsFindResult, Contact, ContactsFindFilter
from .db import connect

@strawberry.type
class ContactsQuery:
	@strawberry.field(name = "contacts_find")
	async def contacts_find(self, filter: ContactsFindFilter) -> ContactsFindResult:	
		search = {}
		if filter.search_term:
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