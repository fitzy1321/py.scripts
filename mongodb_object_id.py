from typing import Any

from bson import ObjectId
from pydantic import BaseModel


class MongoObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def __modify_schema__(cls, field_schema: dict) -> None:
        field_schema.update(
            examples=["5f85f36d6dfecacc68428a46", "ffffffffffffffffffffffff"],
            example="5f85f36d6dfecacc68428a46",
            type="string",
        )

    @classmethod
    def validate(cls, v: Any) -> ObjectId:
        if not isinstance(v, (ObjectId, cls)) or not ObjectId.is_valid(v):
            raise TypeError("invalid ObjectId specified")
        return v


class MongoBaseModel(BaseModel):
    class Config:
        json_encoders = {ObjectId: str}
