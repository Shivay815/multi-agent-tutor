from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from agents.tutor_agent import TutorAgent

app = FastAPI()

# Mount static files (like CSS if you add it later)
# app.mount("/static", StaticFiles(directory="static"), name="static")

# Configure Jinja2Templates for HTML templating
templates = Jinja2Templates(directory="templates")

# Initialize your TutorAgent
tutor_bot = TutorAgent()

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    """Serves the main HTML page for interaction."""
    return templates.TemplateResponse("index.html", {"request": request, "response": None})

@app.post("/ask", response_class=HTMLResponse)
async def ask_question(request: Request, user_query: str = Form(...)):
    """Handles the user's question and returns the bot's answer."""
    bot_response = tutor_bot.handle_query(user_query)
    return templates.TemplateResponse("index.html", {"request": request, "response": bot_response, "query": user_query})

# Optional: A simple API endpoint for testing without the UI
@app.get("/api/ask")
async def ask_api(query: str):
    """API endpoint to ask the tutor bot a question."""
    response = tutor_bot.handle_query(query)
    return {"query": query, "response": response}

if __name__ == "__main__":
    import uvicorn
    # To run locally: uvicorn main:app --reload
    # We use app.run() for a more robust local development setup with some servers,
    # but for FastAPI, uvicorn.run is standard.
    uvicorn.run(app, host="0.0.0.0", port=8000)