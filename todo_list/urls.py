from django.urls import path
from .views import *

urlpatterns = [
	path('',todolistview.as_view()),
	path('tododetails/<str:pk>', tododetailview.as_view())
]