import os
from crewai import Agent, Task, Crew, Process

# Set environment variables for Groq
os.environ["LITELLM_PROVIDER"] = "groq"
os.environ["OPEN_API_BASE"] = 'https://api.groq.com/openai/v1'
os.environ["OPENAI_MODEL_NAME"] = 'groq/llama3-8b-8192'
os.environ["GROQ_API_KEY"] = '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'

# Email to be processed
email = "nigerian prince sending some gold"

# Define the Email Classifier Agent without an explicit LLM instance.
classifier = Agent(
    role="Email Classifier",
    goal="Accurately classify emails based on their importance. "
         "Give every email one of these ratings: 'important', 'casual', or 'spam'.",
    backstory="You are an AI assistant trained on a large dataset of emails, "
              "specialized in classifying emails based on their importance.",
    verbose=True,
    allow_delegation=False,
)

# Define the Email Responder Agent without an explicit LLM instance.
responder = Agent(
    role="Email Responder",
    goal="Based on the importance of the email, write a concise and simple response.",
    backstory="You are an AI assistant trained on a large dataset of emails, "
              "specialized in generating appropriate responses based on email importance.",
    verbose=True,
    allow_delegation=False,
)

# Define the Task for Classifying Email
classify_email = Task(
    description=f"Classify the following email: '{email}'",
    agent=classifier,
    expected_output="One of these three options: 'important', 'casual', or 'spam'."
)

# Define the Task for Responding to Email
respond_to_email = Task(
    description=f"Write a response to the email: '{email}' based on the classification provided by the 'Email Classifier' agent.",
    agent=responder,
    expected_output="A concise response to the email based on its importance."
)

# Create and configure the Crew to run the tasks sequentially.
crew = Crew(
    agents=[classifier, responder],
    tasks=[classify_email, respond_to_email],
    verbose=True,
    process=Process.sequential  # Ensures tasks are executed in order.
)

# Execute the workflow
output = crew.kickoff()

# Print the final result
print(output)