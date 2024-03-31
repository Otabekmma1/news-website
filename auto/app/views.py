from django.shortcuts import render, redirect
from .models import Car, Brand, Colour
from django.contrib import messages
from django.http import HttpResponse

def home(request):
    return HttpResponse("Salom")

def car(request):
    cars = Car.objects.all()
    brands = Brand.objects.all()
    colors = Colour.objects.all()
    selected_color_id = request.GET.get('color')
    if selected_color_id:
        cars = cars.filter(colour_id=selected_color_id)
    return render(request, 'index.html', {'cars': cars, 'brands': brands, 'colors': colors})

def brand_car(request, brand_id):
    cars = Car.objects.filter(brand_id=brand_id)
    brands = Brand.objects.all()
    ctx = {
        'cars': cars,
        'brands': brands
    }
    return render(request, 'index.html', ctx)

def addcar(request):
    brands = Brand.objects.all()
    cars = Car.objects.all()
    colours = Colour.objects.all()

    if request.method=="POST":
        model = request.POST.get('model')
        colour = request.POST.get('colour')
        brand = request.POST.get('brand')
        price = request.POST.get('price')

        brand_instance = Brand.objects.get(id=brand)
        colour_instance = Colour.objects.get(name=colour)
        query=Car(model=model, colour=colour_instance, brand=brand_instance, price=price)
        query.save()
        messages.info(request,"Mashina muvaffaqiyatli o'zgartirildi")
        return redirect("/add")
    ctx = {
        'brands': brands,
        'cars': cars,
        'colours': colours
    }
    return render(request,"blog/index.html", context=ctx)


def updateCar(request,id):
    brands = Brand.objects.all()
    if request.method=="POST":
        model = request.POST.get('model')
        colour = request.POST.get('colour')
        brand = request.POST.get('brand')
        price = request.POST.get('price')

        brand_instance = Brand.objects.get(name=brand)
        colour_instance = Colour.objects.get(name=colour)

        edit=Car.objects.get(id=id)
        edit.model=model
        edit.colour=colour_instance
        edit.brand = brand_instance
        edit.price=price
        edit.save()
        messages.warning(request,"Mashina muvaffaqiyatli o'zgartirildi")
        return redirect("/add")
    car =Car.objects.get(id=id)
    context={
        'car': car,
        'brands':brands
    }
    return render(request,"blog/edit.html",context)


def deleteCar(request,id):
    car =Car.objects.get(id=id)
    car.delete()
    messages.error(request,"Mashina o'chirildi")
    return redirect("/add")