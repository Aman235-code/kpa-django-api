from django.urls import path
from . import views
from django.http import HttpResponseNotAllowed

def wheel_specifications_dispatcher(request):
    if request.method == 'POST':
        return views.create_wheel_spec(request)
    elif request.method == 'GET':
        return views.get_wheel_specification(request)
    return HttpResponseNotAllowed(['GET', 'POST'])

urlpatterns = [
    path('createBasicInfo', views.create_basic_info),
    path('getBasicInfoByPhoneNumber/<str:phone>', views.get_basic_info_by_phone),
    path('forms/wheel-specifications', wheel_specifications_dispatcher),
    path('forms/bogie-checksheet', views.create_bogie_checksheet),
]
