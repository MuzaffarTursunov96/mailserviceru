from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Customer,User,UserProfile
from .serializers import CustomerSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .forms import ProfileForm
from django.contrib.auth.decorators import login_required


class ListCustomers(generics.ListAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer 

class DetailCustomers(generics.RetrieveAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer 
    lookup_url_kwarg='pk'


class CreateCustomers(generics.CreateAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer 

class UpdateCustomers(generics.UpdateAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer 
    lookup_url_kwarg='pk'

class DeleteCustomers(generics.DestroyAPIView):
    queryset = Customer.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = CustomerSerializer 
    lookup_url_kwarg='pk'


@login_required(login_url='login')
def my_profile(request,pk):
    user =get_object_or_404(User,id=pk)
    if request.method =="POST":
        if UserProfile.objects.filter(user=user).exists():
            profile =UserProfile.objects.get(user=user)
            form =ProfileForm(request.POST,request.FILES,instance=profile)
            if form.is_valid():
                form.save()
            else:
                print(form.errors)
        else:
            profile =UserProfile(user=user)
            profile.save()
            form =ProfileForm(instance=profile)
    else:
        if UserProfile.objects.filter(user=user).exists():
            profile =UserProfile.objects.get(user=user)
            form =ProfileForm(instance=profile)
        else:
            form =ProfileForm()

    context={
        # 'profile':profile,
        'form':form
    }
    return render(request,'accounts/my_profile.html',context)