from django.shortcuts import render
from feed.models import Message
from django.http import HttpResponse
# Create your views here.
def index(request):
   if request.method == 'POST':
      content = request.POST.get('content')
      user = request.user
      print(content, user)
      Message.objects.create(content = content, user = user)
   contexte = {}
   contexte ['messages'] = Message.objects.order_by('-created_at')

   return render(request, template_name= 'index.html', context=contexte)

def details(request, id):
   if request.method == 'POST':
      content = request.POST.get('content')
      user = request.user
      Message.objects.create(content = content, user = user, response_to_id = id)

   context = {}
   context['message'] = Message.objects.get(id=id)
   context['comments'] = Message.objects.filter(response_to = id)
   print(context)
   return render(request, 'details.html', context=context)