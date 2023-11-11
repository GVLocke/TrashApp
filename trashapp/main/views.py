from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.urls import resolve
from django.views.decorators.http import require_POST
from django.shortcuts import render, redirect, get_object_or_404
from .models import DistanceMeasurement, TrashCan

from django.http import JsonResponse

@require_POST
def create_trash_can(request):
    name = request.POST.get('name')
    if name:
        TrashCan.objects.create(name=name)
    return redirect('main_page')

from django.views.decorators.http import require_POST


def delete_trash_can(request, trash_can_id):
    trash_can = get_object_or_404(TrashCan, pk=trash_can_id)

    if request.method == 'POST':
        trash_can.delete()
        return redirect('main_page')  # Redirect to the appropriate view after deletion

    return render(request, 'main/delete_trash_can.html', {'trash_can': trash_can})

@require_POST
@csrf_exempt
def receive_distance_data(request):
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

def main_page(request):
    trash_cans = TrashCan.objects.all()
    context = {'trash_cans': trash_cans}
    current_url = resolve(request.path_info).url_name
    print(current_url)
    return render(request, 'main/mainpage.html', context)