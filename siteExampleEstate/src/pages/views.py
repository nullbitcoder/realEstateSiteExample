from django.shortcuts import render

# Create your views here.


def index_view(request, *args, **kwargs):
	return render(request,"index.htm", {})  
        
def contact_view(request, *args, **kwargs):
	return render(request,"contact.htm", {})  

def about_view(request, *args, **kwargs):
	return render(request,"about.htm", {})  

def blog_view(request, *args, **kwargs):
	return render(request,"blog.htm", {})  

def elements_view(request, *args, **kwargs):
	return render(request,"elements.htm", {})  

def facilities_view(request, *args, **kwargs):
	return render(request,"facilities.htm", {})  

def main_view(request, *args, **kwargs):
	return render(request,"main.htm", {})  

def property_view(request, *args, **kwargs):
	return render(request,"property.htm", {})  

def sing_blog_view(request, *args, **kwargs):
	return render(request,"sing-blog.htm", {})  
