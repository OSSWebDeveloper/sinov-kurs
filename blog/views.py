from django.shortcuts import get_object_or_404, redirect, render
from django.db.models import Q
from django.urls import reverse
from blog.forms import RegisterForm
from blog.models import Post

# Create your views here.
def index(request):
    posts = Post.objects.order_by("-date")[:3]
    return render(request , 'blog/index.html' , {'posts':posts})

def posts(request):
    posts = Post.objects.order_by("-date")
    return render(request , 'blog/posts.html' , {'posts':posts})

def post(request , id):
    post = get_object_or_404(Post , id=id)
    return render(request , 'blog/post.html' , {'post':post})

def search_result(request):
    query = request.GET.get('search')
    search_obj = Post.objects.filter(
        Q(title__icontains=query) |Q(des__icontains=query)
    )
    return render(request, 'blog/search.html', {'search_obj':search_obj, 'query':query})

def register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #log the user in
            return redirect('index')
    else:
        form = RegisterForm()
    return render(request, 'blog/register.html', {'form':form})


def comment(request, id):
    post = get_object_or_404(Post , id=id)
    if request.method == 'POST':
        comment = post.comment_set.create(
            author = request.user,
            text = request.POST.get('text')
        )
        if request.user.is_superuser:
            comment.publish = True
            comment.save()
    return redirect(reverse('post', kwargs={'id': id}))
