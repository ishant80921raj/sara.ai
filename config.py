"""
Configuration File for SARA
Customize SARA's behavior here
"""

# ===== VOICE SETTINGS =====
VOICE_CONFIG = {
    "wake_words": [
        "hey sara",
        "ok sara",
        "heysara",
        "oksara"
    ],
    "speech_rate": 150,           # 100-200 (lower = slower, higher = faster)
    "volume": 0.9,                # 0.0-1.0 (0 = mute, 1 = max)
    "voice_gender": "female",     # "male" or "female" (if available)
    "listen_timeout": 10,         # Seconds to listen for command
    "phrase_time_limit": 15,      # Maximum speech duration
}

# ===== AI SETTINGS =====
AI_CONFIG = {
    "use_ollama": True,           # Use Ollama LLM if available
    "ollama_model": "neural-chat", # Model to use: neural-chat, mistral, llama2, tinyllama
    "ollama_host": "localhost",   # Ollama server host
    "ollama_port": 11434,         # Ollama server port
    "fallback_to_rules": True,    # Fallback to rule-based if AI fails
}

# ===== APP PATHS (Customize for your system) =====
APP_PATHS = {
    # Windows
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
    "vscode": "C:\\Users\\Ishant_raj_2006\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
    "calc": "calc.exe",
    "notepad": "notepad.exe",
    "mspaint": "mspaint.exe",
    
    # Add your custom apps here
    # "spotify": "C:\\Users\\YourName\\AppData\\Local\\Spotify\\Spotify.exe",
    # "discord": "C:\\Users\\YourName\\AppData\\Local\\Discord\\app-VERSION\\Discord.exe",
}

# ===== WEBSITE URLS =====
WEBSITES = {
    "youtube": "https://www.youtube.com",
    "google": "https://www.google.com",
    "whatsapp": "https://web.whatsapp.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://www.twitter.com",
    "instagram": "https://www.instagram.com",
    "gmail": "https://mail.google.com",
    "github": "https://www.github.com",
    "stackoverflow": "https://stackoverflow.com",
    "reddit": "https://www.reddit.com",
    "linkedin": "https://www.linkedin.com",
    "netflix": "https://www.netflix.com",
    "spotify": "https://open.spotify.com",
    "twitch": "https://www.twitch.tv",
    
    # Add custom websites
    # "mywebsite": "https://mywebsite.com",
}

# ===== CONVERSATION SETTINGS =====
CONVERSATION_CONFIG = {
    "keep_history": True,         # Remember conversation history
    "max_history": 20,            # Maximum conversations to remember
    "context_aware": True,        # Use context in responses
    "personality": "friendly",    # Personality type: friendly, formal, casual
}

# ===== API SETTINGS =====
API_CONFIG = {
    # Speech Recognition
    "speech_api": "google",       # "google" or "vosk" (for offline)
    
    # Weather API
    "weather_api": "open-meteo",  # Free, no API key needed
    
    # Jokes API
    "jokes_api": "api-ninjas",    # Free tier: 100 requests/day
    
    # Facts API
    "facts_api": "uselessfacts",  # Free, unlimited
}

# ===== LOGGING SETTINGS =====
LOG_CONFIG = {
    "enable_logging": True,
    "log_file": "sara.log",
    "log_level": "INFO",          # DEBUG, INFO, WARNING, ERROR
    "log_voice_input": False,     # Log voice commands (privacy)
}

# ===== BEHAVIOR SETTINGS =====
BEHAVIOR_CONFIG = {
    "auto_greet": True,           # Greet user on startup
    "confirm_actions": True,      # Say "I'm opening..." before executing
    "error_responses": True,      # Say error messages
    "typing_delay": 0.05,         # Delay between characters (for demo mode)
}

# ===== CUSTOM COMMANDS =====
# Add your own custom commands here
CUSTOM_COMMANDS = {
    "test command": {
        "triggers": ["test"],
        "response": "This is a test response",
        "action": None
    },
    # Example:
    # "play music": {
    #     "triggers": ["play music", "play song"],
    #     "response": "Playing your favorite music",
    #     "action": "open_spotify"
    # }
}

# ===== GREETINGS BY TIME =====
GREETINGS = {
    "morning": "Good morning! I'm SARA, your voice assistant. How can I help?",
    "afternoon": "Good afternoon! Ready to assist you.",
    "evening": "Good evening! How can I help?",
    "night": "Good night! I'm here if you need anything.",
}

# ===== FAREWELL MESSAGES =====
FAREWELLS = [
    "Goodbye! See you soon!",
    "See you later!",
    "Bye! Have a great day!",
    "Take care!",
]

# ===== ERROR MESSAGES =====
ERROR_MESSAGES = {
    "not_understood": "I'm sorry, I didn't quite understand that. Can you say it again?",
    "no_audio": "I didn't hear anything. Try again.",
    "api_error": "I'm having trouble with that right now. Please try again later.",
    "app_not_found": "I couldn't find that application.",
    "unknown_command": "I'm not sure about that.",
}

# ===== FEATURE FLAGS =====
FEATURES = {
    "enable_voice_input": True,
    "enable_voice_output": True,
    "enable_ai": True,
    "enable_web_search": True,
    "enable_app_launch": True,
    "enable_jokes": True,
    "enable_facts": True,
    "enable_weather": True,
    "enable_music": True,
}

# ===== DEBUG SETTINGS =====
DEBUG = {
    "verbose": False,             # Print detailed logs
    "show_waveform": False,       # Show audio waveform (requires matplotlib)
    "test_mode": False,           # Run in test mode
    "simulate_network": False,    # Simulate network delays
}

# ===== PERFORMANCE SETTINGS =====
PERFORMANCE = {
    "use_cache": True,            # Cache API responses
    "cache_duration": 3600,       # Cache duration in seconds
    "parallel_processing": True,  # Use threading for parallel tasks
    "low_power_mode": False,      # Reduce CPU usage (slower but efficient)
}

# ===== PRIVACY SETTINGS =====
PRIVACY = {
    "save_conversations": False,  # Save chat history to disk
    "anonymize_logs": True,       # Don't log user names/emails
    "clear_on_exit": True,        # Clear memory on exit
    "use_offline_only": False,    # Disable all online features
}

# ===== SYSTEM SETTINGS =====
SYSTEM = {
    "auto_update": False,         # Auto-update SARA (future)
    "check_updates": True,        # Check for updates on startup
    "telemetry": False,           # Send usage data (respects privacy)
    "crash_reporting": True,      # Report crashes (optional)
}

# ===== HOTKEYS (Future Feature) =====
HOTKEYS = {
    # Not implemented yet, for future use
    "toggle_listening": "Ctrl+Shift+S",
    "open_settings": "Ctrl+Shift+,",
    "quick_command": "Ctrl+Shift+;",
}


def get_config(key: str, default=None):
    """
    Safely get configuration value
    
    Usage:
        speech_rate = get_config("speech_rate", 150)
    """
    config_name = key.upper()
    
    if config_name in globals():
        return globals()[config_name]
    return default


def load_custom_config(filepath: str):
    """
    Load configuration from external file (future feature)
    """
    # TODO: Implement loading from JSON/YAML file
    pass


if __name__ == "__main__":
    # Print all configuration
    print("🎙️ SARA Configuration")
    print("=" * 60)
    
    import json
    config = {
        "voice": VOICE_CONFIG,
        "ai": AI_CONFIG,
        "apps": list(APP_PATHS.keys()),
        "websites": list(WEBSITES.keys()),
        "features": FEATURES,
    }
    
    print(json.dumps(config, indent=2))
