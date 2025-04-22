from pydantic import BaseModel, EmailStr

class AttemptREQ(BaseModel):
    name: str

class AttemptRES(BaseModel):
    name: str
