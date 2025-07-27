from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from api.authentication import FirebaseAuthentication
from api.models import Comment, Post
from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated & IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)