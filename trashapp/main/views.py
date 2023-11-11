import json
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import DistanceMeasurement
from django.http import HttpResponse

from django.http import JsonResponse

@csrf_exempt
def receive_distance_data(request):
    if request.method == 'POST':
        serial_data = request.POST.get('serial_data')

        # Check if serial_data is None
        if serial_data is None:
            return JsonResponse({'error': 'No serial_data in request'}, status=400)

        # Try to convert serial_data to a float
        try:
            distance = float(serial_data)
        except ValueError:
            return JsonResponse({'error': 'serial_data could not be converted to a float'}, status=400)

        DistanceMeasurement.objects.create(distance=distance)
        return JsonResponse({'status': 'Success'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)

def main_page(request):
    # Get the latest DistanceMeasurement object
    latest_measurement = DistanceMeasurement.objects.order_by('-created_at').first()

    # Pass the latest_measurement to the template
    context = {'latest_measurement': latest_measurement}
    return render(request, 'main/mainpage.html', context)