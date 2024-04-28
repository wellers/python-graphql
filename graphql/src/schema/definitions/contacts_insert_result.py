from dataclasses import dataclass
import strawberry

@strawberry.type
@dataclass
class ContactsInsertResult:
	success: bool
	message: str