from .models import Mails
from datetime import datetime
from .utils import send_message,date_spliter
from .models import Messages


def send_message_cron():
  mails = Mails.objects.filter(start_date__lte=datetime.now(),end_date__gte=datetime.now(),used=False).select_related('mail').select_related('customer')
  for mail in mails:
    messages = Messages.objects.filter(mail = mail)
    if send_message(messages):
      mail.used =True
      mail.save()

    now =datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    t2=mail.end_date.strftime("%Y-%m-%d %H:%M:%S")
    if date_spliter(now,t2):
      mail.used =True
      mail.save()

def send_messageto_mail():
  pass

