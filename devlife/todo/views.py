from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Todo
from .serializers import TodoSerializers
from rest_framework import status


# Create your views here.
def todo_page(request):
    if request.user.is_authenticated():
        if request.method == 'GET':
          return render(request,'todo/todo.html')
    else:
        return redirect('/login')


class TodoData(APIView):
    """
        Managing Todo Data through serializers
    """
    def get(self, request):
        if request.user.is_authenticated():
            tasks = Todo.objects.all().filter(user=request.user.id)
            tasks_serializer = TodoSerializers(tasks, many=True)
            return Response(tasks_serializer.data)
        else:
            return Response("You are not authorized to access!")
    
    def post(self, request):
        if request.user.is_authenticated():   # When user is authenticated
            dict_data = request.data
            dict_data['user'] = request.user.id
            serializer = TodoSerializers(data=dict_data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            else: 
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else: # When user is not authenticated 
            return Response("You are not authorized to access!")
