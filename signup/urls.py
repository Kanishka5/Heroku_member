from django.conf.urls import url,include
from . import views
from .views import login_view,register_view

app_name='registration'

urlpatterns=[
    url(r'^$',views.register_view,name='register'),
]
