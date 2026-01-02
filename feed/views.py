from django.shortcuts import render
from feed.models import Message
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