from django.shortcuts import render, get_object_or_404
from .models import Post
import markdown  # Importar la biblioteca markdown

def render_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    post.description = markdown.markdown(post.description)  # Convertir Markdown a HTML
    return render(request, 'post_detail.html', {'post': post})
