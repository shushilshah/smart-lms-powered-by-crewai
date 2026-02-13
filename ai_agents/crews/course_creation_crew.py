from crewai import Crew
from ai_agents.tasks.plan_course import plan_course_task

def create_course_crew(teacher_prescription: str):
    task = plan_course_task(teacher_prescription)

    crew = Crew(
        agents= [task.agent],
        tasks= [task],
        verbose=True
    )
    return crew