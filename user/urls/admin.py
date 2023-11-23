from django.urls import path
from rest_framework.routers import SimpleRouter

from user.views.admin import AdminLoginView, UserViewSet

router = SimpleRouter()
router.register('users', UserViewSet, basename='users-admin')
urlpatterns = [
                  path('login/', AdminLoginView.as_view())
              ] + router.urls
