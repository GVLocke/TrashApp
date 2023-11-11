import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from .models import DistanceMeasurement

@csrf_exempt
def receive_distance_data(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body.decode('utf-8'))
            distance_value = data.get('distance')

            if distance_value is not None:
                DistanceMeasurement.objects.create(distance=distance_value)
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'message': 'Invalid data'})
        except json.JSONDecodeError:
            return JsonResponse({'status': 'error', 'message': 'Invalid JSON data'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method'})
    
def main_page(request):
    latest_measurment = DistanceMeasurement.objects.last()

    context = {'latest_measurment': latest_measurment}
    return render(request, 'main/mainpage.html', context)