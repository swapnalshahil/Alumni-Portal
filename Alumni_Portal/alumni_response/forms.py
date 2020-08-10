from django import forms
from alumni_response.models import Response, Higher, Job, Start_Up, Contact
from django.core.validators import MaxValueValidator, MinValueValidator

STATUS=[
    ('Higher studies','Higher studies'),
    ('Job','Job'),
    ('Entrepreneurship','Entrepreneurship')
]

CONTACT=[
    ('LinkedIn','LinkedIn'),
    ('Facebook','Facebook'),
    ('Email','Email')
]

BRANCH=[
    ('CSE','Computer Science and Engineering'),
    ('MNC','Mathematics and Computing'),
    ('EEE','Electronics and Electrical Engineering'),
    ('ME','Mechanical Engineering'),
    ('Civil','Civil Engineering'),
    ('CST','Chemical Science and Technology'),
    ('CE','Chemical Engineering'),
    ('BT','Biotech'),
    ('EP','Engineering Physics'),
    ('ECE','Electronics and Communication Engineering')
]


class ResponseForm1(forms.ModelForm):
    passout_year=forms.IntegerField(label='Passout Year:',validators=[MaxValueValidator(2020), MinValueValidator(1999)])
    post_college=forms.ChoiceField(label='Your career choice just after graduation:', choices=STATUS)
    current_job=forms.CharField(label='Short Description about your current job or higher education:', widget=forms.Textarea, help_text='please mention your position(post) and your current company')
    department=forms.ChoiceField(label='Branch:', choices=BRANCH)
    class Meta():
        model=Response
        fields=('passout_year','department','current_job','post_college')


class ResponseForm2a(forms.ModelForm):
    programme=forms.CharField(label='Programme:')
    university=forms.CharField(label='University:')
    books=forms.CharField(label='Important Books which should be followed:')
    additional_tips=forms.CharField(label='Addtional Advice:',widget=forms.Textarea)
    class Meta():
        model=Higher
        fields=('programme','university','books','additional_tips')

class ResponseForm2b(forms.ModelForm):
    profile=forms.CharField(label='Job-Profile:')
    company=forms.CharField(label='Company:')
    interview_ques=forms.CharField(label='Questions that were asked in Interviews:',widget=forms.Textarea)
    books=forms.CharField(label='Important Books which should be followed:')
    additional_tips=forms.CharField(label='Addtional Advice:',widget=forms.Textarea)
    class Meta():
        model=Job
        fields=('profile','company','interview_ques','books','additional_tips')

class ResponseForm2c(forms.ModelForm):
    startup_name=forms.CharField(label='Name of Start-up:')
    books=forms.CharField(label='Important Books which should be followed:')
    startup_description=forms.CharField(label='Start-up Description:',widget=forms.Textarea)
    additional_tips=forms.CharField(label='Addtional Advice:',widget=forms.Textarea)
    class Meta():
        model=Start_Up
        fields=('startup_name','startup_description','books','additional_tips')

class ResponseForm3(forms.ModelForm):
    advice=forms.CharField(label="Advice you would like to give to your juniors:",widget=forms.Textarea)
    contact=forms.ChoiceField(label='Where can juniors connect with you:',choices=CONTACT)
    class Meta():
        model=Contact
        fields=('contact','advice')


class CurrentUpdateForm(forms.ModelForm):
    current_job=forms.CharField(label='Short Description about your current job or higher education:', widget=forms.Textarea, help_text='please mention your position(post) and your current company')
    class Meta():
        model=Response
        fields=('current_job',)
