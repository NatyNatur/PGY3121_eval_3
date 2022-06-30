from django.shortcuts import render
from vacunasMaule.models import Articulo
from django.http import HttpResponse

def ingresar_productos(request):
    return render(request,"ingresar_productos.html")

def index(request):
    return render(request,"index.html")

def busqueda_productos(request):
    return render(request,"busqueda_productos.html") 

def listar_todo(request):
    return render(request,"listar_todo.html")


def eliminar_producto(request):
    return render(request,"eliminar_producto.html")

def modificar_articulo(request):
    return render(request,"modificar_articulo.html")

# Create your views here.

def listar_todo_articulos(request):
    datos = Articulo.objects.all()  
    return render(request,"listar_todo.html",{'articulos':datos})
    
def ingreso_producto(request):
    nombre=request.GET["txt_nombre"]
    categoria=request.GET["txt_categoria"]
    precio=request.GET["txt_precio"]
    if len(nombre)>0 and len(categoria)>0 and len(precio)>0:
        pro=Articulo(nombre=nombre,categoria=categoria,precio=precio)  
        pro.save()
        mensaje="Articulo ingresado..."
    else:
        mensaje="Articulo No ingresado o faltan datos..."
    return HttpResponse(mensaje)
    
def modificar(request):
    if request.GET["txt_id"]:
        id_recibido = request.GET["txt_id"]
        precio_recibido = request.GET["txt_precio"]
        producto = Articulo.objects.filter(id=id_recibido)
        if producto:
            pro=Articulo.objects.get(id=id_recibido)
            pro.precio = precio_recibido
            pro.save()
            mensaje = "Precio correctamente modificado"           
        else:
            mensaje = "No existe producto para modificar"           
    else:
        mensaje = "Debe ingresar un id para modificar"
    return HttpResponse(mensaje)



def buscar(request):
    if request.GET["txt_producto"]:
        producto = request.GET["txt_producto"]
        articulos = Articulo.objects.filter(nombre__icontains=producto)
        return render(request,"listar.html",{"articulos":articulos,"query":producto})
    else:
        mensaje = "Debe ingresar un nombre de producto"
        return HttpResponse(mensaje)


def eliminacion_producto(request):
    if request.GET["txt_id"]:
        id_recibido = request.GET["txt_id"]
        producto = Articulo.objects.filter(id=id_recibido)
        if producto:
            pro=Articulo.objects.get(id=id_recibido)
            pro.delete()
            mensaje = "Producto Eliminado..."
        else:
            mensaje = "Producto No eliminado...No existe producto con ese id"
    else:
        mensaje = "Debe ingresar un id para eliminación..."
    return HttpResponse(mensaje)


