import strawberry
from .contacts_mutation import ContactsMutation

@strawberry.type
class Mutation:
	@strawberry.field
	def contacts(self) -> ContactsMutation:
		return ContactsMutation()