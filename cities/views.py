from django.http import JsonResponse, HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt
from django.db import transaction
from django.http import HttpResponseNotFound


from .models import City, Coord


def index(request, q=''):
    if q != '':
        cities = City.objects.filter(name__contains=q)
        result_list = list(cities.values('name', 'country'))
        return JsonResponse(result_list, safe=False)
    return HttpResponseNotFound("hello")


@csrf_exempt
@transaction.atomic
def load_city_json(request):
    if request.method == 'POST':
        try:
            received_json_data = json.loads(request.body)
            with transaction.atomic():
                for obj in received_json_data:
                    cm = City()
                    cc = Coord()
                    cc.lat = obj['coord']['lat']
                    cc.lon = obj['coord']['lon']
                    cc.save()
                    cm.name = obj['name']
                    cm.country = obj['country']
                    cm.ow_id = obj['id']
                    cm.coord = cc
                    cm.save()

            return HttpResponse("successss")
        except IndexError:
            return HttpResponse("un success db")
    return HttpResponse("nope")
