from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns =[
    path('',views.index,name='index'),
    path('login/',views.login_view,name='login'),
    path('logout/',views.logout_view,name='logout'),

    path('forgot_password/',views.forgot_password,name='forgot_password'),
    path('reset_password_validate/<uidb64>/<token>/',views.reset_password_validate,name='reset_password_validate'),
    path('reset_password/',views.reset_password,name='reset_password'),
    path('singup/',views.singup,name='singup'),





    # templates
    path('elements/',views.elements,name='elements'),
    path('widgets/',views.widgets,name='widgets'),
    path('forms/',views.forms,name='forms'),
    path('tables/',views.tables,name='tables'),
    path('charts/',views.charts,name='charts'),
    path('not_found/',views.not_found,name='not_found'),
    path('button/',views.button,name='button'),
    path('blank/',views.blank,name='blank'),
    path('typography/',views.typography,name='typography'),




    # add elements
    # mail
    path('add_mail/',views.add_mail,name='add_mail'),
    path('mail-list/',views.mail_list,name='mail_list'),
    path('mail_detail/<int:pk>',views.mail_detail,name='mail_deatil'),

    # message
    path('add_message/',views.add_message,name='add_message'),
    path('message-list/',views.message_list,name='message_list'),
    path('message-detail/<int:pk>',views.message_detail,name='message_detail'),

    # customer
    path('add_customer/',views.add_customer,name='add_customer'),
    path('customer-list/',views.customer_list,name='customer_list'),
    path('customer-detail/<int:pk>',views.customer_detail,name='customer_detail'),

]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)