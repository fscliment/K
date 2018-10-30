from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from app_portfolio.models import Proyecto

posts = Proyecto.objects.all()

def post_list(request):
    
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(posts, pk=pk)
    return render(request, 'post_detail.html', {'post': post})