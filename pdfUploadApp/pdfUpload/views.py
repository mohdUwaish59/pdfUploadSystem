from django.shortcuts import render, redirect
from .forms import SourceDocumentForm, CandidateDocumentForm
from .models import SourceDocument, CandidateDocument

def upload_documents(request):
    source_form = SourceDocumentForm()
    candidate_form = CandidateDocumentForm()

    if request.method == 'POST':
        if 'source_document_form' in request.POST:
            source_form = SourceDocumentForm(request.POST, request.FILES)
            if source_form.is_valid():
                source_document = SourceDocument(document=request.FILES['source_document'])
                source_document.save()
        elif 'candidate_document_form' in request.POST:
            candidate_form = CandidateDocumentForm(request.POST, request.FILES)
            if candidate_form.is_valid():
                candidate_document = CandidateDocument(document=request.FILES['candidate_document'])
                candidate_document.save()

    source_documents = SourceDocument.objects.all()
    candidate_documents = CandidateDocument.objects.all()

    context = {'source_form': source_form, 'candidate_form': candidate_form, 'source_documents': source_documents, 'candidate_documents': candidate_documents,}

    return render(request, 'upload_documents.html', context)

def home(request):
    return render(request, 'home.html')

def result(request):
    return render(request, 'result.html')
