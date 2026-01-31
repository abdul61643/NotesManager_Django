
from django.shortcuts import render, redirect, get_object_or_404
from .models import Note
from django.forms import ModelForm
from django import forms


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'content']
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter note title'
            }),
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 5,
                'placeholder': 'Write your note here...'
            }),
        }

def notes_list(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'notes/notes_list.html', {'notes': notes})


def create_note(request):
    form = NoteForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('notes_list')
    return render(request, 'notes/notes_form.html', {'form': form})

def update_note(request, id):
    note = get_object_or_404(Note, id=id)
    form = NoteForm(request.POST or None, instance=note)
    if form.is_valid():
        form.save()
        return redirect('notes_list')
    return render(request, 'notes/notes_form.html', {'form': form})

def delete_note(request, id):
    note = get_object_or_404(Note, id=id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes_list')
    return render(request, 'notes/notes_confirm_delete.html', {'note': note})
