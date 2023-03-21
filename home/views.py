from django.shortcuts import render, redirect
from .models import Post, Comment
from .forms import PostForm, CommentForm
import random
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist

def homePage(request):
    trand = Post.objects.all()[:6]
    post = Post.objects.all
    context = {'post':post, 'trand':trand}
    return render(request, 'home/home.html',context)

def blogPage(request):
    post = Post.objects.all()[:10]
    context = {'post':post}
    return render(request, 'home/blog.html',context)

def post(request, pk):
    post = Post.objects.get(pk=pk)

    if request.method == 'POST':
        c_form = CommentForm(request.POST)
        if c_form.is_valid():
            comment = c_form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post', pk=post.pk)
        else:
            print(form.errors.as_data())
    else:
        try:
            comment = Comment.objects.filter(post=post)
        except ObjectDoesNotExist:
            comment = None
        c_form = CommentForm()
        post.views += 1
        post.save()
        form = PostForm(instance=post)
        article = True
        if comment == None:
            context = {'post': post, 'form': form, 'article':article, 'c_form':c_form}
        else:
            context = {'post': post, 'form': form, 'article':article, 'comment':comment , 'c_form':c_form}
        return render(request, 'home/post.html', context)
        

@login_required
def newPost(request):
    if request.method == 'POST':
        print('posting')
        form = PostForm(request.POST, request.FILES)
        print(form)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post', pk=post.pk)
        else:
            print(form.errors.as_data())
    else:
        form = PostForm()
    return render(request, 'home/post.html', {'form': form})

@login_required
def editPost(request,pk):
    post = Post.objects.get(id=pk)
    form = PostForm(instance=post)
    if request.method == 'POST':
        form = PostForm(request.POST,instance=post)
        if form.is_valid():
            form.save()
            return redirect('post',pk = post.pk)
    context = {'post':post, 'form': form}
    return render(request,'home/post.html',context)

@login_required
def deletePost(request,pk):
    post = Post.objects.get(id=pk)
    post.delete()
    return redirect('blogPage')

@login_required
def deleteComment(request,pk):
    comment = Comment.objects.get(id=pk)
    post = comment.post.id
    comment.delete()
    return redirect('post', pk=post)

def about(request):
    name = 'John Doe'
    profession = random.choice(['web developer', 'graphic designer', 'writer'])
    city = random.choice(['New York City', 'London', 'Tokyo'])
    hobbies = random.choice(['play soccer', 'read books', 'watch movies'])
    favorite_color = random.choice(['blue', 'green', 'red'])
    favorite_music_genre = random.choice(['rock', 'pop', 'hip-hop'])
    favorite_movie = random.choice(['The Godfather', 'The Shawshank Redemption', 'Forrest Gump'])
    another_hobby = random.choice(['paint', 'cook', 'travel'])
    
    context = {
        'name': name,
        'profession': profession,
        'city': city,
        'hobbies': hobbies,
        'favorite_color': favorite_color,
        'favorite_music_genre': favorite_music_genre,
        'favorite_movie': favorite_movie,
        'another_hobby': another_hobby
    }
    
    return render(request, 'about.html', context)

