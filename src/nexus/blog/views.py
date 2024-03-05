from django.shortcuts import render

from .forms import CommentForm
from .models import Post, Comment
from django.db.models import Count, F



def blog_list(request):
    posts = Post.objects.annotate(comment_count=Count('comment'),
                                  author_name=F('author__username')
                                  ).values('id', 'title', 'image', 'content', 'post_date', 'comment_count',
                                           'author_name',)
    print(posts)

    ctx = {
        'posts': posts
    }
    return render(request, 'blog.html', ctx)


def blog_detail(request, pk):

    form = CommentForm()
    if request.POST:
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save()
            comment.post = Post.objects.get(id=pk)
            comment.author = request.user
            comment.save()
    post = Post.objects.annotate(
        comment_count=Count('comment'),
        author_name=F('author__username')
    ).filter(pk=pk).values('id', 'title', 'image', 'content', 'post_date', 'comment_count', 'author_name')

    comments = Comment.objects.filter(post_id=pk).select_related('author')
    print(post)
    print(comments)
    ctx = {
         'post': post[0],
        'comments': comments,
        'form': form
     }
    return render(request, 'blog_detail.html', ctx)
