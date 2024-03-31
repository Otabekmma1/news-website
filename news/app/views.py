from django.shortcuts import render, redirect
from .models import Post, Category
from django.contrib import messages

def home(request):
    posts = Post.objects.all()[0:4]
    first_post = Post.objects.first()
    categories  = Category.objects.all()
    ctx = {
        'posts': posts,
        'categories': categories,
        'first_post': first_post
    }
    return render(request, 'index.html', ctx)

def category(request, category_id):
    posts = Post.objects.filter(category_id=category_id)
    categories = Category.objects.all()
    ctx = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'index.html', ctx)

def post(request, id):
    posts = Post.objects.filter(id=id)
    categories = Category.objects.all()
    ctx = {
        'posts': posts,
        'categories': categories
    }
    return render(request, 'index.html', ctx)

# -------- Maqola ------
# Maqola yaratish
def post_create(request):
    categories = Category.objects.all()
    posts = Post.objects.all()

    if request.method=="POST":
        title=request.POST.get('title')
        content=request.POST.get('content')
        category=request.POST.get('category')
        image=request.POST.get('image')
        # print(name,email,age,gender)
        category_instance = Category.objects.get(title=category)
        query=Post(title=title,content=content, category=category_instance, image=image)
        query.save()
        messages.info(request,"Maqola muvaffaqiyatli o'zgartirildi")
        return redirect("/insert")
    ctx = {
        'posts': posts,
        'categories': categories
    }
    return render(request,"blog/index.html", context=ctx)


# Maqolani tahrirlash
def updateData(request,id):
    categories = Category.objects.all()
    if request.method=="POST":
        title=request.POST['title']
        content = request.POST.get('content')
        category = request.POST.get('category')
        image = request.POST.get('image')
        category_instance = Category.objects.get(title=category)

        edit=Post.objects.get(id=id)
        edit.title=title
        edit.content=content
        edit.category=category_instance
        edit.image=image
        edit.save()
        messages.warning(request,"Maqola muvaffaqiyatli o'zgartirildi")
        return redirect("/insert")
    post =Post.objects.get(id=id)
    context={
        "post":post,
        'categories': categories
    }
    return render(request,"blog/edit.html",context)

# Maqolani o'chirish
def deleteData(request,id):
    post = Post.objects.get(id=id)
    post.delete()
    messages.error(request,"Maqola o'chirildi")
    return redirect("/insert")


#    ------ Kategoriya --------
# Kategoriyalar yaratish
def insertCategory(request):
    categories = Category.objects.all()
    if request.method=="POST":
        title=request.POST.get('title')
        query=Category(title=title)
        query.save()
        messages.info(request,"Kategoriya muvaffaqiyatli qo'shildi")
        return redirect("/insertctg")
    ctx = {
        'categories': categories
    }
    return render(request,"blog/category_insert.html", context=ctx)

# Kategoriyani tahrirlash
def updateCategory(request,id):
    categories = Category.objects.all()
    if request.method=="POST":
        title=request.POST['title']

        edit=Category.objects.get(id=id)
        edit.title=title
        edit.save()
        messages.warning(request,"Kategoriya muvaffaqiyatli o'zgartirildi")
        return redirect("/insertctg")
    category =Category.objects.get(id=id)
    context={
        "category":category,
        'categories': categories
    }
    return render(request,"blog/category_edit.html",context)

# Kategoriyani o'chirish
def deleteCategory(request,id):
    ctg = Category.objects.get(id=id)
    ctg.delete()
    messages.error(request,"Kategoriya o'chirildi")
    return redirect("/insertctg")