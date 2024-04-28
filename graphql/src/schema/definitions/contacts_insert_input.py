from dataclasses import dataclass
import strawberry
from .contact_input import ContactInput

@strawberry.input
@dataclass
class ContactsInsertInput:
	contacts: list[ContactInput]