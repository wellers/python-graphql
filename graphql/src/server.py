import strawberry
from schema.scalars import PyObjectIdType
from schema.definitions import *

schema = strawberry.Schema(Query, Mutation, scalar_overrides={PyObjectId: PyObjectIdType})