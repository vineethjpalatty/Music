from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.views import View
# Create your views here.
class signup1(View):
    def get(self, request):
        form = UserCreationForm()

        return render(request, 'registration/signup.html', {'form': form})

    def post(self, request):

        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
