from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def login_page(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user:
            login(request, user)   # SESSION CREATED
            return redirect("profile")

    return render(request, "login.html")


class ProfileAPI(APIView):
    def get(self, request):
        return Response({
            "username": request.user.username,
            "auth": "SESSION AUTH"
        })
