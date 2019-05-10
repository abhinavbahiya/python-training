from django.shortcuts import render, HttpResponse

# Create your views here.

def login(request):
    return render(request, 'login.html', {})
    #return HttpResponse('You are at login page')

def validate(request):
    if request.method == 'POST':
        u = request.POST['uname']
        p = request.POST['pwd']
        from .models import account_module
        try: 
            account_module.objects.get(username=u)
            return HttpResponse('Successfully Login')
        except:
            a = account_module()
            a.username = u
            a.password = p
            a.save()
            return HttpResponse('User Created')
    else:
        return HttpResponse('Bbye!')

def createaccount(request):
    return HttpResponse(request)