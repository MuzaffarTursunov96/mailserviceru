from rest_framework import serializers
from accounts.models import Customer
import pytz
timezones = pytz.all_timezones



class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = Customer
        fields = ['id','phone_number', 'phone_code', 'teg', 'timezone']

    def validate_phone_number(self,value):
        for val in value:
            if val not in "0123456789":
                raise serializers.ValidationError('You must add phone number like this 74951234567 ')

        if value[0]!='7':
            raise serializers.ValidationError('First letter should be "7"')
        
        return value
      
    def validate_phone_code(self,value):
        for val in value:
            if val not in "+1234567890()":
                raise serializers.ValidationError('You must add phone number like this +7 (495) or 39022')
        return value

    def validate_timezone(self,value):
        if value not in timezones:
            raise serializers.ValidationError(f'You must select from this links "{timezones}"')
        return value

      