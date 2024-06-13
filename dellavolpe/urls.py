# project_name/urls.py
from django.urls import path, include
from dispositivos.views import DispositivoViewSet

urlpatterns = [
    path('dispositivos/', DispositivoViewSet.as_view({
        'get': 'list',   
        'post': 'create' 
    }), name='dispositivos-list'),
    path('dispositivos/<int:pk>/', DispositivoViewSet.as_view({
        'get': 'retrieve',    
        'put': 'update',      
        'delete': 'destroy'   
    }), name='dispositivos-detail'),
]

