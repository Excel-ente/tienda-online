from django.http import JsonResponse
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

@require_GET
def status(request):
    if request.user.is_authenticated:
        return JsonResponse({'authenticated': True, 'username': request.user.username})
    return JsonResponse({'authenticated': False})

@require_POST
def register(request):
    username = request.POST.get('username')
    email = request.POST.get('email')
    password = request.POST.get('password')
    if User.objects.filter(username=username).exists() or User.objects.filter(email=email).exists():
        return JsonResponse({'error': 'exists'}, status=400)
    if len(password or '') < 8:
        return JsonResponse({'error': 'password_short'}, status=400)
    user = User.objects.create_user(username=username, email=email, password=password)
    login(request, user)
    return JsonResponse({'username': user.username, 'email': user.email})

@require_POST
def login_view(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    if user is None:
        try:
            u = User.objects.get(email=username)
            user = authenticate(request, username=u.username, password=password)
        except User.DoesNotExist:
            pass
    if user is None:
        return JsonResponse({'error': 'invalid'}, status=400)
    if not user.is_active:
        return JsonResponse({'error': 'inactive'}, status=400)
    login(request, user)
    return JsonResponse({'username': user.username, 'email': user.email})

@require_POST
def logout_view(request):
    logout(request)
    return JsonResponse({'ok': True})
