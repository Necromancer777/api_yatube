from django.urls import include, path
from rest_framework.authtoken import views
from .views import PostViewSet, GroupViewSet, CommentViewSet
from rest_framework import routers

router_v1 = routers.DefaultRouter()
router_v1.register(r'posts', PostViewSet, basename='post')
router_v1.register(r'groups', GroupViewSet, basename='group')
router_v1.register(r'posts/(?P<post_id>[\d]+)/comments',
                   CommentViewSet, basename='comment')


urlpatterns = [
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router_v1.urls)),
]
