from crewai import Agent, Task, Crew, Process
from langchain_ollama import OllamaLLM
import os

os.environ["LITELLM_PROVIDER"] = "ollama"

# os.environ['DEEPSEEK_API_KEY']

llAma = "ollama_chat/deepseek-r1"

topic = "NCS Membership Support"

# DEFINE AGENTS
research_agent = Agent(
    role="Support Agent",
    goal=f"answer any questions that concerns {topic} ",
    backstory=f"you are a researcher who has been studying {topic} for years, and you've implemented your theoretical knowledge on a broad range of real-world projects",
    verbose=True,
    allow_delegation=False,
    llm=llAma
)

prompt_agent = Agent(
    role="promptengineer",
    goal=f"write a single structured prompt in markdown explaining how a world-class {topic} would approach a project",
    backstory=f"you're an AI assistant that writes a single prompt explaining how a world-class {topic} would approach a project",
    verbose=True,
    allow_delegation=False,
    llm=llAma
)

# DEFINE TASKS
gather_info = Task(
    description=f"from your knowledge base, collect relevant information about {topic} experts",
    agent=research_agent,  # Corrected: Assigning a single agent
    expected_output=f"A clear list of key points related to {topic} experts and how they work",
)

write_prompt = Task(
    description=f"write a single structured prompt in markdown explaining how a world-class {topic} would approach a project",
    agent=prompt_agent,  # Corrected: Assigning a single agent
    expected_output=f"A single structured prompt in markdown explaining how a world-class {topic} would approach a project",
)

# DEFINE CREW
crew = Crew(
    agents=[research_agent, prompt_agent],  # Corrected: Using the properly defined agents
    tasks=[gather_info, write_prompt],  # Corrected: Using the properly defined tasks
    process=Process.sequential  # Corrected: Using proper process mode
)

# EXECUTE
output = crew.kickoff()
print(output)
