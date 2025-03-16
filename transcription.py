import os
import whisper
import ffmpeg

MP4_FILE = "input.mp4"  # Change this to your MP4 file path

def extract_audio(mp4_file, output_audio):
    """Extracts audio from an MP4 file using ffmpeg and saves it as a WAV file."""
    os.system(f"ffmpeg -i {mp4_file} -ac 1 -ar 16000 -q:a 0 {output_audio} -y")

def transcribe_audio(audio_file):
    """Transcribes the audio using OpenAI's Whisper model."""
    model = whisper.load_model("large")  # Use a larger model for better accuracy
    result = model.transcribe(audio_file, language='he', fp16=False)  # Set language to Hebrew
    return result["text"]

def transcribe_mp4(mp4_file):
    """Extracts audio from MP4 and transcribes it."""
    audio_file = "temp_audio.wav"
    extract_audio(mp4_file, audio_file)
    transcription = transcribe_audio(audio_file)
    os.remove(audio_file)  
    return transcription

def save_result_to_file(result, filename="output.txt"):
    """Save the result to a file."""
    with open(filename, "w", encoding="utf-8") as file:
         file.write(result)

    print(f"Result saved to {filename}")

if __name__ == "__main__":
    transcription = transcribe_mp4(MP4_FILE)
    save_result_to_file(transcription, filename="transcription.txt")
