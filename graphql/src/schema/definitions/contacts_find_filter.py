from dataclasses import dataclass
import strawberry

@strawberry.input
@dataclass
class ContactsFindFilter:
	search_term: str