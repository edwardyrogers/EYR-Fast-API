from pydantic import BaseModel


class AttemptREQ(BaseModel):
    name: str

    
class AttemptRES(BaseModel):
    name: str
    
    class TestOneRES(BaseModel):
        name: str

    class TestTwoRES(BaseModel):
        pass
