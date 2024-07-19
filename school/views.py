from rest_framework import viewsets
from .models import User, Subject, Mark
from .serializers import UserSerializer, SubjectSerializer, MarkSerializer,RegisterSerializer,LoginSerializer

from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication


class RegisterAPI(APIView):
    def post(self,request):
        data = request.data 
        serializer = RegisterSerializer(data=data)

        if not serializer.is_valid():
            return Response({'message' : serializer.errors}, status = status.HTTP_404_NOT_FOUND )
        
        serializer.save()
        return Response({'message' : "User Created" },status = status.HTTP_201_CREATED)
    

class LoginAPI(APIView):

    def post(self,request):
        data = request.data 
        serializer = LoginSerializer(data = data)
        if not serializer.is_valid():
            return Response({'message' : serializer.errors}, status = status.HTTP_404_NOT_FOUND )
        
        user = authenticate(username = serializer.data['username'],password=serializer.data['password'])
      

        if not user:
            return Response({"message":"Invalid"}, status = status.HTTP_404_NOT_FOUND)
        
        token,_ = Token.objects.get_or_create(user=user)
        return Response({"message" : "Login Successfull","token":str(token) },status = status.HTTP_200_OK)



class UserViewSet(viewsets.ModelViewSet):
    #permission_classes=[IsAuthenticated]
    authentication_classes = [TokenAuthentication]
    queryset = User.objects.all()
    serializer_class = UserSerializer

class SubjectViewSet(viewsets.ModelViewSet):
    queryset = Subject.objects.all()
    serializer_class = SubjectSerializer

class MarkViewSet(viewsets.ModelViewSet):
    queryset = Mark.objects.all()
    serializer_class = MarkSerializer

# Create your views here.
