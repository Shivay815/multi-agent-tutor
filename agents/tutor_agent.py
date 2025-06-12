import os
import google.generativeai as genai
from dotenv import load_dotenv

# Import sub-agents
from agents.math_agent import MathAgent
from agents.physics_agent import PhysicsAgent

load_dotenv() # Load environment variables from .env

class TutorAgent:
    def __init__(self):
        self.api_key = os.getenv("GEMINI_API_KEY")
        if not self.api_key:
            raise ValueError("GEMINI_API_KEY not found in environment variables.")

        genai.configure(api_key=self.api_key)
        self.model = genai.GenerativeModel('models/gemini-1.5-flash-latest')

        # Initialize sub-agents
        self.math_agent = MathAgent(self.api_key)
        self.physics_agent = PhysicsAgent(self.api_key)

    def determine_agent(self, query: str) -> str:
        """Determines which sub-agent should handle the query."""
        prompt = f"""
        Analyze the following student query and determine if it's primarily about 'math' or 'physics'.
        Respond with only the word 'math', 'physics', or 'general' if neither applies.

        Student query: "{query}"
        """
        response = self.model.generate_content(prompt)
        # Make sure to strip whitespace and convert to lowercase for robust comparison
        return response.text.strip().lower()

    def handle_query(self, query: str) -> str:
        """Delegates the query to the appropriate sub-agent."""
        agent_type = self.determine_agent(query)

        if "math" in agent_type:
            print(f"Delegating '{query}' to Math Agent...")
            return self.math_agent.process_query(query)
        elif "physics" in agent_type:
            print(f"Delegating '{query}' to Physics Agent...")
            return self.physics_agent.process_query(query)
        else:
            print(f"Handling '{query}' with general response...")
            # Fallback to general Gemini model if no specific agent
            fallback_prompt = f"You are a general tutoring assistant. Answer the following query: {query}"
            response = self.model.generate_content(fallback_prompt)
            return response.text