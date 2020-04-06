from django.conf.urls import url

from toolkit.views import TestView, user

urlpatterns = [
    url(r'test', TestView.as_view()),
    url(r'user/login', user.obtain_auth_token),
]
