from django.shortcuts import render
from rest_framework import generics
from rest_framework.response import Response
from .serializers import MailSerializer,MessageSerializer
from .models import Mails,Messages
from rest_framework.decorators import api_view,permission_classes
from accounts.models import Customer
from datetime import datetime
import datetime as ddate
from .utils import date_spliter,split_filter_text
from rest_framework.permissions import IsAuthenticated



class CreateMail(generics.CreateAPIView):
    queryset = Mails.objects.all()
    serializer_class = MailSerializer 
    permission_classes = (IsAuthenticated,)
    

class DeleteMail(generics.DestroyAPIView):
    queryset = Mails.objects.all()
    serializer_class = MailSerializer 
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg='pk'
    

class DetailMail(generics.RetrieveAPIView):
    queryset = Mails.objects.all()
    serializer_class = MailSerializer 
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg='pk'


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def StatisticsMail(request):
    mails =Mails.objects.all()
    
    mailserializer =MailSerializer(mails,many=True)
    
    return Response({'data':mailserializer.data})

class UpdateMail(generics.UpdateAPIView):
    queryset = Mails.objects.all()
    serializer_class = MailSerializer 
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg='pk'


#Mail end---------


class MessageList(generics.ListAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer 
    permission_classes = (IsAuthenticated,)


class MessageCreate(generics.CreateAPIView):
    queryset = Messages.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer 

class DeleteMessage(generics.DestroyAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer 
    permission_classes = (IsAuthenticated,)
    lookup_url_kwarg='pk'

class UpdateMessage(generics.UpdateAPIView):
    queryset = Messages.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = MessageSerializer 
    lookup_url_kwarg='pk'


class DetailMessage(generics.RetrieveAPIView):
    queryset = Messages.objects.all()
    serializer_class = MessageSerializer 
    lookup_url_kwarg='pk'
    permission_classes = (IsAuthenticated,)



    

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def TestMail(request):
    message=Messages.objects.filter(mail__id = 64).select_related('mail').select_related('customer')
    mailserializer = MessageSerializer(message,many=True)
    return Response({'data':mailserializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def MailIsActive(request):
    yesterday = ddate.date.today() - ddate.timedelta(days=1)
    today_start=ddate.date.today() + ddate.timedelta(days=1)
    mails = Mails.objects.filter(start_date__gt=yesterday,end_date__lt=today_start,used=False)
    mailserializer = MailSerializer(mails)
    if mails.count() > 0:
        return Response({'data':mailserializer.data})
    return Response({'data':'No active mails.'})



