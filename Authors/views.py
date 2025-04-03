from django.shortcuts import render,redirect
from Book.models import *
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required


# Create your views here.
@login_required(login_url="/login/") 
def dashboard(request):
    book_details = book.objects.all()
    return render(request,"author-dashboard.html",context={"book_details":book_details})

@login_required(login_url="/login/") 
def Authoraddbook(request):
    if request.POST:
            data = request.POST
            Book_Title = data.get("Book-Title")
            Book_Img = request.FILES.get("Book-Img")
            Book_Auth = data.get("Auth-Name")
            Book_Rating = data.get("Book-Rating")
            Book_PDF = request.FILES.get("Book-PDF-File")

            book.objects.create(Title=Book_Title,Book_image=Book_Img,Auth=Book_Auth,Rating=Book_Rating,Book=Book_PDF)

    return render(request,"author-dashboard-addbooks.html")

@login_required(login_url="/login/") 
def AuthorManageBook(request):
    book_details = book.objects.all()

    return render(request,"author-dashboard-manageBooks.html",context={"book_details":book_details})

@login_required(login_url="/login/") 
def AuthorUpdateBook(request,id):
    Queryset = book.objects.get(id=id)
    if request.POST:
            data = request.POST
            Book_Title = data.get("Book-Title")
            book_Img = request.FILES.get("Book-Img")
            Book_Auth = data.get("Auth-Name")
            Book_Rating = data.get("Book-Rating")
            Book_PDF = request.FILES.get("Book-PDF-File")

            Queryset.Title = Book_Title
            Queryset.Auth = Book_Auth
            Queryset.Rating = Book_Rating

            if book_Img:
                 Queryset.Book_image = book_Img

            if Book_PDF:
                 Queryset.Book = Book_PDF

            Queryset.save()
            return redirect("/dashboard/manageBooks/")



    return render(request,"author-dashboard-updatebooks.html",context={'book_details':Queryset})

@login_required(login_url="/login/") 
def AuthorDeleteBook(request,id):
     Queryset = book.objects.get(id=id)

     Queryset.delete() 

     return redirect("/dashboard/manageBooks")

def login_page(request):
     if request.method == "POST":
          U_name = request.POST.get("userName")
          U_pass = request.POST.get("password")

          if not User.objects.filter(username = U_name).exists():
               messages.info(request, "wrong user name")
               return redirect("/login/")

          user = authenticate(username = U_name , password = U_pass)

          if user is None:
               messages.info(request,"wrong password")
               return redirect("/login/")
          
          login(request,user)

          return redirect("/dashboard/")

     return render(request,"login.html")


def logout_page(request):
     logout(request)
     return redirect("/")


def readBook(request,id):
     BOOK = book.objects.get(id=id)
     return render(request,"readpage.html",context={"book":BOOK})