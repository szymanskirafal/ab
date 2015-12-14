
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .forms import NewGroupForm





@login_required
def grupa(request):
    return render(request, 'grupa/grupa.html')




@login_required
def nowa(request):
    if request.method == 'POST':
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            new_group = Group.objects.create(name=group_name)

            return HttpResponseRedirect('/dodane/')
    else:
        form = NewGroupForm()

    return render(request, 'grupa/new_group.html', {'form': form})
