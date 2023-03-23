import csv
import datetime
import os

from django.conf import settings
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse_lazy
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView, ListView, UpdateView, DeleteView, DetailView

from engine.forms import SchemaForm, DataFormSet
from engine.models import Schema, Data


class CustomLoginView(LoginView):
    template_name = 'engine/login.html'


class SchemaListView(ListView):
    model = Schema
    template_name = 'engine/schema_list.html'
    context_object_name = 'schemas'


class SchemaAddView(TemplateView):
    template_name = "engine/schema_create.html"

    def get(self, *args, **kwargs):
        schema_form = SchemaForm
        data_formset = DataFormSet(queryset=Schema.objects.none())

        return self.render_to_response({'data_formset': data_formset, 'schema_form': schema_form})

    # Define method to handle POST request
    def post(self, *args, **kwargs):
        schema_form = SchemaForm(data=self.request.POST)
        data_formset = DataFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if data_formset.is_valid() and schema_form.is_valid():
            schema = schema_form.save()
            data = data_formset.save(commit=False)
            for row in data:
                row.created_at = schema.created_at
                row.save()
            return redirect(reverse_lazy("schema_list"))
        return self.render_to_response({'data_formset': data_formset, 'schema_form': schema_form})


class SchemaUpdateView(UpdateView):
    form_class = SchemaForm
    model = Schema
    success_url = reverse_lazy('schema_list')
    template_name = 'engine/schema_update.html'


class SchemaDetailView(DetailView):
    model = Schema
    template_name = 'engine/schema_detail.html'
    context_object_name = 'schema'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        schema = Schema.objects.get(pk=self.kwargs['pk'])
        data = Data.objects.filter(created_at=schema.created_at)
        schema_path = os.path.join(settings.MEDIA_ROOT, schema.name)
        try:
            os.listdir(schema_path)
            schema_list = os.listdir(schema_path)
            context['schema_files'] = schema_list[::-1]
        except FileNotFoundError:
            pass
        context['data'] = data
        return context


class SchemaDeleteView(DeleteView):
    model = Schema
    success_url = reverse_lazy('schema_list')
    template_name = 'engine/schema_delete.html'


@csrf_exempt
def export_csv(request, pk):
    amount = int(request.POST.get('amount'))
    schema = Schema.objects.get(id=pk)
    data = Data.objects.filter(created_at=schema.created_at)
    schema_path = os.path.join(settings.MEDIA_ROOT, schema.name)

    if not os.path.exists(schema_path):
        print('here')
        os.makedirs(schema_path)

    with open(f"media/{schema.name}/{schema.name}_{datetime.datetime.now().strftime('%H_%M_%S')}.csv", 'x', newline='',
              encoding='UTF8') as f:
        writer = csv.writer(f)
        writer.writerow(['Order', 'Column Name', 'Column Type'])
        data_fields = data.values_list('order', 'data_name', 'data_type')
        while amount != 0:
            for d in data_fields:
                writer.writerow(d)
            amount -= 1
    return JsonResponse(data={})


def download(request, schema_name):
    schema_path = os.path.join(settings.MEDIA_ROOT, schema_name.split('_', maxsplit=1)[0])
    for file in os.listdir(schema_path):
        if file == schema_name:
            schema_path = os.path.join(schema_path, file)
            break
    with open(schema_path, 'rb') as f:
        response = HttpResponse(f.read(), content_type='text/csv')
        response['Content-Disposition'] = f'attachment; filename="{schema_path}"'
        return response
