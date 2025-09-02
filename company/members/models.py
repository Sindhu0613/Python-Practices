from django.db import models

class AudioRecording(models.Model):
    title = models.CharField(max_length=100)
    audio_file = models.FileField(upload_to='members/')
    uploaded_at = models.DateTimeField(auto_now_add=True)
