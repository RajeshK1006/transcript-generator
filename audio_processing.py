import requests
import time
import assemblyai as aai 
from api_credentials import api_KEY_aai
import sys

# Set API key
api_key = api_KEY_aai
aai.settings.api_key = api_key

# API URLs
transcript_url = "https://api.assemblyai.com/v2"

# Headers
headers = {"authorization": api_key}

# Function to upload audio file
def upload_audio(file_name):
    with open(file_name, "rb") as f:
        response = requests.post(transcript_url + "/upload", headers=headers, data=f)
        response.raise_for_status()  # Raise an error for bad status codes
        upload_url = response.json()["upload_url"]
    return upload_url

# Function to get audio URL
def get_audio_url(upload_url):
    return {"audio_url": upload_url}

# Function to transcribe audio
def transcribe_audio(audio_url):
    response = requests.post(transcript_url + "/transcript", json=audio_url, headers=headers)
    response.raise_for_status()  # Raise an error for bad status codes
    transcript_id = response.json()['id']
    return transcript_id

# Function to poll for transcription result
def poll_transcription(transcript_id):
    polling_endpoint = f"https://api.assemblyai.com/v2/transcript/{transcript_id}"
    while True:
        response = requests.get(polling_endpoint, headers=headers)
        response.raise_for_status()  # Raise an error for bad status codes
        transcription_result = response.json()
        if transcription_result['status'] == 'completed':
            return transcription_result['text']
        elif transcription_result['status'] == 'error':
            raise RuntimeError(f"Transcription failed: {transcription_result['error']}")
        else:
            time.sleep(3)

# Function to write transcription result to file
def write_to_file(content, file_name):
    transcript_file = file_name + ".txt"
    with open(transcript_file, "w") as f:
        f.write(content)
    return transcript_file

# Main function
def main():
    file_name = sys.argv[1]
    upload_url = upload_audio(file_name)
    audio_url = get_audio_url(upload_url)
    transcript_id = transcribe_audio(audio_url)
    content = poll_transcription(transcript_id)
    transcript_file = write_to_file(content, file_name)
    print(f"Transcription saved to: {transcript_file}")

if __name__ == "__main__":
    main()
