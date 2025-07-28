from django.db.models import Count
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, status, filters
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from api.authentication import FirebaseAuthentication
from api.models import Post
from api.models.like_model import Like
from api.pagination import StandardCursorPagination
from api.permissions import IsAuthorOrReadOnly
from api.serializers import PostSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_datetime')
    serializer_class = PostSerializer
    authentication_classes = [FirebaseAuthentication]
    pagination_class = StandardCursorPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['author']
    ordering_fields = ['created_datetime', 'likes_count', 'comments_count']
    ordering = ['-created_datetime']

    def get_queryset(self):
        return Post.objects.annotate(
            likes_count = Count('likes', distinct=True),
            comments_count = Count('comments', distinct=True)
        )

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated & IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

    @action(detail=True, methods=['post'], permission_classes=[IsAuthenticated])
    def like(self, request, pk=None):
        post = self.get_object()
        user = request.user

        try:
            like = Like.objects.get(post=post, user=user)
            like.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Like.DoesNotExist:
            Like.objects.create(post=post, user=user)
            return Response(status=status.HTTP_201_CREATED)