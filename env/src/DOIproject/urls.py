"""DOIproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from invoicemgmt import views
from django.conf import settings
from django.conf.urls.static import static

# from django.conf import settings
# from django.conf.urls.static import static


urlpatterns = [
    path('accounts/', include('registration.backends.default.urls')),
    path('admin/', admin.site.urls),
    path('', views.list_invoice, name='home'),
    path('add_invoice/', views.add_invoice, name='add_invoice'),
    path('list_invoice/', views.list_invoice, name='list_invoice'),
    path('update_invoice/<str:pk>/', views.update_invoice, name="update_invoice"),
    path('delete_invoice/<str:pk>/', views.delete_invoice, name="delete_invoice"),
    path('upload_file',views.upload_file, name="upload_file"),
    path('list_excel_data/', views.list_excel_data,name="list_excel_data"),
    path('excel_data_delete/<str:pk>/',views.delete_excel_data,name="excel_data_delete"),
    path('excel_data_update/<str:pk>/',views.update_excel_data,name="excel_data_update"),
    path('upload_csv_file',views.upload_csv_file, name="upload_csv_file"),
    
 
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)




# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
