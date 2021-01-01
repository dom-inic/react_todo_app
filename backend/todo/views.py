# todo/views.py

from django.shortcuts import render
from rest_framework import viewsets         
from .serializers import TodoSerializer      
from .models import Todo                     
# a

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
