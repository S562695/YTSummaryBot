from transformers import pipeline
from youtube_transcript_api import YouTubeTranscriptApi

def summarize_youtube_video(video_url):
    # Extract video ID from YouTube URL
    video_id = video_url.split("=")[-1]

    # Get transcript of the YouTube video
    transcript = YouTubeTranscriptApi.get_transcript(video_id)
    
    # Combine transcript into a single text
    result = ""
    for i in transcript:
        result += ' ' + i['text']

    # Initialize summarization pipeline
    summarizer = pipeline('summarization')

    # Split text into chunks and summarize each chunk
    summarized_text = []
    num_iters = int(len(result)/1000)
    for i in range(0, num_iters + 1):
        start = i * 1000
        end = (i + 1) * 1000
        chunk = result[start:end]
        summarized_chunk = summarizer(chunk)[0]['summary_text']
        summarized_text.append(summarized_chunk)

    return summarized_text
