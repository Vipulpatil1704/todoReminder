# from django.shortcuts import render

# # Create your views here.
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Task
from .serializers import TaskSerializer
from bson import ObjectId

class TaskListCreateView(APIView):
    def get(self, request):
        tasks = Task.objects.all()
        serializer = TaskSerializer(tasks, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = TaskSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class DeleteAllTasksView(APIView):
    def delete(self, request):
        Task.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class TaskDetailView(APIView):
   
    def put(self, request, pk):
        try:
            # task = Task.objects.get(pk=pk)
            object_id = ObjectId(pk)  # Ensure pk is a valid ObjectId
            task = Task.objects.get(_id=object_id)  # Use the `_id` field for MongoDB lookup
            serializer = TaskSerializer(task, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def delete(self, request, pk):
        try:
            # task = Task.objects.get(pk=pk)
            object_id = ObjectId(pk)  # Ensure pk is a valid ObjectId
            task = Task.objects.get(_id=object_id)  # Use the `_id` field for MongoDB lookup
            task.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Task.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

