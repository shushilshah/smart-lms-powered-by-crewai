from crewai import Agent
from ai_agents.config.llm import get_llm

course_planner_agent = Agent(
    role="Course Planner",
    goal="Design a structured online course based on teacher input",
    backstory="You are a senior curriculum archtect with deep teaching experience",
    llm=get_llm(),
    verbose=True
)