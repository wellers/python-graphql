import strawberry
from schema.definitions import ContactsInsertInput, ContactsInsertResult
from .db import connect

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