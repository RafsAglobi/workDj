from django.shortcuts import render
from django.views import View


# Классовое представление
class ClassBasedView(View):
    def get(self, request):
        return render(request, 'second_task/class_view.html')


# Функциональное представление
def FunctionBasedView(request):
    return render(request, 'second_task/function_view.html')
