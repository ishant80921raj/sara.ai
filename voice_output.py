# """
# Voice Output Module for SARA - SUPER FAST & SMART
# Handles text-to-speech using pyttsx3 (offline)
# WITH EMOJI SOUND REACTIONS - No reading emojis!
# """

# import pyttsx3
# import threading
# from typing import Optional
# import re

# class VoiceOutput:
#     def __init__(self, rate: int = 180, volume: float = 1.0):
#         """
#         Initialize text-to-speech engine - FAST like Google Assistant!
        
#         Args:
#             rate: Speaking rate (180+ for fast responses like Google Assistant!)
#             volume: Volume level (0.0 to 1.0) - MAX volume
#         """
#         self.engine = pyttsx3.init()
        
#         # FASTER speaking rate - like Google Assistant!
#         self.engine.setProperty('rate', rate)  # 180 = FAST!
        
#         # Set volume to maximum for clarity
#         self.engine.setProperty('volume', volume)  # Volume (0-1)
        
#         # Set voice to FEMALE - more feminine and sweet
#         voices = self.engine.getProperty('voices')
        
#         # Try to find a good feminine voice
#         female_voice = None
#         for voice in voices:
#             if 'female' in voice.name.lower() or 'woman' in voice.name.lower():
#                 female_voice = voice.id
#                 break
        
#         # If no female voice found, use the second one (usually female in most systems)
#         if female_voice:
#             self.engine.setProperty('voice', female_voice)
#         elif len(voices) > 1:
#             self.engine.setProperty('voice', voices[1].id)  # Usually female on Windows
        
#         # Emoji sound map - instead of reading emojis, make appropriate sounds!
#         self.emoji_sounds = {
#             '😂': 'ha ha ha',  # Laughing
#             '😃': 'hehe',      # Happy
#             '😊': 'teehee',    # Smiling
#             '😍': 'aww',       # Loving
#             '😘': 'mua',       # Kiss
#             '🤔': 'hmm',       # Thinking
#             '😲': 'wow',       # Surprised
#             '😱': 'aah',       # Shocked
#             '🎉': 'hurray',    # Party
#             '🔥': 'shhh',      # Fire
#             '💕': 'aww',       # Love
#             '💜': 'aww',       # Love
#             '❤️': 'aww',       # Love
#             '👍': 'yes',       # Thumbs up
#             '🎵': 'da da da',  # Music
#             '✨': 'tink',      # Sparkle
#             '⚡': 'zap',       # Lightning
#         }
        
#         print(f"🎤 SARA Voice ready! FAST mode activated! ⚡ (Like Google Assistant)")
    
#     def _clean_text(self, text: str) -> str:
#         """
#         Remove emojis from text but add their sound effects
        
#         Args:
#             text: Text with emojis
            
#         Returns:
#             Text without emojis (cleaner speech)
#         """
#         cleaned = text
#         emoji_reactions = []
        
#         # Find and replace emojis
#         for emoji, sound in self.emoji_sounds.items():
#             if emoji in cleaned:
#                 emoji_reactions.append(sound)
#                 cleaned = cleaned.replace(emoji, '')
        
#         # Also remove any other emoji-like characters
#         cleaned = re.sub(r'[^\w\s\.\!\?\,\;\:\'\"]', '', cleaned)
#         cleaned = ' '.join(cleaned.split())  # Remove extra spaces
        
#         return cleaned, emoji_reactions
    
#     def speak(self, text: str, wait: bool = True):
#         """
#         Convert text to speech and play it - FAST!
        
#         Args:
#             text: Text to speak
#             wait: If True, wait for speech to finish before returning
#         """
#         if not text or len(text.strip()) == 0:
#             return
        
#         # Clean text and get emoji sounds
#         clean_text, emoji_sounds = self._clean_text(text)
        
#         # Don't speak if text is empty after cleaning
#         if not clean_text or len(clean_text.strip()) == 0:
#             clean_text = "okay"
        
#         print(f"[SARA] {clean_text}")
        
#         self.engine.say(clean_text)
        
#         if wait:
#             self.engine.runAndWait()
        
#         # Play emoji sound effects if any
#         for sound in emoji_sounds:
#             self.engine.say(sound)
#             if wait:
#                 self.engine.runAndWait()
    
#     def speak_async(self, text: str):
#         """
#         Speak text in a separate thread (non-blocking)
        
#         Args:
#             text: Text to speak
#         """
#         thread = threading.Thread(target=self.speak, args=(text, True), daemon=True)
#         thread.start()
    
#     def stop(self):
#         """Stop current speech"""
#         self.engine.stop()
    
#     def set_rate(self, rate: int):
#         """Change speaking rate"""
#         self.engine.setProperty('rate', rate)
    
#     def set_volume(self, volume: float):
#         """Change volume level"""
#         if 0.0 <= volume <= 1.0:
#             self.engine.setProperty('volume', volume)


# class SpeechHelper:
#     """Helper class for natural speech responses"""
    
#     @staticmethod
#     def greet(hour: int) -> str:
#         """Generate appropriate greeting based on time"""
#         if hour < 12:
#             return "Good morning!"
#         elif hour < 17:
#             return "Good afternoon!"
#         elif hour < 21:
#             return "Good evening!"
#         else:
#             return "Good night!"
    
#     @staticmethod
#     def confirm_action(action: str) -> str:
#         """Generate confirmation message"""
#         confirmations = [
#             f"Okay, {action}.",
#             f"Sure thing! {action}.",
#             f"Got it! {action}.",
#             f"Done! {action}.",
#         ]
#         import random
#         return random.choice(confirmations)
    
#     @staticmethod
#     def error_response() -> str:
#         """Generate friendly error message"""
#         responses = [
#             "I'm sorry, I didn't quite understand that.",
#             "Can you say that again?",
#             "I'm not sure about that.",
#             "Let me think about that...",
#         ]
#         import random
#         return random.choice(responses)


# if __name__ == "__main__":
#     # Test voice output
#     voice = VoiceOutput()
#     print("🎙️ SARA Voice Output Test\n")
    
#     voice.speak("Hello! I'm SARA, your voice assistant.")
#     voice.speak("I can understand your commands and help you with various tasks.")
#     voice.speak("Try saying 'Hey Sara, open YouTube' or 'what's the time'")






# """
# Voice Output Module for SARA
# NEURAL TTS | SOFT GIRL VOICE | GEMINI-LIKE
# """

# import asyncio
# import edge_tts
# import os
# import threading
# import re

# class VoiceOutput:
#     def __init__(self):
#         # ⭐ BEST soft girl voices (Gemini-like)
#         self.voice = "en-US-JennyNeural"      # super soft & friendly
#         # self.voice = "en-IN-NeerjaNeural"   # Indian soft girl (optional)

#         self.rate = "-15%"     # slow = more natural
#         self.volume = "+0%"

#         # Emoji reactions (spoken naturally, not read)
#         self.emoji_sounds = {
#             '😂': 'ha ha',
#             '😃': 'hehe',
#             '😊': 'hmm',
#             '😍': 'aww',
#             '😘': 'mua',
#             '🤔': 'hmm',
#             '😲': 'wow',
#             '😱': 'oh',
#             '🎉': 'yay',
#             '🔥': 'wow',
#             '💕': 'aww',
#             '❤️': 'aww',
#             '👍': 'yes',
#         }

#         print("🎤 SARA Neural Voice Ready (Soft Girl • Gemini Style)")

#     def _clean_text(self, text: str):
#         cleaned = text
#         reactions = []

#         for emoji, sound in self.emoji_sounds.items():
#             if emoji in cleaned:
#                 reactions.append(sound)
#                 cleaned = cleaned.replace(emoji, '')

#         cleaned = re.sub(r'[^\w\s\.\!\?\,]', '', cleaned)
#         cleaned = ' '.join(cleaned.split())

#         return cleaned, reactions

#     async def _speak_async(self, text: str):
#         communicate = edge_tts.Communicate(
#             text=text,
#             voice=self.voice,
#             rate=self.rate,
#             volume=self.volume
#         )
#         await communicate.save("sara_voice.mp3")

#     def speak(self, text: str):
#         if not text or not text.strip():
#             return

#         clean_text, reactions = self._clean_text(text)

#         if not clean_text:
#             clean_text = "okay"

#         print(f"[SARA] {clean_text}")

#         asyncio.run(self._speak_async(clean_text))
#         os.system("start sara_voice.mp3")  # Windows

#         # speak emoji reactions softly
#         for r in reactions:
#             asyncio.run(self._speak_async(r))
#             os.system("start sara_voice.mp3")

#     def speak_async(self, text: str):
#         threading.Thread(
#             target=self.speak,
#             args=(text,),
#             daemon=True
#         ).start()


# # ---------------- TEST ----------------
# if __name__ == "__main__":
#     sara = VoiceOutput()
#     sara.speak("Hey, I'm Sara. How can I help you today?")
#     sara.speak("You can talk to me naturally, just like Gemini 😊")




"""
Voice Output Module for SARA
OFFLINE | SWEET FEMALE VOICE | FAST & CLEAN
Best possible feminine voice using pyttsx3 (Windows)
"""

import pyttsx3
import threading
import re

class VoiceOutput:
    def __init__(self, rate: int = 155, volume: float = 1.0):
        self.engine = pyttsx3.init()

        # Sweet + Natural speaking speed
        self.engine.setProperty('rate', rate)
        self.engine.setProperty('volume', volume)

        # -------- FORCE BEST FEMALE VOICE (WINDOWS) --------
        voices = self.engine.getProperty('voices')
        selected_voice = None

        for v in voices:
            if "zira" in v.name.lower():   # Microsoft Zira (BEST female)
                selected_voice = v.id
                break

        if selected_voice:
            self.engine.setProperty('voice', selected_voice)
        elif len(voices) > 1:
            self.engine.setProperty('voice', voices[1].id)

        # Emoji reactions (soft & cute)
        self.emoji_sounds = {
            '😂': 'ha ha ha',
            '😃': 'hehe',
            '😊': 'hmm',
            '😍': 'aww',
            '😘': 'mua',
            '🤔': 'hmm',
            '😲': 'wow',
            '😱': 'oh',
            '🎉': 'yay',
            '🔥': 'wow',
            '💕': 'aww',
            '❤️': 'aww',
            '👍': 'yes',
        }

        print("🎤 SARA Voice Ready (Sweet Female • Offline)")

    def _clean_text(self, text: str):
        cleaned = text
        reactions = []

        for emoji, sound in self.emoji_sounds.items():
            if emoji in cleaned:
                reactions.append(sound)
                cleaned = cleaned.replace(emoji, '')

        cleaned = re.sub(r'[^\w\s\.\!\?\,]', '', cleaned)
        cleaned = ' '.join(cleaned.split())

        return cleaned, reactions

    def speak(self, text: str, wait: bool = True):
        if not text or not text.strip():
            return

        clean_text, reactions = self._clean_text(text)

        if not clean_text:
            clean_text = "okay"

        print(f"[SARA] {clean_text}")
        self.engine.say(clean_text)

        if wait:
            self.engine.runAndWait()

        for r in reactions:
            self.engine.say(r)
            if wait:
                self.engine.runAndWait()

    def speak_async(self, text: str):
        threading.Thread(
            target=self.speak,
            args=(text, True),
            daemon=True
        ).start()

    def stop(self):
        self.engine.stop()

    def set_rate(self, rate: int):
        self.engine.setProperty('rate', rate)

    def set_volume(self, volume: float):
        if 0.0 <= volume <= 1.0:
            self.engine.setProperty('volume', volume)


# ---------------- TEST ----------------
if __name__ == "__main__":
    sara = VoiceOutput()
    sara.speak("Hey, I am Sara. How can I help you today?")
    sara.speak("You can say things like open YouTube or tell me the time 😊")
