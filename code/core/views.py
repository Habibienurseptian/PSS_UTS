from django.shortcuts import render, HttpResponse
from django.http.response import JsonResponse

from core.models import Item, Supplier, Categories, User

# Create your views here.
def index(request):
    return HttpResponse ("<h1>Selamat Datang di Isekai</h1>")

def testing(request):
    admin = User.objects.create_user(
        username="admin_7", email="admin7@gmail.com",
        password="admin7"
    )
    category = Categories.objects.create(
        name="Printer",
        description="Alat cetak",
        created_by=admin
    )
    supllier = Supplier.objects.create(
        name="Johan",
        contact_info="Johan.jr",
        created_by=admin
    )

    Item.objects.create(
        name="Printer Canon",
        description="Alat cetak",
        price="7500000",
        quantity="4",
        category_id=category,
        supplier_id=supllier,
        created_by=admin
    )

    return HttpResponse("Welcome")

def allItem(request):
    allItem = Item.objects.all().select_related('category_id').select_related('supplier_id').select_related('created_by')
    result = []
    for item in allItem:
        record = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'quantity': item.quantity,
            'category': {
                'id': item.category_id.id,
                'name': item.category_id.name,
                'description': item.category_id.description,
                'created': {
                    'id': item.created_by.id,
                    'username': item.created_by.username,
                    'email': item.created_by.email,
                    'password': item.created_by.password
                }
            },
            'supplier': {
                'id': item.supplier_id.id,
                'name': item.supplier_id.contact_info,
                'created':{
                    'id': item.created_by.id,
                    'username': item.created_by.username,
                    'email': item.created_by.email,
                    'password': item.created_by.password
                }
            },
            'created':{
                'id': item.created_by.id,
                'username': item.created_by.username,
                'email': item.created_by.email,
                'password': item.created_by.password
            }
        }
        result.append(record)
    return JsonResponse(result, safe=False)

from django.db.models import Sum, Avg, F, Count

def stock_barang(request):
    item = Item.objects.all()
    stock = item.aggregate(total_stock=Sum('quantity'),
                           nilai_stock=Sum(F('quantity')*F('price')),
                           rata_harga=Avg('price'))

    data = {
        'total_stock': stock['total_stock'],
        'nilai_stock': stock['nilai_stock'],
        'rata_rata_harga': stock['rata_harga']
    }

    return JsonResponse(data)

def stock_bawah(request, threshold=5):
    stock_barang_sedikit = Item.objects.filter(quantity__lt=threshold).values('id', 'name', 'quantity', 'price')
    return JsonResponse(list(stock_barang_sedikit), safe=False)

def kategori_barang(request, category_id):
    items = Item.objects.filter(category_id=category_id).select_related('category_id')
    result = []
    for item in items:
        record = {
            'id': item.id,
            'name': item.name,
            'description': item.description,
            'price': item.price,
            'quantity': item.quantity,
            'category': {
                'id': item.category_id.id,
                'name': item.category_id.name,
                'description': item.category_id.description
            }
        }
        result.append(record)
        return JsonResponse(result, safe=False)