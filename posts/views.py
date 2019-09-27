from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import ModelPost
from django.views import View

from .forms import PostForm

# Create your views here.
def BlogView1(request):
    if request.method == 'POST':

        form = PostForm(request.POST)
        form.save()
        return redirect('home')
    else:
        form = PostForm()
        return render(request,'posts/hello.html',{
            'form': form,
        })

class Blog(View):
    def get(self,request):
        form = PostForm()
        return render(request, 'posts/hello.html', {
            'form': form,
        })
    def post(self,request):
        form = PostForm(request.POST)
        form.save()
        return redirect('home')




def BlogView2(request):
    posts=ModelPost.objects.all()
    form=PostForm
    args={'posts':posts,'form':form}
    return render(request,"posts/show.html",args)

def BlogView3(request):
    return HttpResponse("hi3")

def BlogView4(request):
    return HttpResponse("hi4")
