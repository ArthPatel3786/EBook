from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Home_page(request):


    book_details = book.objects.all()
   

    if request.GET.get("search"):
        query = request.GET.get("search")
        book_details = book.objects.filter(Title__icontains = query)


    return render(request,"index.html",context={"book_details":book_details})

def book_page(request):
    
    return render(request,"bookpage.html")

def Add_books(request):
    
    if request.POST:
        data = request.POST
        Book_Title = data.get("Book-Title")
        Book_Img = request.FILES.get("Book-Img")
        Book_Auth = data.get("Auth-Name")
        Book_Rating = data.get("Book-Rating")
        Book_PDF = request.FILES.get("Book-PDF-File")
       
       
        book.objects.create(Title=Book_Title,Book_image=Book_Img,Auth=Book_Auth,Rating=Book_Rating,Book=Book_PDF)

        

    return render(request,"Addbook.html")