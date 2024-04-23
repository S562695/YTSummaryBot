import streamlit as st
from main import summarize_youtube_video

def main():
    st.title("YouTube Video Summarizer")

    # Input box for YouTube URL
    youtube_url = st.text_input("Enter YouTube URL")

    # Submit button
    if st.button("Summarize") and youtube_url:
        # Summarize the YouTube video
        summarization_result = summarize_youtube_video(youtube_url)
        
        # Display the summarized text
        for i, summary in enumerate(summarization_result):
            st.write(f"Chunk {i+1}:")
            st.write(summary)

if __name__ == "__main__":
    main()
