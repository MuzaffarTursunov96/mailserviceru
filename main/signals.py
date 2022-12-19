
from django.db.models.signals import post_save
from django.dispatch import receiver
from main.models import Mails
from datetime import datetime
from accounts.models import Customer
from main.models import Messages
from .utils import date_spliter,split_filter_text,send_message
from django.db.models import Q

@receiver(post_save,sender=Mails)
def mail_is_created(sender, instance, created, **kwargs):
    if created:        
        now =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        t1=instance.start_date.strftime("%Y-%m-%d %H:%M:%S")
        t2=instance.end_date.strftime("%Y-%m-%d %H:%M:%S")
        filter_text =split_filter_text(instance.fil_code_teg)

        customers = Customer.objects.filter( Q(phone_code__in=filter_text['number_list']) & Q(teg__in=filter_text['text_list']))

        if date_spliter(t2,now):
            for customer in customers:
                message = Messages()
                message.created_date_to_send =instance.end_date
                message.status ='proccessing'
                message.mail = instance
                message.customer =customer
                message.save()
            customer_ids =[]
            for customer in customers:
                customer_ids.append(customer.id)

            messages = Messages.objects.filter(mail = instance,customer__id__in= customer_ids, status ='proccessing').select_related('mail').select_related('customer')
            if send_message(messages):
                instance.used =True
                instance.save()

        elif t1 <= now and  t2 >= now :
            for customer in customers:
                message = Messages()
                message.created_date_to_send =instance.end_date
                message.status ='proccessing'
                message.mail = instance
                message.customer =customer
                message.save()
        elif t1 > now:
            for customer in customers:
                message = Messages()
                message.created_date_to_send =instance.end_date
                message.status ='to_be_sent'
                message.mail =instance
                message.customer =customer
                message.save()
        

                
            