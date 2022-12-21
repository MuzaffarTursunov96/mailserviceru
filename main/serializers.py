from rest_framework import serializers,fields
from .models import Mails,Messages
from datetime import datetime
from django.db.models import Count
from accounts.models import Customer
import string
from .utils import split_filter_text


class MailSerializer(serializers.ModelSerializer):
    start_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    end_date = serializers.DateTimeField(format="%Y-%m-%d %H:%M")
    info =serializers.SerializerMethodField(method_name='get_info')

    class Meta:
        model = Mails
        fields = ['start_date', 'text_approval', 'fil_code_teg', 'end_date','info']
        depth = 1

    def get_info(self,obj):
        statistics = Messages.objects.filter(mail=obj).values('status','created_date_to_send').annotate(status_count=Count('status')).annotate(customer_count=Count('customer'))

        return statistics


    def validate(self, data):

        if 'start_date' in data.keys() and 'end_date' in data.keys():
            if data['start_date'] > data['end_date'] :
                raise serializers.ValidationError({"end_date": "finish must occur after start"})

        if 'end_date' in data.keys():
            d1 =data['end_date'].strftime("%Y-%m-%d %H:%M")
            d2 =datetime.now().strftime("%Y-%m-%d %H:%M")
            if d1 <= d2:
                raise serializers.ValidationError("end_date can't be little now!")



        
        if 'fil_code_teg' in data.keys():

            text_number =split_filter_text(data['fil_code_teg'])

            if len(text_number['number_list']) < 1:
                raise serializers.ValidationError(" Phone code can't be null, you must enter. For example fil_code_teg entering like this: '78941,text1,23365,78894,text2' ")
            
            if len(text_number['text_list']) < 1:
                raise serializers.ValidationError(" Tag can't be null, you must enter. For example fil_code_teg entering like this: 'text1,78941,334444,text2,78894' ")

            

        return data

   

 

class MessageSerializer(serializers.ModelSerializer):
    created_date_to_send = serializers.DateTimeField(format="%Y-%m-%d %H:%M")

    class Meta:
        model = Messages
        fields = ['created_date_to_send', 'status', 'mail', 'customer']

    
    def validate(self, data):
        if data['status'] not in ['processing','message_sent','to_be_sent']:
            raise serializers.ValidationError({"status": "status must select from this list ['processing','message_sent','to_be_sent'] "})


        return data


      
    
   
      