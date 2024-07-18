# backend/directos/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View
from .models import Directo
import json

def search_directos(request):
    query = request.GET.get('query', '')
    results = Directo.objects.filter(title__icontains=query) | Directo.objects.filter(category__icontains=query)
    data = list(results.values('id', 'title', 'description', 'category', 'video_url', 'rating'))  # Incluye la calificación
    return JsonResponse(data, safe=False)

@method_decorator(csrf_exempt, name='dispatch')
class UpdateRatingView(View):
    def post(self, request, *args, **kwargs):
        data = json.loads(request.body)
        directo_id = data.get('directo_id')
        rating = data.get('rating')

        try:
            directo = Directo.objects.get(id=directo_id)
            directo.rating = rating
            directo.save()
            return JsonResponse({'status': 'success', 'rating': rating})
        except Directo.DoesNotExist:
            return JsonResponse({'status': 'error', 'message': 'Directo not found'}, status=404)
