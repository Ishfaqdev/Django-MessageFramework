from django.shortcuts import render
from django.contrib import messages
from . forms import RegistrationForm
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your account has been registered')
            messages.info(request, 'Now you can login')
    else:
        form = RegistrationForm()
    return render(request, 'enroll/registration.html', {'form': form})
