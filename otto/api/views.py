from pdb import post_mortem
from tokenize import Token
from urllib import request, response
from rest_framework.response import Response
from webbrowser import get
from django.shortcuts import render
from .serializers import UserRegister
from rest_framework.views import APIView
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse,HttpResponseRedirect

# Create your views here.
class register (APIView):
    model=post_mortem
    def post (self,request,fromat=None):
        serializer=UserRegister(data=request.data)
        data={}
        if serializer.is_valid():
            account=serializer.save()
            data['response']='registered'
            data['username']=account.username
            data['email']=account.email
            token=Token.objects.get_or_create(user=account).key
            data['token']=token.key
        else:
            data=serializer.errors
        return Response(data)
class welcome(APIView):
    permission_classes=((IsAuthenticated,))

    def get(self,request):
        content={'user':str(request.user),'userid':str(request.user.id)}
        return Response(content)        
def list(request):
    return render(request, 'welcome.html')
def list2(request):
    return render(request, 'list.html')    
class login(APIView):
    def login(request):
     if request.method == 'POST':    
        return render(request, 'login.html')







