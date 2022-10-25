from django.shortcuts import get_object_or_404, redirect, render
from .models import Post
from django.views.generic import ListView, DeleteView
def homeView(request):
    return render(request, 'index.html', {})

class BlogView(ListView):
    template_name = 'blog-index.html'
    context_object_name = 'blogs'
    ordering = ['-id']
    model = Post

def delete(request, pk):
    if request.method == "POST":
            blog = get_object_or_404(Post, pk=pk)
            return render(request, 'del-blog.html', {'blog':blog})
    else:
        return redirect('blog-index')

def delSure(request, pk):
    if request.method == "POST":
        blog = get_object_or_404(Post, pk=pk)
        blog.delete()
        return redirect('blog-index')
    else:
        return redirect('blog-index')


def CreateBlogView(request):
    return render(request, 'create-blog.html', {})

def CreatePost(request):
    errors = {}
    if request.method == "POST":
        title = request.POST['title']
        c = request.POST['content']
        p = Post(Title = title, content=c)
        if len(c) and len(title)>10:
            p.save()
            return redirect('blog-index')
        else:
            errors['len'] = 'small length'
            return render(request, 'create-blog.html', {'err':errors})
    else:
         return redirect('home')

def GetDetail(request, pk):
    obj = Post.objects.get(id=pk)
    return render(request, 'detail.html', {'post':obj})