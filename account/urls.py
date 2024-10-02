from django.urls import path
from .views import WebTokenAuth, Registration, Update_user, View_data, Delete_account, BeforeRegistration


urlpatterns = [
    path('login/', WebTokenAuth.as_view()),
    path('before_registration/', BeforeRegistration.as_view()),
    path('registration/', Registration.as_view()),
    path('update/', Update_user.as_view()),
    path('take_to/', View_data.as_view()),
    path('delete_acc/', Delete_account.as_view()),


]
