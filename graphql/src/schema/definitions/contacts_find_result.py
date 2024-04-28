from dataclasses import dataclass
import strawberry
from .contact import Contact

@strawberry.type
@dataclass
class ContactsFindResult:
	success: bool
	message: str
	docs: list[Contact]