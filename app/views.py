from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
def displaytopic(request):

    T=Topic.objects.all()
    d={'topics':T}
    return render(request,'displaytopic.html',d)

def displaywebpage(request):

    W=Webpage.objects.all()
    W=Webpage.objects.filter(topic_name='Cricket')
    W=Webpage.objects.filter(topic_name='cricket')
    #W=Webpage.objects.get(topic_name='Cricket)
    W=Webpage.objects.exclude(topic_name='Hockey')
    W=Webpage.objects.all()[1:5:2] #indexing method if we want only particular number of rows onl
    W=Webpage.objects.all().order_by('name')
    W=Webpage.objects.all().order_by('-name')
    W=Webpage.objects.all().order_by(Length('name'))
    W=Webpage.objects.all().order_by(Length('name').desc())
    e={'webpages':W}
    
    return render(request,'displaywebpage.html',e)

def displayaccessrecords(request):

    A=AccessRecords.objects.all()
    A=AccessRecords.objects.filter(date='2001-1-1')
    A=AccessRecords.objects.filter(date__gt='2001-1-1')
    A=AccessRecords.objects.filter(date__gte='2001-1-1')
    A=AccessRecords.objects.filter(date__lt='2005-1-1')
    A=AccessRecords.objects.filter(date__lte='2005-1-1')
    f={'accessrecords':A}
    
    return render(request,'displayaccessrecord.html',f)
