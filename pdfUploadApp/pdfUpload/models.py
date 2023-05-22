from django.db import models

class SourceDocument(models.Model):
    document = models.FileField(upload_to='source_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.name

class CandidateDocument(models.Model):
    document = models.FileField(upload_to='candidate_documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.document.name
