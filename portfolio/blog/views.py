from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from app_portfolio.models import Proyecto



def post_list(request):
    
    posts=Proyecto.objects.order_by('titulo')
    return render(request, 'post_list.html', {'posts': posts})


def post_detail(request, pk):
    posts=Proyecto.objects.order_by('titulo')
    post = get_object_or_404(posts, pk=pk)
    print(post)
    return render(request, 'post_detail.html', {'post': post})