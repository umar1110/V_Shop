

from faster_whisper import WhisperModel

model = WhisperModel("large-v3")  

def transcribe_audio(file_path: str) -> str:

    segments, info = model.transcribe(file_path, beam_size=5)
    transcription = " ".join([segment.text for segment in segments])
    
    return transcription