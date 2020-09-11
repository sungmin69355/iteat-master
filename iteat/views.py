from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Quiz
# Create your views here.

def home(request):
  return render(request, 'main.html')

def Quizpage(request):
  q = Quiz.objects.order_by('-id')
  q_list = Quiz.objects.all().order_by('-id')
  paginator = Paginator(q_list,3)
  page = request.GET.get('page')
  posts = paginator.get_page(page)
  return render(request, 'Quizpage.html',{'quiz':q, 'posts':posts})

def Quizdetail(request, quiz_id):
  q = get_object_or_404(Quiz, pk = quiz_id)
  return render(request, 'Quizdetail.html',{'quiz':q})