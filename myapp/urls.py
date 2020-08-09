from django.urls import path
from myapp import views
app_name="myapp"

urlpatterns = [
    path('login/',views.login,name="login"),
]
