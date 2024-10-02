"""
URL configuration for app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from random_word.views import *
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('random/', random_view, name='random_form'),
    path('new_word/', WordCreateView.as_view(), name='new_word'),
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('word/<int:pk>/vocabulary_update', WordUpdateView.as_view(), name='vocabulary_update'),
    path('word/<int:pk>/word_delete', WordDeleteView.as_view(), name='word_delete'),
    path('word/<int:pk>/', WordDetailView.as_view(), name='word_detail'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
