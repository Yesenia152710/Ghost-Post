"""ghostpost URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from ghost_app import views

urlpatterns = [
    path('subpost/', views.subpost_view),
    path('votes/', views.votes_view),
    path('boast/', views.boast_view),
    path('roast/', views.roast_view),
    path('downvote/<int:post_id>/', views.downvote_view),
    path('upvote/<int:post_id>/', views.upvote_view),
    path('', views.index_view, name="homepage"),
    path('admin/', admin.site.urls),
]
