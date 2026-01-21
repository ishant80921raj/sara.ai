#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
SARA - ALL ROUNDER ASSISTANT
Features: Math, Science, Grammar, GK, Songs, Lullabies, Stories, Emotions, Camera
"""

from brain import SARBrain

print("""
╔══════════════════════════════════════════════════════════════════════╗
║                  🌟 SARA - ALL ROUNDER ASSISTANT 🌟                  ║
║                  EMOTIONS | STORIES | SONGS | CAMERA                ║
╚══════════════════════════════════════════════════════════════════════╝

🧠 BRAIN FEATURES:
✅ Multiplication Tables (2-20)
✅ Alphabet Learning (A-Z with pronunciation)
✅ Grammar Teaching (Noun, Verb, Adjective, Tense, Sentences)
✅ General Knowledge (Capitals, Largest, How Many)
✅ Science (Gravity, Light, Sound, DNA, Planets)
✅ Math Problems (Addition, Subtraction, Multiplication, Division, Percentages, Geometry)
✅ Jokes & Humor
✅ Songs with Lyrics
✅ Lullabies (लोरी)
✅ Stories (कहानियां)
✅ Motivation & Inspiration
✅ Life Advice (Study, Health, Friends, Confidence)
✅ EMOTION DETECTION & SUPPORT
✅ 📷 CAMERA FEATURE - Emotion Detection!

""")

# Initialize brain
brain = SARBrain(api_key='invalid')

# Test some features
test_features = {
    "📊 MULTIPLICATION TABLE": "5 ka table",
    "🔤 ALPHABET": "abcd sikhao",
    "📚 GRAMMAR": "noun kya hota hai",
    "🌍 GENERAL KNOWLEDGE": "India ka capital",
    "🧮 MATH": "12 times 8",
    "🎵 SONG": "gana gao",
    "💤 LULLABY": "lori suna",
    "📖 STORY": "story suno",
    "💪 MOTIVATION": "mujhe motivate karo",
    "💔 EMOTION (SAD)": "main bahot udaas hun",
    "😊 EMOTION (HAPPY)": "main bahot khush hun",
}

print("=" * 70)
print("🧪 QUICK FEATURE TEST")
print("=" * 70 + "\n")

for feature, query in test_features.items():
    print(f"\n{feature}")
    print("-" * 70)
    print(f"Query: {query}")
    try:
        response, action, _ = brain.process_command(query)
        # Show first 200 chars
        display = response[:200] + "..." if len(response) > 200 else response
        print(f"Response: {display}")
    except Exception as e:
        print(f"Error: {e}")

print("\n\n" + "=" * 70)
print("✨ NOW LAUNCH SARA GUI! ✨")
print("=" * 70)
print("""
Command: python sara_gui_enhanced.py

Features in GUI:
✅ START/END buttons
✅ Voice input with microphone
✅ Voice output with speaker
✅ 📷 CAMERA BUTTON - NEW!
✅ Emotion detection via camera
✅ Beautiful animated SARA character
✅ Chat history display
✅ Mute/Unmute option
✅ All features above!

GET READY FOR THE BEST AI ASSISTANT! 🚀
""")
