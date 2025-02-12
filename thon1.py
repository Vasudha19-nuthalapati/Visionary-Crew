import whisper
import argparse
import os
import streamlit as st

def transcribe_audio(file_path, model_size="medium", language=None, save_to_file=False):
    """
    Transcribes an audio file using OpenAI's Whisper model.

    Parameters:
        file_path (str): Path to the audio file.
        model_size (str): Model size ("tiny", "base", "small", "medium", "large").
        language (str): Optional language hint (e.g., "en" for English).
        save_to_file (bool): Whether to save transcription to a text file.

    Returns:
        str: Transcribed text.
    """
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"File '{file_path}' not found.")

    print(f"Loading Whisper model ({model_size})...")
    model = whisper.load_model(model_size)

    print("Transcribing audio...")
    result = model.transcribe(file_path, language=language)
    transcription = result["text"]

    print("\nTranscription:\n")
    print(transcription)

    if save_to_file:
        output_file = file_path.rsplit(".", 1)[0] + "_transcription.txt"
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(transcription)
        print(f"\nTranscription saved to: {output_file}")

    return transcription

if _name_ == "_main_":
    parser = argparse.ArgumentParser(description="Whisper Audio Transcription")
    parser.add_argument("file", type=str, help="Path to the audio file")
    parser.add_argument("-m", "--model", type=str, default="medium", choices=["tiny", "base", "small", "medium", "large"], help="Model size")
    parser.add_argument("-l", "--language", type=str, default=None, help="Language code (e.g., 'en' for English)")
    parser.add_argument("-s", "--save", action="store_true", help="Save transcription to a text file")
    
    args = parser.parse_args()

    try:
        transcribe_audio(args.file, args.model, args.language, args.save)
    except Exception as e:
        print(f"Error: {e}")
        