import strawberry
from schema.scalars import PyObjectId

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