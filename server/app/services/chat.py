from app.schemas.response import ChatResponse
from app.core.chatbot import ChatBot
from app.core.scraper import LeetCodeScraper
from app.core.prompts_manager import PromptManager


class ChatService:
    def __init__(self):
        self.messages = []
        self.scraper = LeetCodeScraper()
        self.chatbot = ChatBot()
        self.prompt_manager = PromptManager()
        self.problem = ""

    def init_chat(self, url: str, message: str) -> ChatResponse:
        
        self.problem = self.scraper.get_question(url)
        if not self.problem:
            return {"role": "bot", "message": "I'm sorry, I couldn't find that problem. Please try again."}
        
        intial_prompt = self.prompt_manager.get_initial_prompt(problem_description=self.problem, user_message=message)
        response = self.chatbot.get_response(intial_prompt)
        self.messages.append({"role": "bot", "message": response})

        return {"role": "bot", "message": response}
    
    def continue_chat(self, message: str) -> ChatResponse:
        self.messages.append({"role": "user", "message": message})
        chat_history = self.messages
        stage_prompt = self.prompt_manager.get_stage_detection_prompt(self.messages, message)
        stage = self.chatbot.get_response(stage_prompt)
        prompt = self.prompt_manager.get_prompt_for_stage(stage, self.messages, message)
        response = self.chatbot.get_response(prompt)
        self.messages.append({"role": "bot", "message": response})

        return {"role": "bot", "message": response}
    
    def reset_chat(self) -> ChatResponse:
        self.messages = []
        self.problem = ""
        return {"role": "bot", "message": "Chat reset successfully."}
    
chat_service = ChatService()