import google.generativeai as genai
from app.core.config import settings

class ChatBot:
    def __init__(self):
        self.key = settings.API_KEY  # Load API key
        genai.configure(api_key=self.key)  # Initialize Gemini API
        self.model = genai.GenerativeModel("gemini-2.0-flash")  # Use the Gemini model

    def get_response(self, message: str) -> str:
        """
        Sends a message to the Gemini API and returns a response.
        """
        try:
            response = self.model.generate_content(message)  # Generate response
            return response.text if response else "I couldn't understand that."
        except Exception as e:
            return f"Error: {str(e)}"