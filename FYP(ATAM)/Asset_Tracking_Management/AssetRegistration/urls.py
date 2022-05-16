from django.urls import path
from AssetRegistration import views

urlpatterns = [

   path('asset', views.asset),
   path('show', views.show),
   path('edit/<int:id>', views.edit),
   path('update/<int:id>', views.update),
   path('delete/<int:id>', views.destroy),
   
   
]