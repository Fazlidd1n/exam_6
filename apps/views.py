from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from apps.forms import CarbonadForm
from apps.models import Carbonad


class CarbonadListVeiw(ListView):
    template_name = 'index.html'
    queryset = Carbonad.objects.order_by('-id')
    context_object_name = 'carbonads'


class CarbonadUpdateView(UpdateView):
    template_name = 'update_product.html'
    form_class = CarbonadForm
    model = Carbonad
    success_url = reverse_lazy('carbonad_list')


class CarbonadDeleteView(DeleteView):
    template_name = 'delete_todo.html'
    model = Carbonad
    queryset = Carbonad.objects.all()
    success_url = reverse_lazy('carbonad_list')

#
# def delete_product(request, pk):
#     Carbonad.objects.filter(id=pk).delete()
#     return redirect("product_list")
#
#
# def update_product(request, pk):
#     if request.method == 'POST':
#         Carbonad.objects.filter(id=pk).update(name=request.POST['name'], price=request.POST['price'])
#         return redirect('product_list')
#     context = {
#         'product': Product.objects.filter(id=pk)
#     }
#     return render(request, 'update_product.html', context)
