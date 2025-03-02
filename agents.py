from crewai import Agent, Task, Crew, Process

# from langchain_community import Ollama
from langchain_ollama import OllamaLLM
import os
os.environ["LITELLM_PROVIDER"] = "openai"



llAma = OllamaLLM(model = "llama3:latest")

topic = "Web Development"

# DEFINE AGENTS     ___________________________________________________________


research_agent = Agent(
    role = "researcher", 
    goal = f"from your memory, gather relevant information about how an expert {topic} developer works",
    backstory = f"you are a researcher who has been studying {topic} for years, and you've implemented your theoretical knowledge on a broad range of real-world projects",
    verbose=True,
    allow_delegation=False,
    llm=llAma
    
)

prompt_agent = Agent(
    role = "promptengineer", 
    goal = f"write a single structured prompt in markdown explaining how a world-class {topic} would approach a project",
    backstory = f"you're an AI assistant that writes a single prompt explaining how a world-class {topic} would approach a project",
    verbose=True,
    allow_delegation=False,
    llm=llAma
    
)


# DEFINE TASKS      ___________________________________________________________ 

gather_info = Task(
    description = f"from your knowledge base, collect relevant information about {topic} experts",
    agents = [research_agent],
    expected_output = f"A clear list of key points related to {topic} experts and how they work",
)

write_prompt = Task(
    description = f"write a single structured prompt in markdown explaining how a world-class {topic} would approach a project",
    agents = [prompt_agent],
    expected_output = f"A single structured prompt in markdown explaining how a world-class {topic} would approach a project",
)


# DEFINE CREW       ___________________________________________________________

crew = Crew(
    
    agents=[Agent(role="researcher", task="collect information")],
    tasks=[Task(description="from your knowledge base, collect relevant information about Web Development experts", agent="researcher")],
    process = Process(mode="sequential")


    # agents = [research_agent, prompt_agent],
    # tasks = [gather_info, write_prompt],
    # verbose = True,
    # process = Process.sequential
)

output = crew.kickoff()
print(output)