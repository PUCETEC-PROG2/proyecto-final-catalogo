from django.http import HttpResponse
from django.template import loader
from django.contrib.auth.views import LoginView
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils import timezone
from .models import DVD
from .models import VHS
from .models import VideoEquipments
from .models import Client
from .models import Purchase, Product
from catalogo.forms import DVDForm, VHSForm, VideoEquipmentsForm, PurchaseForm, ClientForm

#Catalogo inicio

def index(request):
    dvds = DVD.objects.all()
    vhss = VHS.objects.all()
    video_equipments = VideoEquipments.objects.all()
    template = loader.get_template('index.html')
    return HttpResponse(template.render(
        {
            'dvds': dvds,
            'vhss': vhss,
            'videoequipments': video_equipments,
        },
        request))

#Listas

def DVDs(request):
    dvds = DVD.objects.all()
    template = loader.get_template('dvd_list.html')
    return HttpResponse(template.render(
        {
            'dvds':dvds,
        },
        request))

def VHSs(request):
    VHSs = VHS.objects.all()
    template = loader.get_template('vhs_list.html')
    return HttpResponse(template.render(
        {
            'vhss':VHSs,
        },
        request))

def Video_Equipments(request):
    videoequipments = VideoEquipments.objects.all()
    template = loader.get_template('video_equipments_list.html')
    return HttpResponse(template.render(
        {
            'videoequipments':videoequipments,
        },
        request))

def Purchases(request):
    purchases = Purchase.objects.all()
    template = loader.get_template('purchases_list.html')
    return HttpResponse(template.render(
        {
            'purchases':purchases,
        },
        request))

def Clients(request):
    clients = Client.objects.all()
    template = loader.get_template('clients_list.html')
    return HttpResponse(template.render(
        {
            'clients':clients,
        },
        request))

#Información (Display)

def dvd(request, DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    template = loader.get_template('display_dvd.html')
    context = {
        'dvd': dvd
    }
    return HttpResponse(template.render(context, request))

def vhs(request, VHS_id):
    vhs = VHS.objects.get(id=VHS_id)
    template = loader.get_template('display_vhs.html')
    context = {
        'vhs': vhs
    }
    return HttpResponse(template.render(context, request))

def videoequipment(request, VE_id):
    videoequipment = VideoEquipments.objects.get(id=VE_id)
    template = loader.get_template('display_video_equipments.html')
    context = {
        'videoequipment': videoequipment
    }
    return HttpResponse(template.render(context, request))

def purchase(request, purchase_id):
    purchase = Purchase.objects.get(id=purchase_id)
    products = purchase.products.all()
    print(products)
    template = loader.get_template('display_purchase.html')
    context = {
        'purchase': purchase,
        'products': products
    }
    return HttpResponse(template.render(context, request))

@login_required

# DVD VIEWS

def add_DVD(request):
    if request.method == 'POST':
        form = DVDForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm()
    
    return render(request, 'dvd_form.html', {'form': form})

def edit_DVD(request, DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    if request.method == 'POST':
        form = DVDForm(request.POST, request.FILES, instance=dvd)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = DVDForm(instance=dvd)
    
    return render(request, 'dvd_form.html', {'form': form})

def delete_DVD(request, DVD_id):
    dvd = DVD.objects.get(id=DVD_id)
    dvd.delete()
    return redirect('catalogo:index')

# VHS VIEWS

def add_VHS(request):
    if request.method == 'POST':
        form = VHSForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VHSForm()
    
    return render(request, 'vhs_form.html', {'form': form})

def edit_VHS(request, VHS_id):
    vhs = VHS.objects.get(id=VHS_id)
    if request.method == 'POST':
        form = VHSForm(request.POST, request.FILES, instance=vhs)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VHSForm(instance=vhs)
    
    return render(request, 'vhs_form.html', {'form': form})

def delete_VHS(request, VHS_id):
    vhs = VHS.objects.get(id=VHS_id)
    vhs.delete()
    return redirect('catalogo:index')

# VIDEO_EQUIPMENTS VIEWS

def add_VideoEquipments(request):
    if request.method == 'POST':
        form = VideoEquipmentsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VideoEquipmentsForm()
    
    return render(request, 'video_equipments_form.html', {'form': form})

def edit_VideoEquipments(request, VE_id):
    VideoEquipment = VideoEquipments.objects.get(id=VE_id)
    if request.method == 'POST':
        form = VideoEquipmentsForm(request.POST, request.FILES, instance=VideoEquipment)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = VideoEquipmentsForm(instance=VideoEquipment)
    
    return render(request, 'video_equipments_form.html', {'form': form})

def delete_VideoEquipments(request, VE_id):
    VideoEquipment = VideoEquipments.objects.get(id=VE_id)
    VideoEquipment.delete()
    return redirect('catalogo:index')

# Purchases views

def add_Purchase(request):
    if request.method == "POST":
        form = PurchaseForm(request.POST)
        if form.is_valid():
            purchase = form.save(commit=False)
            purchase.date = timezone.now()
            purchase.total_price = form.cleaned_data['total_price']
            purchase.save()

            selected_products = form.cleaned_data['products']
            purchase.products.set(selected_products)

            return redirect("catalogo:Purchases")
    else:
        form = PurchaseForm()

    products = Product.objects.all()

    return render(request, "purchase_form.html", {"form": form, "products": products})

# Clients Views

def add_Client(request):
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = ClientForm()
    
    return render(request, 'client_form.html', {'form': form})

def edit_Client(request, client_id):
    client = Client.objects.get(id=client_id)
    if request.method == 'POST':
        form = ClientForm(request.POST, request.FILES, instance=client)
        if form.is_valid():
            form.save()
            return redirect('catalogo:index')
    else:
        form = ClientForm(instance=client)
    
    return render(request, 'client_form.html', {'form': form})

def delete_Client(request, client_id):
    client = Client.objects.get(id=client_id)
    client.delete()
    return redirect('catalogo:index')

#Busquedas

def search(request):
    query = request.GET.get('query', '')
    dvds = DVD.objects.filter(name__icontains=query)
    vhs = VHS.objects.filter(name__icontains=query)
    videoequipments = VideoEquipments.objects.filter(name__icontains=query)

    template = loader.get_template('search_results.html')
    context = {
        'query': query,
        'dvds': dvds,
        'vhss': vhs,
        'videoequipments': videoequipments,
    }
    return HttpResponse(template.render(context, request))

class CustomLoginView(LoginView):
    template_name = "login_form.html"