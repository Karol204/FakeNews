
from django.contrib import admin
from django.urls import path
from BazaFakeKont.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', FirstPage.as_view()),
    path('form', FormPage.as_view())
]
