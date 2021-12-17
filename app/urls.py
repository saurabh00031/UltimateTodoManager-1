

from django.contrib import admin
from django.urls import path
from app import views 


urlpatterns = [
   path('' , views.home , name='home' ), 
   path('login/' ,views.login  , name='login'), 
   path('signup/' , views.signup ), 
   path('update/<int:id>/' , views.update ,name="update" ),
   path('deletes/<int:id>/' , views.deletes ,name="deletes" ),
   path('add-todo/' , views.add_todo ), 
   path('delete-todo/<int:id>/' , views.delete_todo ), 
   path('change-status/<int:id>/<str:status>/' , views.change_todo ), 
   path('logout/' , views.signout ), 
   path('about/' , views.about ,name="about" ),
]



#another method to call that functions

# from django.contrib import admin
# from django.urls import path
# from app.views import home , login , signup , add_todo , signout , delete_todo, change_todo,update,deletes


# urlpatterns = [
#    path('' , home , name='home' ), 
#    path('login/' ,login  , name='login'), 
#    path('signup/' , signup ), 
#    path('update/<int:id>/' , update ,name="update" ),
#    path('deletes/<int:id>/' , deletes ,name="deletes" ),
#    path('add-todo/' , add_todo ), 
#    path('delete-todo/<int:id>' , delete_todo ), 
#    path('change-status/<int:id>/<str:status>' , change_todo ), 
#    path('logout/' , signout ), 
# ]
