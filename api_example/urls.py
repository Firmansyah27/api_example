
from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('languages.urls')),
    path('api-auth/', include('rest_framework.urls')),
    path('home/', views.home, name="home")
    
]
