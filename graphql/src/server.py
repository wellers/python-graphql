import strawberry
from schema.scalars import PyObjectIdType, PyObjectId
from schema.resolvers import Query, Mutation

schema = strawberry.Schema(Query, Mutation, scalar_overrides={PyObjectId: PyObjectIdType})