from django.shortcuts import render
from feed.models import Message
# Create your views here.
def index(request):
   contexte = {}   
   
   contexte ['messages'] = Message.objects.order_by('-created_at')

   return render(request, template_name= 'index.html', context=contexte)