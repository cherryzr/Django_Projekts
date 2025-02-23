from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from .models import Task
import json

# creating API endpoints to list, add, update, and delete tasks.


# index view
def index(request):
    return render(request, "index.html")


@csrf_exempt  # Temporarily disable CSRF protection for testing
def get_tasks(request):
    tasks = list(Task.objects.values())
    return JsonResponse(tasks, safe=False)


@csrf_exempt
def add_task(request):
    if request.method == "POST":
        data = json.loads(request.body)
        task = Task.objects.create(title=data["title"])
        return JsonResponse(
            {"id": task.id, "title": task.title, "completed": task.completed}
        )


@csrf_exempt
def delete_task(request, task_id):
    if request.method == "DELETE":
        task = get_object_or_404(Task, id=task_id)
        task.delete()
        return JsonResponse({"message": "Task deleted"})


@csrf_exempt
def update_task(request, task_id):
    if request.method == "POST":
        task = get_object_or_404(Task, id=task_id)
        data = json.loads(request.body)
        task.completed = data.get("completed", task.completed)
        task.save()
        return JsonResponse({"message": "Task updated"})
