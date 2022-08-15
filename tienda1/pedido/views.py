from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from pedido.models import Articulos, Category

from pedido.forms import FormularioArticulo, CustomUserForm

from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import login, authenticate

from django.contrib.auth.models import User


# views

def home(request):
    #template_name="pedido/home.html"

    #context={}
    #context['articulos']=Articulos.objects.all()[3:] 
    articulos=Articulos.objects.all()[1:]
    categorias=Category.objects.all()
    #return render(request, template_name, context)
    return render(request, "pedido/home.html", {"articulos": articulos, "categorias": categorias})

def help(request):
    
    return render(request, "pedido/help.html")
@login_required
def postView(request):

    data= {
        'form':FormularioArticulo()
    }

    if request.method == 'POST':
        formulario = FormularioArticulo(request.POST, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Producto Publicado exitosamente"

    return render(request, 'pedido/post.html', data)

def detalle(request, id): 

    articulo = Articulos.objects.get(id=id)
    data= {
        'form':FormularioArticulo(instance=articulo)
    }
    if request.method == 'POST':
        formulario = FormularioArticulo(data=request.POST, instance=articulo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Datos de producto modificados correctamente"
            data['form'] = FormularioArticulo(instance=Articulos.objects.get(id=id))

    return render(request, 'pedido/detalle.html', data)

def category_products(request, id): 

    articulo = Articulos.objects.filter(category_id=id)
    
    return HttpResponse(articulo)


def modificar_producto(request, id): 

    articulo = Articulos.objects.get(id=id)
    data= {
        'form':FormularioArticulo(instance=articulo)
    }
    if request.method == 'POST':
        formulario = FormularioArticulo(data=request.POST, instance=articulo, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            data['mensaje'] = "Datos de producto modificados correctamente"
            data['form'] = FormularioArticulo(instance=Articulos.objects.get(id=id))

    return render(request, 'pedido/modificar_producto.html', data)

def eliminar_producto(request, id):
    articulo= Articulos.objects.get(id=id)
    articulo.delete()

    return redirect(to="my_account")

def registro_usuario(request):
    data = {
        'form':CustomUserForm()
    }

    if request.method == 'POST':
        formulario = CustomUserForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username= formulario.cleaned_data['username']
            password= formulario.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(to="my_account")


    return render(request, 'registration/registrar.html', data)

def my_account(request):
    template_name="pedido/my_account.html"    

    articulos=Articulos.objects.all()
    return render(request, template_name, {'user': request.user,"articulos": articulos})
   

def busqueda_productos(request):

    return render(request, "busqueda_productos.html")

def buscar_todo(request):
    articulo=Articulos.objects.all()

    return render(request, Articulos.objects.all() )



def buscar(request):
    if request.GET["prd"]:

        #mensaje="Producto buscado: %r" %request.GET["prd"]
        producto=request.GET["prd"] #variable del texto ingresado en el buscador

        if len(producto)>30:    #validar si ingresa textos muy largos

            mensaje="Texto ingresado demasiado extenso"
        else:

            producto=Articulos.objects.filter(nombre__icontains=producto)

            return render(request, "resultados_busqueda.html", {"productos":producto, "query":producto})

    else:

        mensaje="no se ah introducido nada"

