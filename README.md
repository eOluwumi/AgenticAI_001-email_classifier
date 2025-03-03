**AgenticAI 001 - Email Classification & Response**

_**Overview**_

_AgenticAI 001 is a multi-agent system designed to classify emails and generate appropriate responses. It leverages the CrewAI framework to coordinate agents that perform distinct tasks—classification and response generation. This is just the beginning of the AgenticAI revolution._

_**Features**___

- _Automated Email Classification: Categorizes emails as important, casual, or spam._

- _Contextual Email Responses: Generates concise and appropriate responses based on classification._

- _Modular Agent-Based Architecture: Utilizes CrewAI agents for task delegation and execution._

- _Sequential Processing: Ensures classification occurs before response generation._

_**Technologies Used**_

_- Python_
_- CrewAI_
_- Groq LLaMA3 8B_
_- OpenAI API (via Groq)_
- _Environment Variables for Configurations_

**_Installation_**

- _Clone the repository:_
-- git clone https://github.com/your-repo/agenticai_001.git
-- cd agenticai_001

- _Create a virtual environment and activate it:_
-- python -m venv .venv
-- On Windows use .venv\Scripts\activate

- _Install dependencies:_
-- pip install -r requirements.txt

- _Set environment variables:_
-- Create a .env file and add:
-- LITELLM_PROVIDER=groq
-- OPEN_API_BASE=https://api.groq.com/openai/v1
-- OPENAI_MODEL_NAME=groq/llama3-8b-8192
-- GROQ_API_KEY=your_api_key_here

- _Run the script:_
--python omain.py

- _Usage_
-- The script processes an email and classifies it.
-- Based on classification, it generates an appropriate response.

**_Example output:_**

# Agent: Email Classifier
## Final Answer: spam

# Agent: Email Responder
## Final Answer:
Dear Nigerian Prince,
Thank you for your email. Unfortunately, I'm not interested in your offer of gold. Please don't contact me again.

-**Next Steps**
- Enhance classification accuracy with fine-tuned models.
- Integrate document-based Q&A for customer support.
- Deploy as an API using FastAPI.
- Implement logging & monitoring for better insights.

**Contributing**
--Contributions are welcome! Feel free to fork this repo and create pull requests.

**License**
-- NIL

🚀 This is just the beginning of the AgenticAI revolution! Stay tuned for more advancements. 🚀
