from django.shortcuts import render ,  get_object_or_404
from .models import userData , stands , standImage
from django.contrib.auth.models import User
from time import gmtime, strftime
from . import searchAlgorithms
from django.contrib.auth.models import User


# Create your views here.
def dashboard_page(request):
    try :
        #user object 
        user = (userData.objects.get(username=User.objects.get(username=request.user.username)))
        #context
        context = {
           "name" : user.name,
            "surname" : user.surname,
            "profileImage" : user.profilePhoto.url
        }

        return render(request,'dashboard/dashboard.html',context)
    except :
        print("got exception")

    return render(request,'dashboard/dashboard.html')

def home_page(request):
    #user object 
    user = (userData.objects.get(username=User.objects.get(username=request.user.username)))

    #userStands = stands.objects.get(owner=user)
    userStands = stands.objects.filter(owner=user)

    #context
    context = {
        "username" : user.username,
        "name" : user.name,
        "surname" : user.surname,
        "profileImage" : user.profilePhoto.url,
        "verificationCode" : user.verificationCode,
        "verified" : user.verified,
        "userStands" : userStands,
        "credit" : user.credit,
        "standsCount" : len(stands.objects.filter(purchased=False))
    }
    return render(request,'home/home.html',context)

def myStands_page(request):
    #user object 
    user = (userData.objects.get(username=User.objects.get(username=request.user.username)))
    #userStands = stands.objects.get(owner=user)
    userStands = stands.objects.filter(owner=user)
    context = {
        "userStands" : userStands,
        "time" : strftime("%Y-%m-%d %H:%M:%S", gmtime())
    }
    return render(request,"myStands/myStands.html",context)
    

def residential_stands_page(request):
    if (request.method == "GET"):
        searchParametre  = request.GET.get("variable1")
        user = (userData.objects.get(username=User.objects.get(username=request.user.username)))
        #userStands = stands.objects.get(owner=user)
        standsAll = stands.objects.filter(purchased=False)
        #if search parametres is not empty search stands
        context = {} #declare before use
        if (searchParametre != None):
            context = searchAlgorithms.searchStand(searchParametre)     
        else:
            context = {
                "stands" : standsAll,
            }
        return render(request,"residentialStands/residentialStands.html",context)
    

def focus_stand_page(request):
    stand  = request.GET.get("variable1")
    context = {
        "data" : stands.objects.get(address=stand)
    }
    return render(request,"residentialStands/standFocus.html",context)

def confirm_purchase_page(request):
    stand  = request.GET.get("variable1")
    context = {
        "data" : stands.objects.get(address=stand)
    }
    return render(request,"residentialStands/confirmPurchase.html" , context)


def celebrate_page(request):
    stand  = request.GET.get("variable1")
    item = stands.objects.get(address=stand)
    #owner
    item.owner = (userData.objects.get(username=User.objects.get(username=request.user.username)))
    #purchased
    item.purchased = True
    #save
    item.save()
    return render(request,"residentialStands/celebrate.html")

def standDetail_page(request):
    #lease
    stand  = request.GET.get("variable1")
    context = {
        "data" : stands.objects.get(address=stand)
    }
    return render(request,"myStands/standDetail.html" , context)

"""
def news_feed(request):
  
    
    context = {
        "msg" : "hello" ,
        "stand" : stands.objects.all()[0]
    }

    return render(request,"feedPage/feed.html" , context)
"""
def news_feed(request):

    user = (userData.objects.get(username=User.objects.get(username=request.user.username)))
    
    context = {
       "gender" : user.gender,
    }

    return render(request,"feedPage/feed.html" , context)

"""
def news_feed(request):
    feeder  = request.GET.get("variable1")
    context = {
    "headline" : feeds.objects.get(address=feeder)
    }
    return render(request,"feedPage/feed.html" , context)
"""
def developers(request):
  
    
    context = {
        "msg" : "hello" ,
        "stand" : stands.objects.all()[0]
    }

    return render(request,"DevelopersPage/developer.html" , context)

def index(request, pagename):
    pagename = '/' + pagename
    pg = get_object_or_404(Page, permalink=pagename)
    context = {
    'title': pg.title,
    'content': pg.bodytext,
    'last_updated': pg.update_date,
    'page_list': Page.objects.all(),
    }
    return render(request, 'pages/page.html', context)
