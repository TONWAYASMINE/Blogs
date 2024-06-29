from django.shortcuts import render, HttpResponse
from .models import Article
from .groq_client import GroqClient
from django.views import View
from django.http import JsonResponse

# Create your views here.

def index(request):
    posts = Article.objects.all()
    return render(request, 'index.html', {'posts': posts})

class ChatView(View):
    client = GroqClient()

    def post(self, request):
        user_message = request.POST.get('message')
        try:
            response = self.client.send_message(user_message)
            return JsonResponse({'response': response})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
# Create your views here.
