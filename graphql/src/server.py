import strawberry
from schema.scalars import PyObjectIdType
from schema.types import *

schema = strawberry.Schema(Query, Mutation, scalar_overrides={PyObjectId: PyObjectIdType})