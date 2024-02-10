from bson.objectid import ObjectId as BsonObjectId
import strawberry

class PyObjectId(BsonObjectId):
	@classmethod
	def __get_validators__(cls):
		yield cls.validate

	@classmethod
	def validate(cls, v):
		if not BsonObjectId.is_valid(v):
			raise ValueError("Invalid ObjectId")
		return BsonObjectId(v)

	@classmethod
	def __modify_schema__(cls, field_schema):
		field_schema.update(type="string")

# serialize PyObjectId as a scalar type
PyObjectIdType = strawberry.scalar(
	PyObjectId, serialize=str, parse_value=lambda v: PyObjectId(v)
)