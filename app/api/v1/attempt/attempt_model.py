from pydantic import BaseModel


class AttemptREQ(BaseModel):
    name: str


class AttemptRES(BaseModel):
    name: str
