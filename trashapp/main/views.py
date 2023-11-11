import json
import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import DistanceMeasurement, TrashCan
from django.http import HttpResponse

from django.http import JsonResponse

@csrf_exempt
def receive_distance_data(request):
    if request.method == 'POST':
        trash_can_name = request.POST.get('trash_can')
        serial_data = request.POST.get('serial_data')

        if trash_can_name is None or serial_data is None:
            return JsonResponse({'error': 'Missing trash_can or serial_data in request'}, status=400)

        try:
            trash_can = TrashCan.objects.get(name=trash_can_name)
        except TrashCan.DoesNotExist:
            return JsonResponse({'error': 'Trash can does not exist'}, status=400)

        try:
            distance = float(serial_data)
        except ValueError:
            return JsonResponse({'error': 'serial_data could not be converted to a float'}, status=400)

        DistanceMeasurement.objects.create(distance=distance, trash_can=trash_can)
        return JsonResponse({'status': 'Success'})

    return JsonResponse({'error': 'Method not allowed'}, status=405)

def main_page(request):
    # Get the latest DistanceMeasurement object
    latest_measurement = DistanceMeasurement.objects.order_by('-created_at').first()

    # Pass the latest_measurement to the template
    context = {'latest_measurement': latest_measurement}
    return render(request, 'main/mainpage.html', context)