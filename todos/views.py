from rest_framework import viewsets, generics
from .models import Todo
from .serializers import TodoSerializer

# class TodoViewSet(viewsets.ModelViewSet):
#     queryset = Todo.objects.all().order_by('-created_at')
#     serializer_class = TodoSerializer

# GET all todos + CREATE new todo
class TodoListCreateView(generics.ListCreateAPIView):
    serializer_class = TodoSerializer

    def get_queryset(self):
        return Todo.objects.all().order_by('-created_at')

    def perform_create(self, serializer):
        serializer.save()

# GET one todo + UPDATE + DELETE
class TodoDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer