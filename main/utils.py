
from pathlib import Path
import os
import re
import requests as rq
from decouple import config




def date_spliter(date1,date2):
    a1=[]
    b1=''
    for i in date1:
        if i==":":
            a1.append(b1)
            b1 =''
        elif i==" ":
            a1.append(b1)
            b1 =''
        elif i=="-":
            a1.append(b1)
            b1 =''
        else:
            b1 += i
    a1.append(b1)
    a2=[]
    b2=''
    for i in date2:
        if i==":":
            a2.append(b2)
            b2 =''
        elif i==" ":
            a2.append(b2)
            b2 =''
        elif i=="-":
            a2.append(b2)
            b2 =''
        else:
            b2 += i
    a2.append(b2)
    if abs(int(a1[0]) -int(a2[0])) == 0 and abs(int(a1[1]) -int(a2[1])) == 0 and abs(int(a1[2]) -int(a2[2])) == 0 and abs(int(a1[3]) -int(a2[3])) == 0 and abs(int(a1[4]) -int(a2[4])) <= 5:
        return True
    else:
        return False

def date_spliter_cron(date1,date2):
    a1=[]
    b1=''
    for i in date1:
        if i==":":
            a1.append(b1)
            b1 =''
        elif i==" ":
            a1.append(b1)
            b1 =''
        elif i=="-":
            a1.append(b1)
            b1 =''
        else:
            b1 += i
    a1.append(b1)
    a2=[]
    b2=''
    for i in date2:
        if i==":":
            a2.append(b2)
            b2 =''
        elif i==" ":
            a2.append(b2)
            b2 =''
        elif i=="-":
            a2.append(b2)
            b2 =''
        else:
            b2 += i
    a2.append(b2)
    if abs(int(a1[0]) -int(a2[0])) == 0 and abs(int(a1[1]) -int(a2[1])) == 0 and abs(int(a1[2]) -int(a2[2])) == 0 and abs(int(a1[3]) -int(a2[3])) == 0 and abs(int(a1[4]) -int(a2[4])) <= 5:
        return True
    else:
        return False






def split_filter_text(text):
    text = text.lower()
    new_text = re.split(',',text)
    string_list = []
    number_list = []
    for new in new_text:
        try:
            a =int(new)
            number_list.append(new)
        except:
            string_list.append(new)
    return {'number_list':number_list,'text_list':string_list}



def send_message(messages):
    all_aproved =True
    for message in messages:
        data_object = {
            "id": message.customer.id,
            "phone": message.customer.phone_number,
            "text": message.mail.text_approval
        }
        token =config("TOKEN")
        headers={
            'accept': 'application/json',
            'Authorization': f'Bearer {token}',
            'Content-Type': 'application/json'
        }
        api_link = "https://probe.fbrq.cloud/v1/send/{a}".format(a=message.id)
        output = rq.post(api_link, headers=headers,json=data_object)

        if output.status_code == 200:
            message.status ='message_sent'
            message.save()
        else:
            all_aproved=False

    return all_aproved
   
