from django.shortcuts import render
from blog.models import Blog, Category

# Görünümleri burada oluşturun
def index(request):
    context = {
        "blogs": Blog.objects.filter(is_home=True, is_active=True),
        "categories": Category.objects.all(),
    }
    return render(request, "blog/index.html", context)

def blogs(request):
    context = {
        "blogs": Blog.objects.filter(is_active=True),
        "categories": Category.objects.all(),
    }
    return render(request, "blog/blogs.html", context)

def blog_details(request, slug):
    selectedBlog = Blog.objects.get(slug=slug)
    context = {
        "blog": selectedBlog
    }
    return render(request, "blog/blog-details.html", context)

def blogs_by_category(request, slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug,
    }
    return render(request, "blog/blogs.html", context)
