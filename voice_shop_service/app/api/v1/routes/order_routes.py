
import time
from fastapi import APIRouter, Form, HTTPException, UploadFile , File
from app.services.voice_services import transcribe_audio
router = APIRouter()


@router.post("/order")
async def create_order(audio_file:UploadFile = File(...)):
    """
    Create a new order with an audio file upload.
    """
    
    if not audio_file.content_type.startswith("audio/"):
        raise HTTPException(status_code=400, detail="Invalid audio file")
    
    # Print file details for debugging
    print(f"Received file: {audio_file.filename}")
    print(f"Content type: {audio_file.content_type}")   
    

     # Save audio temporarily
    temp_path = f"/tmp/{int(time.time())}_{audio_file.filename}"
    
    try:
        with open(temp_path, "wb") as buffer:
            content = await audio_file.read()
            buffer.write(content)
            
        print(f"💾 Audio saved to: {temp_path}")
        # STEP 1: Transcribe audio using Groq Whisper
        print("🎤 Transcribing audio...")
        
        transcription = transcribe_audio(temp_path)
        print(f"📝 Transcription: {transcription}")
        
    except Exception as e:
        raise HTTPException(status_code=500, detail="Failed to save audio file")
    
    return {
        "message": "Order created successfully",
        "filename": audio_file.filename
    }

