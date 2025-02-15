from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name = 'catalogo'

urlpatterns = [
    path("", views.index, name="index"),
    #Listas
    path("DVDs/", views.DVDs, name="DVDs"),
    path("VHSs/", views.VHSs, name="VHSs"),
    path("Video_Equipments/", views.Video_Equipments, name="Video_Equipments"),
    path("Purchases/", views.Purchases, name="Purchases"),
    path("Clients/", views.Clients, name="Clients"),

    #Información (Display)
    path("dvd/<int:DVD_id>/", views.dvd, name="dvd"),
    path("vhs/<int:VHS_id>/", views.vhs, name="vhs"),
    path("videoequipment/<int:VE_id>/", views.videoequipment, name="videoequipment"),
    path("purchase/<int:purchase_id>/", views.purchase, name="purchase"),
    path("client/<int:client_id>/", views.client, name="client"),

    #Superusuario (admin)
    path("add_DVD/", views.add_DVD, name="add_DVD"),
    path("edit_DVD/<int:DVD_id>", views.edit_DVD, name="edit_DVD"),
    path("delete_DVD/<int:DVD_id>", views.delete_DVD, name="delete_DVD"),

    path("add_VHS/", views.add_VHS, name="add_VHS"),
    path("edit_VHS/<int:VHS_id>", views.edit_VHS, name="edit_VHS"),
    path("delete_VHS/<int:VHS_id>", views.delete_VHS, name="delete_VHS"),

    path("add_VideoEquipments/", views.add_VideoEquipments, name="add_VideoEquipments"),
    path("edit_VideoEquipments/<int:VE_id>", views.edit_VideoEquipments, name="edit_VideoEquipments"),
    path("delete_VideoEquipments/<int:VE_id>", views.delete_VideoEquipments, name="delete_VideoEquipments"),

    path("add_Purchase/", views.add_Purchase, name="add_Purchase"),

    path("add_Client/", views.add_Client, name="add_Client"),
    path("edit_Client/<int:client_id>", views.edit_Client, name="edit_Client"),
    path("delete_Client/<int:client_id>", views.delete_Client, name="delete_Client"),
    
    path('search/', views.search, name='search'),
    path("login/", views.CustomLoginView.as_view(), name="login"),
    path('accounts/logout/', auth_views.LogoutView.as_view(), name='logout'),
]