# HomeWork AI

HomeWork AI is an intelligent teaching assistant designed to guide users through problem-solving steps without directly providing answers. It helps break down problems, suggests improvements, and encourages users to think critically.

## Project Overview
- **Backend:** Runs on `localhost:8080`
- **Frontend:** Runs on `localhost:8501`
- **Prompts Manager:** 9 structured prompts for guiding users
- **Docker-based deployment**
- **No authentication or database**

## Features
- Provides structured guidance based on problem-solving stages
- Classifies user progress through chat history
- Suggests hints instead of direct answers
- Works locally using Docker

## Installation and Setup

### Prerequisites
Ensure you have the following installed:
- Docker
- Docker Compose

### Running the Project

- Clone the repository:
   ```sh
   git clone https://github.com/Manan21st/HomeWorkAI.git
   cd HomeWorkAI
   ```

- Start the project using Docker:
   ```sh
   docker-compose up --build
   ```

- Access the frontend at:
   ```
   http://localhost:8501
   ```

- Backend will be running at:
   ```
   http://localhost:8080
   ```

## Frontend Functionality
The frontend consists of:
- A **URL section** where users must keep the problem's URL while asking questions.
- A **reset button** to switch to a new problem.
- A **chat area** with a text input and send button to interact with the AI.
- **Chat history is maintained for a single problem until reset**.

## API Endpoints
The backend exposes three main endpoints:
- **`/init`** - Initializes a new conversation for a given problem.
- **`/continue`** - Continues the conversation with a new message.
- **`/reset`** - Resets the chat, allowing users to switch to a new problem.

## Prompts Manager
The `PromptManager` class manages user interactions through structured prompts. It includes prompts for:
- Detecting the problem-solving stage
- Understanding the problem
- Exploring examples
- Breaking down the problem
- Writing pseudocode
- Writing code
- Testing and debugging
- Optimizing the solution
- General follow-up questions

## Project Structure
```
/homework-ai
├── client/              # Frontend application (Streamlit)
│   ├── app.py           # Main frontend script
│   ├── Dockerfile       # Docker configuration for frontend
│   ├── requirements.txt # Dependencies for frontend
├── server/              # Backend application (FastAPI/Flask)
│   ├── app/             # Main application logic
│   │   ├── api/         # API endpoints
│   │   │   ├── endpoints/
│   │   │   │   ├── __init__.py
│   │   │   │   ├── chat.py
│   │   │   ├── __init__.py
│   │   │   ├── api.py
│   │   ├── core/        # Core logic
│   │   │   ├── chatbot.py
│   │   │   ├── config.py
│   │   │   ├── prompts_manager.py
│   │   │   ├── scraper.py
│   │   ├── schemas/     # Request and response schemas
│   │   │   ├── request.py
│   │   │   ├── response.py
│   │   ├── services/    # Business logic services
│   │   │   ├── chat.py
│   │   ├── main.py
│   ├── .env                 # Environment variables
│   ├── Dockerfile           # Backend Dockerfile
│   ├── requirements.txt     # Backend dependencies
├── docker-compose.yml   # Docker configuration
└── README.md            # Project documentation
```

---
Made with ❤️ by Manan Agrawal

