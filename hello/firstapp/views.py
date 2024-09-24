from django.shortcuts import render
from django.http import *



def index(request):
            cat = ["Ноутбуки", "Принтеры", "Сканеры", "Диски", "Шнуры"]
            return render(request, "firstapp/index.html", context={"cat": cat})

        # header = "Персональные данные" # обычная переменная
        # langs = ["Английский", "Немецкий", "Испанский"] # массив
        # user = {"name": "Максим,", "age": 30} # словарь
        # addr = ("Виноградная", 23, 45) # кортеж
        # data = {"header": header, "langs": langs, "user": user, "address": addr}
        # return render(request, "index.html", context=data)




