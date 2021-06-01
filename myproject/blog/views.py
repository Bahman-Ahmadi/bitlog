from django.shortcuts import render
from blog.models import Post

def main(request):
	context = {"listPost": Post.objects.filter(status='p').order_by('-created')}
	return render(request, "blog/index.html", context=context)

def page(request, slug):
	context = {"post": Post.objects.get(slug=slug)}
	return render(request, "blog/page.html", context=context)