from django.shortcuts import render
from places.models import Place
from django.http import HttpResponse
from django.shortcuts import get_object_or_404


def show_main(request):
    places = Place.objects.all()
    features = []
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.latitude, place.longitude]
            },
            "properties": {
                "title": place.title,
                "placeId": place.id,
                "detailsUrl": {
                    "title": place.title,
                    "imgs": place.get_images_paths(),
                    "description_short": place.description_short,
                    "description_long": place.description_long,
                    "coordinates": {
                        "lng": place.longitude,
                        "lat": place.latitude
                    }
                }
            }
        }
        features.append(feature)
    places_for_render = {
        "type": "FeatureCollection",
        "features": features
    }

    return render(request, "index.html", context={"places": places_for_render})


def show_place(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    return HttpResponse(f'{place.title}')
