from django.shortcuts import render, redirect
from django.http import HttpResponse
from polls.models import Collaborator


# Create your views here.
def index(request):
  return render(request, 'polls/index.html')

def save(request):
  print(request)
  if request.method == 'POST':
    first_name = request.POST.get('first_name')
    last_name = request.POST.get('last_name')
    print(first_name)
    print(last_name)
    c = Collaborator(first_name=first_name, last_name=last_name)
    c.save()
  else:
    print(' ::get request::')

  return redirect('/alan/')