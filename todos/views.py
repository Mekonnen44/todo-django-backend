from rest_framework import viewsets, generics
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.permissions import IsAuthenticated

# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all().order_by('-created_at')
#     serializer_class = TodoSerializer

# GET all todos + CREATE new todo
class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user).order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

# GET one todo + UPDATE + DELETE
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TodoSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)