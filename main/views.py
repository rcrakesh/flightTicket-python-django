from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import ToDoList , Item
from .forms import CreateNewList

# def index(response, id):
#     ls = ToDoList.objects.get(id=id)

#     if response.method == "POST":
#          if response.POST.get("save"):
#               for item in ls.item_set.all():
#                    if response.POST.get("c"+ str(item.id))=="clicked":
#                         item.complete = True
#                    else:
#                         item.complete = False
#                    item.save() 
#          elif response.POST.get("newitem"):
#             txt = response.POST.get("new")
#             if len(txt)>2:
#                  ls.item_set.create(text=txt , complete=False)
#             else:
#                  print("invalid")     
#     # item = ls.item_set.get(id=1)
#     return render(response,"main/list.html",{"ls":ls})


# def home(response):
#      return render(response,"main/home.html",{})

# def create(response):
#      if response.method == "POST":
#           form = CreateNewList(response.POST)

#           if form.is_valid():
#                n = form.cleaned_data["name"]
#                t=ToDoList=n
#                t.save()
#           return HttpResponseRedirect("/%i" %t.id)    
#      else:
#           form = CreateNewList()     

#     #  form = CreateNewList()
#      return render(response,"main/create.html",{"form":form})


# def v1(response):
#     return HttpResponse("<h1> view the page</h1>")
def add(request):
     if 'num1' in request.POST and 'num2' in request.POST:
            num1 = int(request.POST['num1'])
            num2 = int(request.POST['num2'])
            result = num1 + num2
          #   return HttpResponse(f'The sum of {num1} and {num2} is {result}')
            return render(request, 'main/result.html' , {'result': result})
     else:
              return render(request, 'main/create.html')
