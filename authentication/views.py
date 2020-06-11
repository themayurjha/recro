from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout
from django.contrib.auth.models import auth, User
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from authentication.serializer import ExtendedUserSerializer, UserSerializer
from .models import ExtentedUser


# Create your views here.
def user_login(request):
    context = {}
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        try:
            username = User.objects.get(email=email).username
        except Exception as e:
                 return render(request, 'login.html', {'error':'User Does not Exists'})
        
        else:
            user = auth.authenticate(username=username, password=password)
        
            if user:
                login(request, user)
                return redirect('/success/')
            else:
                return render(request, 'login.html', {'error':'Wrong Password'})
    else:
        return render(request, 'login.html', context)


@login_required(login_url='/login/')
def user_success(request):
    return render(request, 'success.html', {'user':request.user})


class ShowAllUser(APIView):
    def get(self, request):
        user= ExtentedUser.objects.all()
        serializer = ExtendedUserSerializer(user, many=True)
        return Response(serializer.data)

def get_user_id(request):
    pass

def reset_password(request):
    if request.method == 'PUT':
        username = request.PUT['username']
        password = request.PUT['password']
        try:
            user = User.objects.get(username=username)
        except Exception:
            return render(request, 'updatepassword.html', {'msg' : 'User doesnot exists'})
        else:
            try:
                user.password = password
                user.save()
            except Exception:
                return render(request, 'updatepassword.html', {'msg' : 'Try Again. Something went wrong'})
            else:
                return render(request, 'updatepassword.html', {'msg' : 'passwordupdated'})

    else:
        return render(request, 'updatepassword.html')


class PhoneSearch(APIView):
        def get(self,request):
            return render(request, 'searchphno.html')

        def post(self, request):
            phno = request.POST.get('phno', False)
            user= ExtentedUser.objects.get(phoneno=phno)
            serializer = ExtendedUserSerializer(user)
            return Response(serializer.data)

