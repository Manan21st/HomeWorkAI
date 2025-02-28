from fastapi import APIRouter, HTTPException, Depends
from app.schemas.response import ChatResponse
from app.schemas.request import ChatRequest, ChatRequestMsg
from app.services.chat import ChatService, chat_service

router = APIRouter()

def get_chat_service():
    return chat_service

@router.post("/init", response_model=ChatResponse)
def initiate_chat(request: ChatRequest, chat_service: ChatService = Depends(get_chat_service)):
    try:
        response = chat_service.init_chat(request.url, request.message)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/continue", response_model=ChatResponse)
def continue_chat(request: ChatRequestMsg, chat_service: ChatService = Depends(get_chat_service)):
    try:
        response = chat_service.continue_chat(request.message)
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.post("/reset", response_model=ChatResponse)
def reset_chat(chat_service: ChatService = Depends(get_chat_service)):
    try:
        response = chat_service.reset_chat()
        return response
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))