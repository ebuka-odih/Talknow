from django.shortcuts import render
from .models import Post

def home(request):
    latest = Post.objects.order_by('-timestamp')

    context = {
        'latest': latest
    }
    return render(request, 'index.html', context)