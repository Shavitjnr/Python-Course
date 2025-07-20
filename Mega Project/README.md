# Jarvis Voice Assistant

A Python-based voice assistant that can perform various tasks like opening websites, playing music, getting news, and answering questions using AI.

## Features

- Voice recognition and text-to-speech
- Web browser automation
- Music playback from YouTube
- News headlines
- AI-powered responses using OpenAI
- Wake word detection ("Jarvis")

## Setup

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Set up environment variables:
   - Create a `.env` file in the project directory
   - Add your API keys:

```bash
# OpenAI API Key - Get from https://platform.openai.com/api-keys
export OPENAI_API_KEY="your_openai_api_key_here"

# News API Key - Get from https://newsapi.org/
export NEWS_API_KEY="your_news_api_key_here"
```

Or create a `.env` file:
```
OPENAI_API_KEY=your_openai_api_key_here
NEWS_API_KEY=your_news_api_key_here
```

3. Run the assistant:
```bash
python main.py
```

## Usage

1. Say "Jarvis" to wake up the assistant
2. Give commands like:
   - "Open Google"
   - "Play skyfall"
   - "What's the weather?"
   - "Tell me the news"

## Security Note

- Never commit API keys to version control
- Use environment variables for sensitive data
- The `.env` file should be added to `.gitignore`

## Files

- `main.py` - Main voice assistant application
- `client.py` - OpenAI API client example
- `musicLibrary.py` - Music library with YouTube links
- `test_songs.py` - Test script for music functionality 