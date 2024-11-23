from django.urls import path
from .views import ClassBasedView, FunctionBasedView

urlpatterns = [
    path('class-view/', ClassBasedView.as_view(), name='class_view'),
    path('function-view/', FunctionBasedView, name='function_view'),
]
