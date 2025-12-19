from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
# Create your views here.

def login_cookie(request):
    if request.method == "POST":
        username = request.POST.get("username")

        response = redirect("home")
        response.set_cookie("user", username)   
        return response

    return render(request, "login.html")


def home(request):
    user = request.COOKIES.get("user")

    if not user:
        return HttpResponse("Not logged in")

    return HttpResponse(f"Hello {user} (COOKIE AUTH)")