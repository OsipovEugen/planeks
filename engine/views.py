from django.contrib.auth.views import LoginView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, ListView, UpdateView, DeleteView, DetailView

from engine.forms import SchemaForm, SchemaFormSet
from engine.models import Schema


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
        formset = SchemaFormSet(queryset=Schema.objects.none())
        return self.render_to_response({'schema_formset': formset})

    # Define method to handle POST request
    def post(self, *args, **kwargs):

        formset = SchemaFormSet(data=self.request.POST)

        # Check if submitted forms are valid
        if formset.is_valid():
            formset.save()
            return redirect(reverse_lazy("schema_list"))

        return self.render_to_response({'schema_formset': formset})


class SchemaUpdateView(UpdateView):
    form_class = SchemaForm
    model = Schema
    success_url = reverse_lazy('schema_list')
    template_name = 'engine/schema_update.html'

class SchemaDetailView(DetailView):
    model = Schema
    template_name = 'engine/schema_detail.html'
    context_object_name = 'schema'


class SchemaDeleteView(DeleteView):
    model = Schema
    success_url = reverse_lazy('schema_list')
    template_name = 'engine/schema_delete.html'
