

# Create your views here.
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class LoginAPI(ObtainAuthToken):
    pass   # returns token


class ProfileAPI(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "user": request.user.username,
            "auth": "TOKEN AUTH"
        })
