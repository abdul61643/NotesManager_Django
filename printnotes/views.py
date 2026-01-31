from django.shortcuts import render, get_object_or_404
from notes.models import Note

def print_notes(request):
    notes = Note.objects.all().order_by('-created_at')
    return render(request, 'printnotes/print_notes.html', {'notes': notes})

def print_single_note(request, id):
    note = get_object_or_404(Note, id=id)
    return render(request, 'printnotes/print_single_note.html', {'note': note})