from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ai_agents.services.run_course_agent import run_course_planner
from lms_app.models import Course

@csrf_exempt
def generate_course(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            prescription = body.get("prescription")

            if not prescription:
                return JsonResponse({"error": "Prescription is required"}, status=400)
            
            result  = run_course_planner(prescription)
            level_value = result.get("level", "beginner").lower()
            outcomes = result.get("learning_outcomes", [])
            if isinstance(outcomes, list):
                outcomes_text = "\n".join(outcomes)
            else:
                outcomes_text = str(outcomes)

            course = Course.objects.create(
                title = result.get("title"),
                description = result.get("description"),
                # student_slots = result.get("student_slots"),
                level = level_value,
                duration = result.get("duration"),
                teacher = request.user,
                learning_outcomes = outcomes_text,
                is_published = False

            )

            return JsonResponse({
                "id": course.id,
                "title": course.title,
                "description": course.description,
                "level": course.level,
                "duration": course.duration,
                "learning_outcomes": outcomes_text,
                "message": "Saved to database successfully"
            })
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
        

def course_generator_page(request):
    return render(request, "ai_teacher/ai_course_generator.html")