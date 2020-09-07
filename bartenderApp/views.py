from django.shortcuts import redirect, render


# redirects requests from root directory to main directory
def home(request):
    return redirect("/drinks/")
