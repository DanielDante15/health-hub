from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from .views import *

urlpatterns = [
      path('users/', UserList.as_view(), name='user-list'),
    path('users/create', UserCreate.as_view(), name='create-user'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('users/<int:pk>', UserUpdate.as_view(), name='user-update'),
    path('users/<int:pk>', UserDelete.as_view(), name='user-delete'),

]


if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)