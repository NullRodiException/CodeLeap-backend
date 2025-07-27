from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework_nested import routers
from .views import PostViewSet, CommentViewSet, UserProfileView

router = DefaultRouter()
router.register(r'', PostViewSet, basename='post')
posts_router = routers.NestedDefaultRouter(router, r'', lookup='post')
posts_router.register(r'comments/', CommentViewSet, basename='post-comments')
urlpatterns = [
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('', include(router.urls)),
    path('', include(posts_router.urls)),
]