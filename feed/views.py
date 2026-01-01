from django.shortcuts import render
from datetime import datetime

# Create your views here.
def index(request):
   contexte = {
        "messages": [
          {
            "content": "texte",
            "username": "MB",
            "created_at": datetime.now()
          },
           {
            "content": "texte",
            "username": "MB",
            "created_at": datetime.now()
          },
           {
            "content": "texte",
            "username": "MB",
            "created_at": datetime.now()
          }

        ]
    }   
   return render(request, template_name= 'index.html', context=contexte)