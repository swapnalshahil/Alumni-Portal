from django.db import models
from django.contrib.auth.models import User
# Create your models here.

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
    ('Computer Science and Engineering','Computer Science and Engineering'),
    ('Mathematics and Computing','Mathematics and Computing'),
    ('Electronics and Electrical Engineering','Electronics and Electrical Engineering'),
    ('Mechanical Engineering','Mechanical Engineering'),
    ('Civil Engineering','Civil Engineering'),
    ('Chemical Science and Technology','Chemical Science and Technology'),
    ('Chemical Engineering','Chemical Engineering'),
    ('Biotech','Biotech'),
    ('Engineering Physics','Engineering Physics'),
    ('Electronics and Communication Engineering','Electronics and Communication Engineering')
]


class Response(models.Model):
     # User is model of registration
    alumni=models.ForeignKey(User, on_delete=models.CASCADE, related_name='responses',null=True)
    passout_year=models.IntegerField(null=True)
    department=models.CharField(max_length=50, choices=BRANCH,null=True)
    current_job=models.CharField(max_length=1000, null=True)
    post_college=models.CharField(max_length=20, choices=STATUS,null=True)

class Higher(models.Model):
    alumni=models.ForeignKey(User, on_delete=models.CASCADE, related_name='highers',null=True)
    programme=models.CharField(max_length=100,null=True)
    university=models.CharField(max_length=100,null=True)
    books=models.CharField(max_length=500,null=True)
    additional_tips=models.CharField(max_length=5000,null=True)

class Job(models.Model):
    alumni=models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs',null=True)
    profile=models.CharField(max_length=100,null=True)
    company=models.CharField(max_length=100, null=True)
    interview_ques=models.CharField(max_length=1000,null=True)
    books=models.CharField(max_length=500,null=True)
    additional_tips=models.CharField(max_length=5000,null=True)

class Start_Up(models.Model):
    alumni=models.ForeignKey(User, on_delete=models.CASCADE, related_name='startups',null=True)
    startup_name=models.CharField(max_length=100,null=True)
    startup_description=models.CharField(max_length=5000,null=True)
    books=models.CharField(max_length=500,null=True)
    additional_tips=models.CharField(max_length=5000,null=True)

class Contact(models.Model):
    alumni=models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts',null=True)
    advice=models.CharField(max_length=5000,null=True)
    contact=models.CharField(max_length=100, choices=CONTACT,null=True)

    # class Meta():
    #     ordering=[] according to roll no.
