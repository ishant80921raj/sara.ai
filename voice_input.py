"""
Voice Input Module for SARA
Handles speech recognition and wake word detection
"""

import speech_recognition as sr
import threading
import time
from typing import Optional, Callable

class VoiceInput:
    def __init__(self):
        self.recognizer = sr.Recognizer()
        self.microphone = sr.Microphone()
        self.is_listening = False
        self.wake_words = ["hey sara", "ok sara", "heysara", "oksara"]
        
    def listen_for_audio(self, timeout: int = 10) -> Optional[str]:
        """
        Listen to microphone and return recognized speech as text
        
        Args:
            timeout: Maximum time to listen in seconds
            
        Returns:
            Recognized text or None if failed
        """
        try:
            with self.microphone as source:
                print("🎤 Listening...")
                # Adjust for ambient noise
                self.recognizer.adjust_for_ambient_noise(source, duration=1)
                
                # Listen for audio
                audio = self.recognizer.listen(source, timeout=timeout, phrase_time_limit=15)
            
            # Recognize speech using Google Speech Recognition (free)
            print("🤔 Processing speech...")
            text = self.recognizer.recognize_google(audio, language='en-IN')
            return text.lower()
            
        except sr.UnknownValueError:
            print("❌ Could not understand audio")
            return None
        except sr.RequestError as e:
            print(f"❌ Speech service error: {e}")
            return None
        except sr.WaitTimeoutError:
            print("⏱️ No speech detected")
            return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def detect_wake_word(self, text: str) -> bool:
        """
        Check if wake word is detected in text
        
        Args:
            text: Text to check for wake words
            
        Returns:
            True if wake word found, False otherwise
        """
        if not text:
            return False
        return any(wake_word in text for wake_word in self.wake_words)
    
    def listen_for_command(self) -> Optional[str]:
        """
        Listen for wake word, then listen for command
        
        Returns:
            Command text or None if failed
        """
        while True:
            text = self.listen_for_audio(timeout=5)
            
            if text and self.detect_wake_word(text):
                print("✅ SARA Activated!")
                print("🎤 Listening for command...")
                
                # Listen for actual command
                command = self.listen_for_audio(timeout=10)
                if command:
                    # Remove wake word if present
                    for wake_word in self.wake_words:
                        if wake_word in command:
                            command = command.replace(wake_word, "").strip()
                    return command
                else:
                    print("Say command again please!")
            else:
                print("Waiting for wake word...")
    
    def start_continuous_listening(self, callback: Callable) -> threading.Thread:
        """
        Start continuous listening in a separate thread
        
        Args:
            callback: Function to call with each detected command
            
        Returns:
            Thread object
        """
        def listen_loop():
            self.is_listening = True
            while self.is_listening:
                command = self.listen_for_command()
                if command:
                    callback(command)
        
        thread = threading.Thread(target=listen_loop, daemon=True)
        thread.start()
        return thread
    
    def stop_listening(self):
        """Stop continuous listening"""
        self.is_listening = False


if __name__ == "__main__":
    # Test voice input
    voice = VoiceInput()
    print("🎙️ SARA Voice Input Test")
    print("Say 'Hey Sara' to activate...\n")
    
    try:
        while True:
            command = voice.listen_for_command()
            if command:
                print(f"📝 Command received: {command}")
    except KeyboardInterrupt:
        print("\n👋 Stopping voice input...")


