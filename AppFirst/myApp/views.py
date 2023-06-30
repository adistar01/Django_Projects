from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .forms import *

# Create your views here.
def myfunctioncall(request):
    return HttpResponse("Hello World")

def myfunctionabout(request):
    return HttpResponse("About")

def myfunctionadd(request, a, b):
    return HttpResponse(a+b)


def myhtmpage(request):
    return render(request, 'index.html')

def secpage(request):
    return render(request, 'second.html')

def thirdpage(request):
    mydict = {
        "var" : "HELLOO !",
        "msg" : "Greetings ! How are you ?"
    }
    return render(request, 'third.html', context=mydict)

def imgpg(request):
    return render(request, 'imgpg.html')

def myform(request):
    if request.method=="POST":
        form = FeedbackForm(request.POST)
        if form.is_valid():
            title = request.POST['title']
            subject = request.POST['subject']
            print(title)
            print(subject)
            var = str('Form submitted'+ str(request.method))
            return HttpResponse(var)
        else:
            mydict = {
                "form":form
            }
            return render(request,'myform.html',context=mydict)

    elif request.method=='GET':
        form = FeedbackForm()
        mydictionary = {
            "form" : form
        }
        return render(request, "myform.html", context=mydictionary)