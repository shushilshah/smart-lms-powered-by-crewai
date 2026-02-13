from crewai import Task
from ai_agents.agents.course_planner import course_planner_agent
from pathlib import Path

PROMPT_PATH = Path(__file__).resolve().parent.parent / "prompts/course_planner.txt"

def load_prompt():
    return PROMPT_PATH.read_text()

def plan_course_task(teacher_prescription: str):
    return Task(
        description=load_prompt().replace(
            "{{teacher_prescription}}", teacher_prescription
        ),
        agent=course_planner_agent,
        expected_output="Valid JSON describing the course"
    )