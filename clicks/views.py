from django.shortcuts import render

# Create your views here.
def ClickPost(request):
    return render(request, 'clicks/index.html')
