from mini import views
from django.conf.urls import url

urlpatterns = [
    url(r'^$', views.index, name='home'),
    url(r'^birthdays$', views.birthday, name='birthdays'),
]