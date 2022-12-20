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
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)