from pydantic import BaseModel

class ChatResponse(BaseModel):
    role : str
    message : str