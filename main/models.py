from django.db import models
from accounts.models import Customer
# Create your models here.



class Messages(models.Model):
  created_date_to_send =models.DateTimeField()
  status = models.CharField(max_length=50)
  mail = models.ForeignKey('Mails',on_delete=models.CASCADE,related_name='messages_m')
  customer =models.ForeignKey(Customer,on_delete=models.CASCADE,related_name='messages_c')
  
  def __str__(self):
    return self.mail.text_approval


class Mails(models.Model):
  start_date = models.DateTimeField()
  text_approval = models.TextField(default='')
  fil_code_teg =models.CharField(max_length=255)
  end_date = models.DateTimeField()
  used =models.BooleanField(default=False)
  
  def __str__(self):
    return self.fil_code_teg
  
  def save(self, *args, **kwargs):
        self.fil_code_teg=self.fil_code_teg.lower()
        super(Mails, self).save(*args, **kwargs)

