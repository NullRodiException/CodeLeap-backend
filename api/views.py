from rest_framework import viewsets
from .models import Post
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .authentication import FirebaseAuthentication

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer

    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated & IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)
