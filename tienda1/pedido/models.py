from django.db import models
from django.contrib.auth.models import User
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel

# Create your models here.

#class Categoria(models.Model):
#    nombre=models.CharField(max_length=30)

#    class Meta:
#        verbose_name='categoria'
#        verbose_name_plural='categorias'
    
#    def __str__(self):
#        return self.nombre
class Category(MPTTModel):
    name = models.CharField(max_length=50, unique=True)
    parent = TreeForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')

    class MPTTMeta:
        order_insertion_by = ['name']
    def __str__(self):
        return self.name 

    def __str__(self):
        full_path=[self.name]
        k= self.parent

        while k is not None:
            full_path.append(k.name)
            k= k.parent
        return ' / '.join(full_path[::-1])

class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    category=models.ForeignKey(Category, on_delete=models.CASCADE)
    #subcategoria=models.
    descripcion=models.TextField(null=True, blank=True)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    #solo_permuta=models.
    #permuta_vende=models.
    #solo_vende==models.  
    imagen=models.ImageField(upload_to="home", null=True, blank=True)
    autor=models.ForeignKey(User, on_delete=models.CASCADE) #SI UN USUARIO SE BORRA, SE BORRAN TODOS SUS POST
    created=models.DateField(auto_now_add=True)
    updated=models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.nombre 

#, null=True, blank=True)
class PostImage(models.Model):
    post = models.ForeignKey(Articulos, default=None, on_delete=models.CASCADE)
    images = models.FileField(upload_to = 'images/')