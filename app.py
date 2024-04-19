
import streamlit as st
from audio_processing import upload_audio, get_audio_url, transcribe_audio, poll_transcription, write_to_file

def main():
    st.title("Audio Transcription")

    # File upload
    uploaded_file = st.file_uploader("Upload audio file", type=["mp3", "wav"])

    if uploaded_file is not None:
        file_name = st.text_input("Enter file name (without extension)")

        if st.button("Transcribe"):
            st.info("Transcribing... This may take a while.")

            # Save uploaded file
            with open(file_name + ".mp3", "wb") as f:
                f.write(uploaded_file.getvalue())

            # Perform transcription
            upload_url = upload_audio(file_name + ".mp3")
            audio_url = get_audio_url(upload_url)
            transcript_id = transcribe_audio(audio_url)
            content = poll_transcription(transcript_id)

            # Display transcribed content
            st.subheader("Transcribed Content")
            st.write(content)

            # Save transcription to file and provide download link
            transcript_file = write_to_file(content, file_name)
            # st.markdown(f"Download transcribed text: [Download {file_name}.txt](data:text/plain;charset=utf-8,{transcript_file})")
            st.download_button(label="Download transcribed text", data=content, file_name=f"{file_name}.txt", mime="text/plain")
if __name__ == "__main__":
    main()
