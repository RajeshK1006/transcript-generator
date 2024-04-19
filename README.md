# Audio Transcription Streamlit App

This Streamlit app allows users to transcribe audio files (in MP3 or WAV format) into text using the AssemblyAI transcription service. Users can upload an audio file, specify a filename, and transcribe the audio. The transcribed text is then displayed on the screen, and users can download the text file if desired.

## Setup

### Installation

To install the required dependencies, run the following command:

pip install -r requirements.txt


### AssemblyAI API Key Setup

To use this app, you'll need an API key from AssemblyAI. Follow these steps to set up your API key:

1. Sign up for an account on [AssemblyAI](https://www.assemblyai.com/).
2. Once logged in, navigate to the API section of your dashboard.
3. Copy your API key.
4. Create a file named `api_credentials.py` in the project directory.
5. Inside `api_credentials.py`, define a variable named `api_KEY_aai` and assign your API key to it:

```python
# api_credentials.py

api_KEY_aai = "YOUR_API_KEY"
```

Replace "YOUR_API_KEY" with your actual API key.


Replace "YOUR_API_KEY" with your actual API key.

Usage
1.Run the Streamlit app by executing the following command:

```python
#app.py
streamlit run app.py
(based on your system the app response will differ)
```
2. The app will open in your default web browser.
3. Upload an audio file by clicking the "Upload audio file" button.
4. Enter a desired filename (without extension) in the text input field.
5. Click the "Transcribe" button to start the transcription process.
6. Once the transcription is complete, the transcribed text will be displayed on the screen.
7. Optionally, click the "Download transcribed text" button to download the transcribed text as a text file.

## Dependency

 - streamlit
 - requests
 - assemblyai


This Readme.md file provides clear instructions on setting up and using the Streamlit app, along with guidance on obtaining and setting up the AssemblyAI API key. Additionally, it lists the dependencies required for running the app.
