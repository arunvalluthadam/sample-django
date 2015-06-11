from django.shortcuts import render

# Create your views here.
def home(request):
	return render(request, "index.html")

def quick_text(request):
	return render(request, "quick_text.html")

def archives(request):
	return render(request, "archives.html")

def category(request):
	return render(request, "category.html")

def signup(request):
	return render(request, "sign_up.html")

def signin(request):
	return render(request, "sign_in.html")

def about(request):
	return render(request, "about.html")