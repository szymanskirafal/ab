
from django.http import HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group


from .forms import NewGroupForm





@login_required
def grupa(request):
    current_user = request.user
    grupy = current_user.groups.all()
    return render(request, 'grupa/grupa.html', {
        'current_user': current_user,
        'grupy': grupy})




@login_required
def nowa(request):
    group_creator = request.user
    if request.method == 'POST':
        form = NewGroupForm(request.POST)
        if form.is_valid():
            group_name = form.cleaned_data['group_name']
            new_group = Group.objects.create(name=group_name)
            new_group.user_set.add(group_creator)

            return HttpResponseRedirect('/dodane/')
    else:
        form = NewGroupForm()

    return render(request, 'grupa/new_group.html', {'form': form})


@login_required
def group(request, group_name):

    return render(request, 'grupa/group.html')
