import google.generativeai as genai

class PhysicsAgent:
    def __init__(self, api_key: str):
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest')
    def process_query(self, query: str) -> str:
        """Processes a physics-related query."""
        prompt = f"""
        You are a specialized Physics Agent. Your purpose is to help students with physics questions.
        Answer clearly and concisely.

        Student query: {query}
        """
        response = self.model.generate_content(prompt)
        return response.text