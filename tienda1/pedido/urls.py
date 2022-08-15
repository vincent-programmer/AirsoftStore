from django.urls import path
from pedido import views
from django.conf import settings
from django.conf.urls.static import static
#from Models.pedido.views import postView
from .views import postView, modificar_producto, eliminar_producto, registro_usuario, detalle, category_products

urlpatterns = [

    path('busqueda_productos/', views.busqueda_productos),
    path('buscar/', views.buscar),
    #path('',views., name=""),
    path('',views.home, name="home"),
    # path('home_login',views.home, name="home_login"),   
   
    path('help',views.help, name="help"),
    
    path('post/', postView, name="post"),
    path('detalle/<id>/', detalle, name="detalle"),    
    path('modificar_producto/<id>/', modificar_producto, name="modificar_producto"),
    path('eliminar_producto/<id>/',eliminar_producto, name="eliminar_producto"),    

    path('my_account',views.my_account, name="my_account"),   

    path('registro/', registro_usuario, name='registro_usuario'),

    path('category/<id>/', views.category_products, name="category_products"),  
]

urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)