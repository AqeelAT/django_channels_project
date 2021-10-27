from django.urls import path

from hello.api.views import HelloApiView

urlpatterns = [
    path('hello/', HelloApiView.as_view()),
]
