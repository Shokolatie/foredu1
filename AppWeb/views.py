from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from .models import AddClient, VectorWork
from .forms import AddClientForm

def index(request):
    cls = AddClient.objects.all()
    vectors_work = VectorWork.objects.all()
    context = {'cls': cls, 'vectors_work': vectors_work}
    return render(request, 'AppWeb/index.html', context)


def by_VectorWork(request, VectorWork_id):
    cls = AddClient.objects.filter(vectorWork_id=VectorWork_id)
    vectors_work = VectorWork.objects.all()
    current_vector = VectorWork.objects.get(pk=VectorWork_id)
    context = {'cls': cls, 'vectors_work': vectors_work, 'current_vector': current_vector}
    return render(request, 'AppWeb/by_VectorWork.html', context)


class AddClientCreateView(CreateView):
    template_name = 'AppWeb/add.html'
    form_class = AddClientForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vectorWork'] = VectorWork.objects.all()
        return context


