import json
from django.http import JsonResponse
from django.views import View
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from .models import UserProfile

@method_decorator(csrf_exempt, name='dispatch')
class UserAPIView(View):
    
    
    def get(self, request):
        users = UserProfile.objects.all()
        user_list = [user.to_dict() for user in users]
        
      
        return JsonResponse({"status": "success", "data": user_list}, status=200)


    def post(self, request):
        try:
            
            body = json.loads(request.body)
            name = body.get('name')
            email = body.get('email')

            if not name or not email:
               
                return JsonResponse(
                    {"error": "Bad Request", "message": "Name and email are required."}, 
                    status=400
                )
            
            if UserProfile.objects.filter(email=email).exists():
                
                return JsonResponse(
                    {"error": "Bad Request", "message": "Email already exists."}, 
                    status=400
                )

   
            new_user = UserProfile.objects.create(name=name, email=email)

          
            return JsonResponse(
                {"status": "success", "data": new_user.to_dict()}, 
                status=201
            )

        except json.JSONDecodeError:
            
            return JsonResponse(
                {"error": "Bad Request", "message": "Invalid JSON format."}, 
                status=400
            )
        except Exception as e:
            
            return JsonResponse(
                {"error": "Internal Error", "message": str(e)}, 
                status=500
            )