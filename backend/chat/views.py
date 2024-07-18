# chat/views.py
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import get_user_model
from .models import ChatMessage
from directos.models import Directo
import json

User = get_user_model()

@csrf_exempt
def get_chat_messages(request, directo_id):
    if request.method == 'GET':
        messages = ChatMessage.objects.filter(directo__id=directo_id).order_by('timestamp')
        data = [{"user": message.user.email, "message": message.message, "timestamp": message.timestamp} for message in messages]
        return JsonResponse(data, safe=False)

@csrf_exempt
def send_chat_message(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        try:
            user = User.objects.get(email=data['user'])
            directo = Directo.objects.get(id=data['directo_id'])
            message = data['message']
            chat_message = ChatMessage.objects.create(user=user, directo=directo, message=message)
            return JsonResponse({"success": True, "message": "Message sent successfully"})
        except User.DoesNotExist:
            return JsonResponse({"success": False, "message": "User does not exist"})
        except Directo.DoesNotExist:
            return JsonResponse({"success": False, "message": "Directo does not exist"})
        except Exception as e:
            return JsonResponse({"success": False, "message": str(e)})