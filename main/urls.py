from django.urls import path
from main import views

urlpatterns =[
  path('mail-create/',views.CreateMail.as_view(),name='create-mail'),
  path('mail-statistics/',views.StatisticsMail,name='statistic-mail'),
  path('mail-delete/<pk>',views.DeleteMail.as_view(),name='delete-mail'),
  path('mail-update/<pk>',views.UpdateMail.as_view(),name='update-mail'),
  path('mail-detail/<pk>',views.DetailMail.as_view(),name='detail-mail'),
  path('mail-active/',views.MailIsActive,name='active-mail'),

  # path('mail-detail-single/<pk>',views.DetailMailSingle,name='detail-mail-single'),

  path('test/',views.TestMail,name='test'),
  


  path('message-list/',views.MessageList.as_view(),name='message-list'),
  path('message-create/',views.MessageCreate.as_view(),name='message-create'),
  path('message-delete/<pk>',views.DeleteMessage.as_view(),name='delete-message'),
  path('message-update/<pk>',views.UpdateMessage.as_view(),name='update-message'),
  path('message-detail/<pk>',views.DetailMessage.as_view(),name='detail-message'),

]