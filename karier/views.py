from django.shortcuts import render
from .models import TruckModel
from .models import Truck
from .forms import TruckForm


# Create your views here.
def truck_table(request):
    if request.method == "POST":
        form = TruckForm(request.POST)
        if form.is_valid() and request.POST['TruckModels'] != "ALL":
            trucks = Truck.objects.filter(model__name__exact=request.POST['TruckModels'])
        else:
            trucks = Truck.objects.all()
    else:
        trucks = Truck.objects.all()
        form = TruckForm()
    models = TruckModel.objects.all()
    return render(request, 'karier/truck_table.html', {'trucks': trucks, 'models': models, 'form': form})
