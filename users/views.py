from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm

def register(request):
    """Rejestration of new user"""
    if request.method != 'POST':
        # Send empty form for user rejestration
        form = UserCreationForm()
    else:
        # Form with data
        form = UserCreationForm(data=request.POST)
        if form.is_valid():
            new_user = form.save()
            # Login new user and move to main page
            login(request, new_user)
            return redirect('learning_logs:index')

    # Show empty form
    context = {'form': form}
    return render(request, 'registration/register.html', context)
    

