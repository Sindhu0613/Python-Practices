from rest_framework import generics
from .models import AudioRecording
from .serializers import AudioRecordingSerializer

class AudioRecordingListCreate(generics.ListCreateAPIView):
    queryset = AudioRecording.objects.all()
    serializer_class = AudioRecordingSerializer
