from django.conf.urls import url
from django.urls import path
from classifier.views import FileUploadView

urlpatterns = [
    path('<path:src>', FileUploadView.as_view()),
]
