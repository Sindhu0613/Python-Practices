from rest_framework import serializers
from .models import AudioRecording

class AudioRecordingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AudioRecording
        fields = ['id', 'title', 'audio_file', 'uploaded_at']
