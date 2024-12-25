from .views import *
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'user', UserProfileViewSet.as_view(), basename='user_list')
router.register(r'follow', FollowViewSet.as_view(), basename='follow_list')
router.register(r'post', PostViewSet.as_view(), basename='post_list')
router.register(r'post-like', PostLikeViewSet.as_view(), basename='post-like_list')
router.register(r'comment', CommentViewSet.as_view(), basename='comment_list')
router.register(r'comment-like', CommentLikeViewSet.as_view(), basename='comment-like_list')
router.register(r'story', StoryViewSet.as_view(), basename='story_list')
router.register(r'save', SaveViewSet.as_view(), basename='save_list')
router.register(r'save-item', SaveItemViewSet.as_view(), basename='save-item_list')

urlpatterns = [
    path('', include(router.urls)),
]