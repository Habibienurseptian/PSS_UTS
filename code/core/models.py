from django.db import models
from django.contrib.auth.models import User

class Categories(models.Model):
    name = models.CharField('Katagori', max_length=100)
    description = models.TextField('Deskripsi', null=True, blank=True)
    created_by = models.ForeignKey(User, verbose_name="Admin", on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Katagori"
        verbose_name_plural = "Katagori"
        
    def __str__(self) -> str:
        return self.name
    
class Supplier(models.Model):
    name = models.CharField('Nama Pengirim', max_length=100)
    contact_info = models.CharField('Kontak Informasi', max_length=100)
    created_by = models.ForeignKey(User, on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Pengirim"
        verbose_name_plural = "Pengirim"

    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    name = models.CharField('Nama Barang', max_length=100)
    description = models.TextField('Deskripsi', null=True, blank=True)
    price = models.DecimalField('Harga', max_digits=10, decimal_places=2)
    quantity = models.IntegerField('Jumlah Barang')
    category_id = models.ForeignKey(Categories, verbose_name="Katagori", on_delete=models.RESTRICT)
    supplier_id = models.ForeignKey(Supplier, verbose_name="Pengirim", on_delete=models.RESTRICT)
    created_by = models.ForeignKey(User, verbose_name="Admin", on_delete=models.RESTRICT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Barang"
        verbose_name_plural = "Barang"

    def __str__(self) -> str:
        return self.name