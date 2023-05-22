from django import forms





class SourceDocumentForm(forms.Form):
    source_document = forms.FileField()

class CandidateDocumentForm(forms.Form):
    candidate_document = forms.FileField()

'''
class DocumentUploadForm(forms.Form):
    candidate_docs = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    source_docs = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
'''
