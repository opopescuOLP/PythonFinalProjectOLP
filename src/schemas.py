from pydantic imoprt BaseModel, Emailstr


class UserBase(BaseModel):
    email: Emailstr
    username: str

class userCreate(UserBase):
    password: str

class User(UserBase):
    id: int

