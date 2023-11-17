from django.contrib.auth.decorators import login_required
import random
from django.contrib.auth import login, logout
from django.shortcuts import render, redirect


# def index(request):
#     name = request.GET.get('name', '')
#     message = request.GET.get('message', '')
#     return HttpResponse(f"Hello {name}! {message}!")


def random_code(request):
    code = str(random.randint(1000, 9999))
    return render(request, 'random.html', {'code': code})


@login_required
def auth_random(request):
    if request.method == 'GET':
        logout(request)
    code = str(random.randint(1000, 9999))
    request.session['code'] = code

    return render(request, 'auth_random.html', {'code': request.session['code']})

# @login_required
# def update_auth_random(request):
#     request.session['code'] = str(random.randint(1000, 9999))
#     return redirect('login')

