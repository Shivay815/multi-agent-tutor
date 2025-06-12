# Multi-Agent Tutor

A conversational AI tutor powered by Google's Gemini models, designed to provide interactive assistance across various subjects. This project demonstrates a multi-agent architecture where a central `TutorAgent` delegates complex queries to specialized `MathAgent` and `PhysicsAgent` instances, leveraging Google's Generative AI capabilities and tool-use (e.g., a calculator).

## Table of Contents

  * [Features](https://www.google.com/search?q=%23features)
  * [How It Works](https://www.google.com/search?q=%23how-it-works)
  * [Setup and Installation](https://www.google.com/search?q=%23setup-and-installation)
      * [Prerequisites](https://www.google.com/search?q=%23prerequisites)
      * [1. Clone the Repository](https://www.google.com/search?q=%231-clone-the-repository)
      * [2. Create and Activate a Virtual Environment](https://www.google.com/search?q=%232-create-and-activate-a-virtual-environment)
      * [3. Install Dependencies](https://www.google.com/search?q=%233-install-dependencies)
      * [4. Set Up Your Google Gemini API Key](https://www.google.com/search?q=%234-set-up-your-google-gemini-api-key)
  * [Running the Application Locally](https://www.google.com/search?q=%23running-the-application-locally)
  * [API Endpoints](https://www.google.com/search?q=%23api-endpoints)
  * [Project Structure](https://www.google.com/search?q=%23project-structure)
  * [License](https://www.google.com/search?q=%23license)

## Features

  * **Intelligent Routing:** A main `TutorAgent` intelligently determines the user's intent and delegates the query to the appropriate specialized agent.
  * **Specialized Agents:**
      * **Math Agent:** Handles mathematical calculations and problems by utilizing a tool (e.g., a calculator).
      * **Physics Agent:** Provides explanations and answers related to physics concepts.
  * **Google Gemini Integration:** Leverages the power of Google's Gemini models for natural language understanding and generation.
  * **FastAPI Backend:** Provides a robust and fast API for interacting with the tutor.
  * **Local and Cloud Deployment:** Easily runnable locally and deployable to platforms like Vercel.

## How It Works

The core of the Multi-Agent Tutor is its delegation mechanism:

1.  A user submits a query to the FastAPI backend's `/ask` endpoint.
2.  The `TutorAgent` receives the query.
3.  The `TutorAgent` uses a Gemini model to classify the query's type (e.g., "math," "physics," or "general").
4.  Based on the classification:
      * If "math," the query is passed to the `MathAgent`.
      * If "physics," the query is passed to the `PhysicsAgent`.
      * If "general," the `TutorAgent` handles the response directly.
5.  Specialized agents (like `MathAgent`) can invoke custom tools (e.g., a Python-based `calculator`) to solve problems before formulating their answer.
6.  The final response is sent back to the user.

-----

## Setup and Installation

Follow these steps to get the Multi-Agent Tutor running on your local machine.

### Prerequisites

  * Python 3.9+
  * A Google Gemini API Key. You can obtain one from [Google AI Studio](https://ai.google.dev/aistudio).

### 1\. Clone the Repository

First, clone the project repository to your local machine:

```bash
git clone https://github.com/Shivay815/multi-agent-tutor.git
cd multi-agent-tutor
```

### 2\. Create and Activate a Virtual Environment

It's highly recommended to use a virtual environment to manage dependencies.

```bash
python -m venv venv
# On macOS/Linux:
source venv/bin/activate
# On Windows:
.\venv\Scripts\activate
```

### 3\. Install Dependencies

With your virtual environment activated, install the required Python packages:

```bash
pip install -r requirements.txt
```

### 4\. Set Up Your Google Gemini API Key

Create a file named `.env` in the root directory of your project (where `main.py` is located) and add your Gemini API key:

```
GEMINI_API_KEY="YOUR_GEMINI_API_KEY_HERE"
```

**Replace `"YOUR_GEMINI_API_KEY_HERE"` with your actual API key.**

## Running the Application Locally

Once you've completed the setup steps, you can run the FastAPI application:

```bash
uvicorn main:app --reload
```

You should see output similar to this:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
```

Open your web browser and go to `http://127.0.0.1:8000` to access the basic interface, or `http://127.0.0.1:8000/docs` for the FastAPI interactive API documentation (Swagger UI), where you can test the `/ask` endpoint.

## API Endpoints

The FastAPI application exposes the following primary endpoint:

  * **`POST /ask`**
      * **Description:** Submits a question to the multi-agent tutor.
      * **Request Body (JSON):**
        ```json
        {
          "query": "What is the capital of France?"
        }
        ```
      * **Response (JSON):**
        ```json
        {
          "response": "Paris is the capital of France."
        }
        ```

## Project Structure

```
multi-agent-tutor/
├── main.py                     # Main FastAPI application
├── agents/                     # Directory for agent classes
│   ├── __init__.py
│   ├── tutor_agent.py          # Central agent for query delegation
│   ├── math_agent.py           # Specialized agent for math queries
│   └── physics_agent.py        # Specialized agent for physics queries
├── tools/                      # Directory for external tools (e.g., calculator)
│   ├── __init__.py
│   └── calculator.py           # Calculator function used by MathAgent
├── .env                        # Environment variables (local only)
├── requirements.txt            # Python dependencies
├── vercel.json                 # Vercel deployment configuration
└── README.md                   # This README file
```

## License

This project is open-source and available under the [MIT License](https://www.google.com/search?q=LICENSE).