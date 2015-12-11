from django.shortcuts import render

from django.contrib.auth.decorators import login_required










@login_required
def grupa(request):
    return render(request, 'grupa/grupa.html')
