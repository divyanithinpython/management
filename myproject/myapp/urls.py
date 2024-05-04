from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from.import views as v

urlpatterns = [
    path('',v.Index,name="Index"),
    #path('packge_details/',v.packagedetail,name="packagedetail"),
    path('addpackage/',v.add_package,name="add_package"),
    path('register/',v.useregister,name="register"),
    path('login/',v.user_login,name="login"),
    path('vendor_register/',v.vendorregister,name="vendorregister"),
    path('vendor_login/',v.vendorlogin,name="vendorlogin"),
    path('home/',v.home,name="home"),
    path('book/',v.book,name="book"),
    path('payment/',v.payment,name="payment"),
    path('confirmation/',v.confirmlist,name="confirmlist"),
    path('packge_details/',v.packagedetail,name="packagedetail"),

    path('tourpackage/',v.tour,name="tour"),
    path('package_location_detail/<str:location>packge_details/',v.package_location_detail,name='package_location_detail')
    
    
    
    
    
    
    
    
    
]