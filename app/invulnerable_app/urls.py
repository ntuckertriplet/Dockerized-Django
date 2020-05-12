from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.urls import re_path

from auto_store import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('products/', views.products, name='products'),
    path('services/', views.services, name='services'),
    path('employees/', views.employees, name='employees'),
    path('customerMemo/', views.customer_memo, name='customer_memo'),
    path('employeeHoliday/', views.employee_holiday, name='employee_holiday'),
    path('shutdown/', views.shutdown, name='shutdown'),
    path('w2/', views.w2, name='w2'),
    path('ceoMessage/', views.ceo_message, name='ceomessage'),
    path('covid19/', views.covid19, name='covid19'),
    path('testing/', views.testing, name='testing'),
    path('bulletin/', views.bulletin, name='bulletin'),
    path('addUser/', views.add_user, name='add_user'),
    path("admin/", admin.site.urls),
]

if bool(settings.DEBUG):
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
