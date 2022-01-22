from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.urls import reverse
from django.views.generic import ListView, UpdateView, DetailView, CreateView
from .forms import CreateNewTask
from .models import Todo


class Index(LoginRequiredMixin, ListView):
    paginate_by = 10
    page_kwarg = 'pg'
    template_name = 'todo.html'
    context_object_name = 'todo_list'

    def get_queryset(self):
        return Todo.objects.filter(user=self.request.user)


class Edit(LoginRequiredMixin, UpdateView):
    template_name = 'edit.html'
    fields = ('title', 'description', 'condition')

    def get_object(self, queryset=None):
        res = get_object_or_404(Todo, pk=self.kwargs['pk'])
        if res.user != self.request.user:
            raise Http404
        return res

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})


class ViewDetail(LoginRequiredMixin, DetailView):
    template_name = 'view.html'

    def get_object(self, queryset=None):
        res = get_object_or_404(Todo, pk=self.kwargs['pk'], user=self.request.user)
        if res.user != self.request.user:
            raise Http404
        return res


class CreateTask(LoginRequiredMixin, CreateView):
    form_class = CreateNewTask
    template_name = 'create.html'

    def form_valid(self, form):
        self.object = form.save(self.request.user)
        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('view', kwargs={'pk': self.object.pk})
