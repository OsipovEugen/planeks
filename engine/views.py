from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView

from engine.forms import SchemaForm, DataFormSet
from engine.models import Schema, Data


class CustomLoginView(LoginView):
    template_name = 'engine/login.html'


# class SchemaCreate(CreateView):
#     form_class = SchemaForm
#     success_url = '/home'
#     template_name = 'engine/schema_create.html'

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
        context['data'] = data
        return context


class SchemaDeleteView(DeleteView):
    model = Schema
    success_url = reverse_lazy('schema_list')
    template_name = 'engine/schema_delete.html'


