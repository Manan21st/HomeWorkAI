from pydantic import BaseModel

class ChatRequest(BaseModel):
    url : str
    message : str

class ChatRequestMsg(BaseModel):
    message : str