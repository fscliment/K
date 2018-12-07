from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from app_portfolio.models import Proyecto
from app_portfolio.models import Blog



def post_list(request):
    
    
    contexto = {}
    
    contexto['posts'] = Proyecto.objects.order_by('titulo')
    contexto['blog_files'] = Blog.objects.all()
    
    return render(request, 'post_list.html', contexto)

#    post=Proyecto.objects.order_by('descripcion')
#    post = get_object_or_404(posts, pk=pk)
#    print(post)
#    return render(request, 'post_detail.html', {'post': post})

