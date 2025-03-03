#AgenticAI 001 - Email Classification & Response

##Overview

AgenticAI 001 is a multi-agent system designed to classify emails and generate appropriate responses. It leverages the CrewAI framework to coordinate agents that perform distinct tasks—classification and response generation. This is just the beginning of the AgenticAI revolution.

###Features

Automated Email Classification: Categorizes emails as important, casual, or spam.

Contextual Email Responses: Generates concise and appropriate responses based on classification.

Modular Agent-Based Architecture: Utilizes CrewAI agents for task delegation and execution.

Sequential Processing: Ensures classification occurs before response generation.

###Technologies Used

Python

CrewAI

Groq LLaMA3 8B

OpenAI API (via Groq)

Environment Variables for Configurations

###Installation

Clone the repository:

git clone https://github.com/your-repo/agenticai_001.git
cd agenticai_001

Create a virtual environment and activate it:

python -m venv .venv
source .venv/bin/activate  # On Windows use .venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Set environment variables:

Create a .env file and add:

LITELLM_PROVIDER=groq
OPEN_API_BASE=https://api.groq.com/openai/v1
OPENAI_MODEL_NAME=groq/llama3-8b-8192
GROQ_API_KEY=your_api_key_here

Run the script:

python main.py

Usage

The script processes an email and classifies it.

Based on classification, it generates an appropriate response.

Example output:

# Agent: Email Classifier
## Final Answer: spam

# Agent: Email Responder
## Final Answer:
Dear Nigerian Prince,
Thank you for your email. Unfortunately, I'm not interested in your offer of gold. Please don't contact me again.

Next Steps

Enhance classification accuracy with fine-tuned models.

Integrate document-based Q&A for customer support.

Deploy as an API using FastAPI.

Implement logging & monitoring for better insights.

Contributing

Contributions are welcome! Feel free to fork this repo and create pull requests.

License

MIT License

🚀 This is just the beginning of the AgenticAI revolution! Stay tuned for more advancements. 🚀

