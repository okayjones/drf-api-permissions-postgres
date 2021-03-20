from rest_framework import generics
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from tasks.permissions import IsOwnerOrReadOnly
from .serializer import TaskSerializer
from .models import Task


class TaskList(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticatedOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsOwnerOrReadOnly,)
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
