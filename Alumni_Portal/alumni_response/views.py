from django.shortcuts import render,redirect,  get_object_or_404
from django.http import HttpResponse
from alumni_response.forms import ResponseForm1, ResponseForm2a, ResponseForm2b, ResponseForm2c, ResponseForm3, CurrentUpdateForm
from django.views.generic import TemplateView, DetailView
from django.core.validators import ValidationError
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Response, Higher, Job, Start_Up, Contact
from django.views.generic.edit import UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

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
                return redirect('alumni_response:form2a', pk=response.pk)
            elif(response.post_college=='Job'):
                return redirect('alumni_response:form2b',  pk=response.pk)
            elif(response.post_college=='Entrepreneurship'):
                return redirect('alumni_response:form2c',  pk=response.pk)
        else:
            messages.success(request, "Please enter a valid passout year!")
            return redirect('alumni_response:form1', pk=response.pk)
    else:
        form=ResponseForm1()
        heading="Alumni's Response"
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})

@login_required
def response2a(request,pk):
    response=get_object_or_404(Response, pk=pk)
    if request.method=='POST':
        form=ResponseForm2a(request.POST)
        if form.is_valid():
            higher=form.save(commit=False)
            higher.alumni=request.user
            higher.response=response
            higher.save()
            return redirect('alumni_response:form3', pk=response.pk)
    else:
        form=ResponseForm2a()
        heading='Higher Studies'
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})

@login_required
def response2b(request, pk):
    response=get_object_or_404(Response, pk=pk)
    if request.method=='POST':
        form=ResponseForm2b(request.POST)
        if form.is_valid():
            job=form.save(commit=False)
            job.alumni=request.user
            job.response=response
            job.save()
            return redirect('alumni_response:form3', pk=response.pk)
    else:
        form=ResponseForm2b()
        heading='Job'
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})



@login_required
def response2c(request, pk):
    response=get_object_or_404(Response, pk=pk)
    if request.method=='POST':
        form=ResponseForm2c(request.POST)
        if form.is_valid():
            start=form.save(commit=False)
            start.alumni=request.user
            start.response=response
            start.save()
            return redirect('alumni_response:form3', pk=response.pk)
    else:
        form=ResponseForm2c()
        heading='Start Up'
        return render(request,'alumni_response/response.html',{'form':form,'heading':heading})

@login_required
def response3(request, pk):
    response=get_object_or_404(Response, pk=pk)
    if request.method=='POST':
        form=ResponseForm3(request.POST)
        if form.is_valid():
            contact=form.save(commit=False)
            contact.alumni=request.user
            contact.response=response
            contact.save()
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

# class CurrentUpdateView(UpdateView):
#     model=Response
#     form_class=CurrentUpdateForm
#     template_name='alumni_response/response.html'


def alumni_list(request):
    response=Response.objects.all()
    context={}
    context['response']=response
    return render(request,'index.html', context)


class AlumniDetail(LoginRequiredMixin, DetailView):
    model=Response
    context_object_name='Alumni'
