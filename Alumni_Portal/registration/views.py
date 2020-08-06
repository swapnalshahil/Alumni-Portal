from django.shortcuts import render
from django.contrib.auth.models import User
from .forms import UserForm
# Create your views here.


def SignupView(request):
    if request.method=="POST":
        user_form=UserForm(data=request.POST)

        if(user_form.is_valid()):
            user=user_form.save(commit=False)
            user.set_password(user.password)
            user.save()

        else:
            print(user_form.errors)

    else:
        user_form=UserForm()
    return render(request, 'registration/signup.html', {'user_form':user_form})
