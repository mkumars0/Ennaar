from ennarroot import views
from django.urls import path,include

app_name='ennarroot'
urlpatterns = [
    path('',views.index ,name='home'),
    path('Admin/',views.admin,name='Admin'),
    path('admin_login/',views.adminLogin,name='admin_login'),
    path('admin_desk/',views.adminDesk,name='admin_desk'),
    path('logout/',views.logout,name='logout'),
    path('upload_product/',views.uploadForm,name='productupload'),
    path('upload/',views.productUpload,name='upload')


]