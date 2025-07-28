from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets, filters
from rest_framework.permissions import IsAuthenticated, AllowAny
from api.authentication import FirebaseAuthentication
from api.models import Comment, Post
from api.pagination import StandardCursorPagination
from api.permissions import IsAuthorOrReadOnly
from api.serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    authentication_classes = [FirebaseAuthentication]
    pagination_class = StandardCursorPagination

    filter_backends = [DjangoFilterBackend, filters.OrderingFilter]
    filterset_fields = ['author']
    ordering_fields = ['created_datetime']

    def get_queryset(self):
        return self.queryset.filter(post=self.kwargs['post_pk'])


    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            permission_classes = [AllowAny]
        else:
            permission_classes = [IsAuthenticated & IsAuthorOrReadOnly]
        return [permission() for permission in permission_classes]

    def perform_create(self, serializer):
        post = Post.objects.get(pk=self.kwargs['post_pk'])
        serializer.save(author=self.request.user, post=post)