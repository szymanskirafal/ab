from django.views import generic
from django.core.urlresolvers import reverse

from django.contrib.auth.mixins import LoginRequiredMixin

from baza.models import DopuszczeniaLegalizacje

from .forms import ZadanieForm
from .models import Zadanie


class ZadanieCreateView(LoginRequiredMixin, generic.CreateView):
    model = Zadanie
    form_class = ZadanieForm
    template_name = "zadania/create.html"

    def form_valid(self, form):
        form.instance.dopuszczenie = DopuszczeniaLegalizacje.objects.get(pk=self.kwargs["dopuszczenie_id"])
        return super().form_valid(form)

    def get_success_url(self):
        return reverse("baza:dopuszczenie_detail", kwargs={"pk": self.kwargs["dopuszczenie_id"]})


class ZadanieDetailView(generic.DetailView):
    context_object_name = "zadanie"
    model = Zadanie
    template_name = "zadania/detail.html"