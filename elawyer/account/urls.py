from rest_framework.routers import SimpleRouter
from django.urls import include, path
from .api import AccountViewSet

app_name = 'account'

api = [
    path('create/', AccountViewSet.as_view({'post': 'create'}), name='create-account'),
    path('retrieve/<int:pk>/', AccountViewSet.as_view({'get': 'retrieve'}), name='retrieve-account'),
    path('update/', AccountViewSet.as_view({'post': 'update'}), name='update-account'),
    path('list/', AccountViewSet.as_view({'get': 'list'}), name='list-account'),
]

urlpatterns = [
    path('api/', include(api))
]