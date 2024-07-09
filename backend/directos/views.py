# directos/views.py
from django.http import JsonResponse
from .models import Directo

def search_directos(request):
    query = request.GET.get('query', '')
    results = Directo.objects.filter(title__icontains=query) | Directo.objects.filter(category__icontains=query)
    data = list(results.values('title', 'description', 'category'))
    return JsonResponse(data, safe=False)
