from ninja import NinjaAPI
from .schemas import UserSchema, UserCreateSchema
from login.models import User
from typing import List

api = NinjaAPI()


@api.get("/users", response=List[UserSchema])
def get_users(request):
    all_users = User.objects.all()
    return all_users


@api.post("/users", response=UserSchema)
def create_user(request, user_in: UserCreateSchema):
    print(user_in.dict())
    user = User.objects.create(username=user_in.username, role=user_in.role)
    user.set_password(user_in.password)
    user.save()
    return user


# @api.post("/users", response=UserSchema)
# def create_user(request, user_in: UserCreateSchema):
#     print(user_in.dict())
#     user = User.objects.create(**user_in.dict())
#     print(user_in.password)
#     user.set_password
#     return user
