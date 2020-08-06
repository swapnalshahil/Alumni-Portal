from django.shortcuts import render,redirect,  get_object_or_404
from django.http import HttpResponse
from alumni_response.forms import ResponseForm1, ResponseForm2a, ResponseForm2b, ResponseForm2c, ResponseForm3, CurrentUpdateForm
from django.views.generic import TemplateView
from django.core.validators import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Response, Higher, Job, Start_Up, Contact
from django.views.generic.edit import UpdateView
# Create your views here.


# class ResponseView(TemplateView):
#     template_name='alumni_response/response.html'
@login_required
def response1(request):
    if request.method=='POST':
        form=ResponseForm1(request.POST)
        if form.is_valid():
            response=form.save(commit=False)
            response.alumni=request.user
            response.save()
            if(response.post_college=='Higher studies'):
                return redirect('alumni_response:form2a')
            elif(response.post_college=='Job'):
                return redirect('alumni_response:form2b')
            elif(response.post_college=='Entrepreneurship'):
                return redirect('alumni_response:form2c')
        else:
            message.success(request, "Please enter a valid passout year!")
            return redirect('alumni_response:form1')
    else:
        form=ResponseForm1()
        heading="Alumni's Response"
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})

@login_required
def response2a(request):
    if request.method=='POST':
        form=ResponseForm2a(request.POST)
        if form.is_valid():
            response=form.save(commit=False)
            response.alumni=request.user
            response.save()
            return redirect('alumni_response:form3')
    else:
        form=ResponseForm2a()
        heading='Higher Studies'
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})

@login_required
def response2b(request):
    if request.method=='POST':
        form=ResponseForm2b(request.POST)
        if form.is_valid():
            response=form.save(commit=False)
            response.alumni=request.user
            response.save()
            return redirect('alumni_response:form3')
    else:
        form=ResponseForm2b()
        heading='Job'
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})



@login_required
def response2c(request):
    if request.method=='POST':
        form=ResponseForm2c(request.POST)
        if form.is_valid():
            response=form.save(commit=False)
            response.alumni=request.user
            response.save()
            return redirect('alumni_response:form3')
    else:
        form=ResponseForm2c()
        heading='Start Up'
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})

@login_required
def response3(request):
    if request.method=='POST':
        form=ResponseForm3(request.POST)
        if form.is_valid():
            response=form.save(commit=False)
            response.alumni=request.user
            response.save()
            return HttpResponse("Thank You")
    else:
        form=ResponseForm3()
        heading='How to Connect'
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})
# return HttpResponse has to be changed


@login_required
def update_current(request,pk):
    if request.method=='POST':
        form=CurrentUpdateForm(request.POST)
        if form.is_valid():
            response=form.save()
            return HttpResponse("Thank You")
    else:
        form=CurrentUpdateForm()
        heading='Update Current Job'
        obj=get_object_or_404(Response, pk=pk)
        form=CurrentUpdateForm(instance=obj)
        return render(request,'alumni_response/response.html' ,{'form':form,'heading':heading})

class CurrentUpdateView(UpdateView):
    model=Response
    form_class=CurrentUpdateForm
    template_name='alumni_response/response.html'
