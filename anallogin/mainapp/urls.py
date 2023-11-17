from django.urls import path

from .views import EnterPhone, EnterCode


urlpatterns = [
    path('enter-phone/', EnterPhone.as_view(), name='enter_phone'),
    path('enter-code/', EnterCode.as_view(), name='enter_code')
]


app_name = 'mainapp'
