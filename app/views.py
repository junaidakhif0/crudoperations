from django.shortcuts import render

# Create your views here.
from app.models import *
from django.db.models.functions import Length
from django.db.models import Q
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

    #fieldlooups
    
    W=Webpage.objects.filter(name__startswith='D')
    W=Webpage.objects.filter(name__endswith='i')
    W=Webpage.objects.filter(name__contains='H')
    W=Webpage.objects.filter(name__in=('Kohli','AKHIF'))
    W=Webpage.objects.filter(name__regex='[a-zA-Z]{4}')
    W=Webpage.objects.filter(name__startswith='D')
    W=Webpage.objects.filter(Q(topic_name='Cricket') & Q(name='DHONI'))
    W=Webpage.objects.filter(Q(topic_name='Cricket'))
    
    e={'webpages':W}
    
    return render(request,'displaywebpage.html',e)

def displayaccessrecords(request):

    A=AccessRecords.objects.all()
    A=AccessRecords.objects.filter(date='2001-1-1')
    A=AccessRecords.objects.filter(date__gt='2001-1-1')
    A=AccessRecords.objects.filter(date__gte='2001-1-1')
    A=AccessRecords.objects.filter(date__lt='2005-1-1')
    A=AccessRecords.objects.filter(date__lte='2005-1-1')
    A=AccessRecords.objects.filter(date__year='2005')
    A=AccessRecords.objects.filter(date__month='1')
    A=AccessRecords.objects.filter(date__day='1')
    A=AccessRecords.objects.filter(date__year__gt='2005')
    A=AccessRecords.objects.filter(date__month__gt='1')
    


    f={'accessrecords':A}
    
    return render(request,'displayaccessrecord.html',f)
