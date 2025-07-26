from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import Post, Comment, Like
from .permissions import IsAuthorOrReadOnly
from .serializers import PostSerializer, CommentSerializer
from .authentication import FirebaseAuthentication

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated & IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer
    authentication_classes = [FirebaseAuthentication]
    permission_classes = [IsAuthenticated & IsAuthorOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        """ Ação para dar like/unlike em um post. """
        post = self.get_object()
        user = request.user

        try:
            like = Like.objects.get(post=post, user=user)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            Like.objects.create(post=post, user=user)
            return Response(status=status.HTTP_201_CREATED)