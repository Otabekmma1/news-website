from django.urls import path
from .views import (home, category, post, post_create, updateData, deleteData,
                    insertCategory, updateCategory, deleteCategory)

urlpatterns = [
    path('', home, name='home'),
    path('category/<int:category_id>/', category, name='categories'),
    path('post/<int:id>/', post, name='posts'),
    path('insert/', post_create, name="create"),
    path('update/<id>/', updateData, name="updateData"),
    path('delete/<id>/', deleteData, name="deleteData"),
    path('insertctg/', insertCategory, name="insertcategory"),
    path('updatectg/<id>/', updateCategory, name="updatecategory"),
    path('deletectg/<id>/', deleteCategory, name="deletecategory"),
]