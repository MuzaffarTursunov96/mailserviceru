from django.shortcuts import render,redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from .models import Customer,User,UserProfile
from .serializers import CustomerSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import get_object_or_404
from .forms import ProfileForm,UserForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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
    if UserProfile.objects.filter(user=user).exists():
        profile =UserProfile.objects.get(user=user)
    else:
        profile =UserProfile(user=user)
        profile.save()

    u_form =UserForm(instance=user)
    form =ProfileForm(instance =profile) 

    if request.method =="POST":
        formupdate =ProfileForm(request.POST,request.FILES,instance=profile)
        uform = UserForm(request.POST,instance=user)
        messages.error(request,"validd start")
        # messages.error(request,uform)
        if u_form.is_valid():
            messages.error(request,"validd user")
            user =uform.save(commit=True)
            user.save()
        else:
            messages.error(request,uform.errors)  

        if formupdate.is_valid():
            messages.error(request,"validd profile")
            userprofile=formupdate.save(commit=True)
            userprofile.user=user
            userprofile.save()
            messages.info(request,'Updated successfully!')
            return redirect('my_profile',pk) 
        else:
            messages.error(request,formupdate.errors)  
    
    context={
        # 'profile':profile,
        'form':form,
        'uform':u_form
    }
    return render(request,'accounts/my_profile.html',context)
