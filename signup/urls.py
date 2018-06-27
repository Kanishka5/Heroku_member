from django.conf.urls import url,include
from . import views
from .views import login_view,register_view


urlpatterns=[
    url(r'^$',views.register_view,name='signup'),
    url(r'^$',include('homepage.urls'),name='homepage'),
]
