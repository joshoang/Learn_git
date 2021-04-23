from django.shortcuts import render, get_object_or_404
from .models import Post, Comment
from blog.forms import CommentForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,decorators
from django.contrib.auth.mixins import LoginRequiredMixin
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, permissions
from .serializers import GetAllPostSerializer, PostPostSerializer

# Create your views here.
from django.views.generic import ListView, DetailView
from django.views import View

class IndexClass(View):
    def get(self,request):
        pass

    def post(self,request):
        pass
    
class PostListView(LoginRequiredMixin,ListView):
    #Cấu hình cho phần check login
    login_url='/login'
    queryset = Post.objects.all().order_by('-date')
    template_name = "blog/blog_generic.html"
    context_object_name = "Posts"
    paginate_by = 2

class PostDetailView(LoginRequiredMixin,DetailView):
    model = Post
    template_name = "blog/post.html"

@decorators.login_required(login_url='/login')
def list(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect("/login")
    Data = {'Posts': Post.objects.all().order_by('-date')}
    return render(request,'blog/blog.html',Data)

@decorators.login_required(login_url='/login')
def post(request,id):
    post = Post.objects.get(id=id)
    return render(request,'blog/post.html',{'post':post})

@decorators.login_required(login_url='/login')
def post_detail_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    form = CommentForm()
    if request.method == "POST":
        form = CommentForm(request.POST, author=request.user, post=post)
        if form.is_valid():
            if request.user.has_perm("blog.add_comment"):
                form.save()
            return HttpResponseRedirect(request.path)
    return render(request, "blog/post.html", {"post": post, "form": form})

class GetAllPost(APIView):
    
    def get(self,request):
        list_post =  Post.objects.all()
        return Response(data=GetAllPostSerializer(list_post, many=True).data , status=status.HTTP_200_OK)
        
    def post(self,request):
        mydata = PostPostSerializer(data = request.data)
        if mydata.is_valid():
            cs = Post.objects.create(title = mydata.data['title'], body = mydata.data['body'])
            return Response(data =cs.id , status=status.HTTP_200_OK)
        return Response(data = "Dữ liệu không hợp lệ" , status=status.HTTP_400_BAD_REQUEST)   

    def put(self,request):
        mydata = PostPostSerializer(data = request.data)
        if mydata.is_valid():
            cs = Post.objects.create(title = mydata.data['title'], body = mydata.data['body'])
            return Response(data =cs.id , status=status.HTTP_200_OK)
        return Response(data = "Dữ liệu không hợp lệ" , status=status.HTTP_400_BAD_REQUEST)   