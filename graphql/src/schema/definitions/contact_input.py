import strawberry

@strawberry.input
class ContactInput:
	title: str
	forename: str
	surname: str