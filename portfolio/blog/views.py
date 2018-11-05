from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from app_portfolio.models import Proyecto



def post_list(request):
    
    posts=Proyecto.objects.order_by('titulo')
    return render(request, 'post_list.html', {'posts': posts})

#    post=Proyecto.objects.order_by('descripcion')
#    post = get_object_or_404(posts, pk=pk)
#    print(post)
#    return render(request, 'post_detail.html', {'post': post})

