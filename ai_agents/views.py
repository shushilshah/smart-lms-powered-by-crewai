from django.shortcuts import render
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ai_agents.services.run_course_agent import run_course_planner

@csrf_exempt
def generate_course(request):
    if request.method == 'POST':
        try:
            body = json.loads(request.body)
            prescription = body.get("prescription")

            if not prescription:
                return JsonResponse({"error": "Prescription is required"}, status=400)
            
            result  = run_course_planner(prescription)
            return JsonResponse(result, safe=False)
        
        except Exception as e:
            return JsonResponse({"error": str(e)}, status=500)
        
    return JsonResponse({"error": "Only POST method allowed"}, status=405)
        

def course_generator_page(request):
    return render(request, "ai_teacher/ai_course_generator.html")