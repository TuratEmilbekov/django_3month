from django.http.response import Http404, HttpResponse
from django.shortcuts import get_object_or_404, render
from . import models, forms
from django.views import generic


# Create your views here.
class CarListView(generic.ListView):
    template_name = 'car_list.html'
    queryset = models.Car.objects.all()
    
    def get_queryset(self):
        return models.Car.objects.all()




class CarDetailView(generic.DetailView):
    template_name = 'car_detail.html'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get("id")
        return get_object_or_404(models.Car, id=post_id)




class CarCreateView(generic.CreateView):
    template_name = 'add_car.html'
    form_class = forms.CarForm
    seccess_url = '/cars/'
    queryset = models.Car.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)



class CarUpdateView(generic.UpdateView):
    template_name = 'add-car'
    form_class = forms.CarForm

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id=post_id)


    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form=form)



class CarDeleteView(generic.DetailView):
    template_name = 'car_delete.html'
    seccess_url = '/cars/'

    def get_object(self, **kwargs):
        post_id = self.kwargs.get('id')
        return get_object_or_404(models.Car, id-post_id)