from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Person
from .models import Product
from .models import Company

# получение данных из БД и загрузка index.html
def index(request):
 people = Person.objects.all()
 return render(request, "index.html", {"people": people})

# сохранение данных в БД
def create(request):
 if request.method == "POST":
    klient = Person()
    klient.name = request.POST.get("name")
    klient.age = request.POST.get("age")
    klient.save()
 return HttpResponseRedirect("/")

# изменение данных в БД
def edit(request, id):
    try:
        person = Person.objects.get(id=id)
        if request.method == "POST":
            person.name = request.POST.get("name")
            person.age = request.POST.get("age")
            person.save()
            return HttpResponseRedirect("/")
        else:
            return render(request, "edit.html", {"person": person})
    except Person.DoesNotExist:
        return HttpResponseNotFound("<h2>Клиент не найден</h2>")
# удаление данных из БД
def delete(request, id):
 try:
    person = Person.objects.get(id=id)
    person.delete()
    return HttpResponseRedirect("/")
 except Person.DoesNotExist:
    return HttpResponseNotFound("<h2>Клиент не найден</h2>")

firma = Company.objects.create(name=" Электрон")
firma.product_set.create(name="Samsung S20", price=42000)
ipad = Product(name="iPad", price=34200)
firma.product_set.add(ipad, bulk=False)
