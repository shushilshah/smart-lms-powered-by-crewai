import json
from ai_agents.crews.course_creation_crew import create_course_crew

def run_course_planner(teacher_prescription: str) -> dict:
    crew = create_course_crew(teacher_prescription)
    result = crew.kickoff()
    raw_output = result.raw

    try:
        return json.loads(raw_output)

    except json.JSONDecodeError:
        print("AI returned invalid JSON")
        print(raw_output)
        raise