from django.urls import path
from .views import WebTokenAuth, Registration, Update_user


urlpatterns = [
    path('login/', WebTokenAuth.as_view()),
    path('registration/', Registration.as_view()),
    path('update/', Update_user.as_view()),

]
