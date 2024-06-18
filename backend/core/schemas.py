from ninja import Schema
from typing import Literal


class UserSchema(Schema):
    username: str
    is_staff: bool
    is_clocked_in: bool
    role: Literal["E", "M"]


class UserCreateSchema(Schema):
    username: str
    role: Literal["E", "M"]
    password: str
