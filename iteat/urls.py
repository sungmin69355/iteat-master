from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
urlpatterns = [
  path('Quizpage/',views.Quizpage,name='Quizpage'),
  path('Quizpage/<int:quiz_id>/',views.Quizdetail, name='Quizdetail'),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

