from pydantic import BaseModel
from typing import List,Union,Optional


class User(BaseModel):
   name:str
   email:str
   password:str

class Blog(BaseModel):
   
   title:str
   body:str


class ShowUser(BaseModel):
   name:str
   email:str
   blogs:List[Blog]=[]
   class Config():
      orm_mode=True



class ShowBlog(BaseModel):
   title:str
   body:str
   creator:ShowUser
   class Config():
      orm_mode=True

class Login(BaseModel):
   username:str
   password:str
   



class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    emai: Optional[str] = None