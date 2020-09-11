from django.db import models

# Create your models here.
class Quiz(models.Model):
  objects = models.Manager()
  title = models.CharField(max_length=300) # 길이 제한이 있는 문자열
  content = models.TextField() 

  def __str__(self):
    return self.title