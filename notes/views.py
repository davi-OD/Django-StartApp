from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import Http404
from .models import Notes
from django.views.generic.edit import DeleteView
from django.views.generic import CreateView, DetailView, ListView, UpdateView
from .forms import NotesForm
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class NotesCreateView(CreateView):
    model = Notes
    # fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.htm'

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.user = self.request.user
        self.object.save()
        return HttpResponseRedirect(self.get_success_url())


class NotesListView(LoginRequiredMixin, ListView):
    model = Notes
    context_object_name = "notes"
    # template_name = 'notes/notes_list.htm'
    login_url = "/admin"

    def get_queryset(self):
        return self.request.user.notes.all()

# def list(request):
#     all_notes = Notes.objects.all()
#     return render(request, 'notes/notes_list.htm', {'notes': all_notes})


class NotesDetailView(DetailView):
    model = Notes
    context_object_name = 'note'
    template_name = 'notes/notes_detail.htm'

# def detail(request, pk):
#     try:
#         note = Notes.objects.get(pk=pk)
#     except Notes.DoesNotExist:
#         raise Http404("Note doesn't exist")
#     return render(request, 'notes/notes_detail.htm', {'note': note})


class NotesUpdateView(UpdateView):
    model = Notes
    # fields = ['title', 'text']
    form_class = NotesForm
    success_url = '/smart/notes'
    template_name = 'notes/notes_form.htm'


class NotesDeleteView(DeleteView):
    model = Notes
    success_url = '/smart/notes'
    template_name = 'notes/notes_delete.html'
