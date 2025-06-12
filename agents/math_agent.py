import google.generativeai as genai
from tools.calculator import calculator # Import your tool

class MathAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest', tools=[calculator])
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    def process_query(self, query: str) -> str:
        """Processes a math-related query and uses the calculator tool if needed."""
        prompt = f"""
        You are a specialized Math Agent. Your purpose is to help students with mathematics questions.
        You have access to a `calculator` tool.
        If the question involves numerical calculations, use the `calculator` tool.
        For theoretical questions, answer directly.
        Be precise and clear.

        Student query: {query}
        """
        response = self.chat.send_message(prompt)
        return response.text