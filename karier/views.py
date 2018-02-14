from django.shortcuts import render

# Create your views here.
def truck_table(request):
    return render(request, 'karier/truck_table.html', {})
