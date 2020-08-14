from django.shortcuts import render,HttpResponseRedirect
from django.http import HttpResponse
from .models import t
# Create your views here.
def dtodo(request):
  d={
    "dis":t.objects.all()
  }
  return render(request,'todoapp/todo.html',d)
def atodo(request):
  a=t(c=request.POST['content'],author=request.POST['author'])
  a.save()
  return HttpResponseRedirect('/')
def deltodo(request,di):
  print(request.POST)
  d=t.objects.get(id=di)
  d.delete()
  return HttpResponseRedirect('/')
