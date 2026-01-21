#!/bin/bash
# Quick Start Guide for SARA with Hinglish Support

## 🚀 START SARA IN VOICE MODE

```bash
cd /path/to/SARA
python main.py --mode voice
```

Then say: **"Hey Sara, ..."** followed by your command

---

## 💬 EXAMPLE HINGLISH COMMANDS

### Time & Date
```
"Hey Sara, kya time ho gaya?"         → "Abhi 11:47 PM hai"
"Hey Sara, aaj konsa din hai?"        → "Aaj Mangalvar (Tuesday) hai"
"Hey Sara, aaj ka date batao"         → "Aaj ka date Tuesday, January 20, 2026 hai"
```

### Open Apps/Websites
```
"Hey Sara, youtube kholo"             → "youtube ko open kar raha hoon"
"Hey Sara, chrome kholo"              → "Opening chrome for you"
"Hey Sara, google kholo"              → "Google ko open kar raha hoon"
```

### Search
```
"Hey Sara, python ke baare mein dhundo"      → "Searching for python..."
"Hey Sara, machine learning search karo"     → "Searching for machine learning..."
"Hey Sara, zyada jano python tutorials"      → "Tell me about python tutorials"
```

### Fun
```
"Hey Sara, ek joke sunao"             → [Hinglish joke + SPOKEN]
"Hey Sara, mazak sunao"               → [Hinglish joke + SPOKEN]
"Hey Sara, fact sunao bhai"           → [Interesting fact + SPOKEN]
"Hey Sara, kuch interesting batao"    → [Fun fact + SPOKEN]
```

### Greetings
```
"Hey Sara, namaste!"                  → "Namaste! Kaise ho? Kya help chahiye?"
"Hey Sara, hi kaise ho?"              → "Hi there! Kaise hoon tu?"
"Hey Sara, hey!"                      → "Hey! What's up?"
```

### Thanks
```
"Hey Sara, shukriya"                  → "Bilkul! Aur bataaa"
"Hey Sara, thank you"                 → "Bilkul! Khushi se help kar raha hoon"
"Hey Sara, dhanyavaad"                → "Swagat hai! Aur kuch chahiye?"
```

---

## 🧪 TEST MODES

### Interactive Mode (Text Input)
```bash
python main.py --mode interactive
```
Type commands instead of speaking them. Great for testing!

### Demo Mode (Automated)
```bash
python main.py --mode demo
```
Watch SARA automatically process 8 predefined commands.

### Test Hinglish Features
```bash
python test_hinglish.py
```
Runs comprehensive tests of all Hinglish support features.

---

## 🎯 WHAT'S NEW IN VERSION 2.0

✅ **Voice Output for EVERY response** - No silent replies!
✅ **Hinglish Support** - Understands Hindi + English mix
✅ **Natural Responses** - Multiple random responses for variety
✅ **Hindi Day Names** - Shows days like "Somvar", "Mangalvar"
✅ **Hinglish Jokes** - 5 funny jokes in Hinglish
✅ **Hinglish Facts** - 6 interesting facts in Hinglish
✅ **Smart Intent Detection** - Understands Hinglish commands
✅ **Conversation History** - Remembers last 10 commands

---

## 📋 SYSTEM REQUIREMENTS

- Python 3.8+
- Microphone (for voice input)
- Speakers (for voice output)
- Internet (for Google Speech API and web search)

### Install Dependencies
```bash
pip install -r requirements.txt
```

**Required packages:**
- SpeechRecognition==3.10.0
- pyttsx3==2.90
- requests==2.31.0
- python-dotenv==1.0.0

---

## 🔧 CUSTOMIZATION

Edit `config.py` to customize:

```python
# Wake words
WAKE_WORDS = ["hey sara", "ok sara", "heysara", "oksara"]

# Voice settings
SPEECH_RATE = 150  # Words per minute (adjust speed)
VOLUME = 0.9       # 0.0 to 1.0

# Voice gender (if multiple voices available)
VOICE_GENDER = "female"
```

---

## 🐛 TROUBLESHOOTING

### SARA not responding?
1. Check microphone is connected
2. Run: `python test_hinglish.py` to test voice system
3. Make sure you say "Hey Sara" clearly

### Can't hear voice responses?
1. Check speakers are enabled
2. Ensure volume is not muted
3. Restart SARA: `python main.py --mode voice`

### Google Speech API not working?
1. Check internet connection
2. Make sure Google can be accessed from your location
3. Try the interactive mode instead: `python main.py --mode interactive`

---

## 🎤 VOICE SYSTEM STATUS

✅ **Microphone Detection** - Working
✅ **Speech Recognition** - Google Speech API accessible
✅ **Text-to-Speech** - pyttsx3 confirmed producing audio
✅ **Wake Word Detection** - Listening for "Hey Sara"
✅ **Voice Output** - All responses spoken

---

## 📞 SUPPORT

For issues or suggestions:
1. Check the error message
2. Try the test suite: `python test_hinglish.py`
3. Review config.py settings
4. Check internet connection

---

**SARA Version:** 2.0 (Hinglish-Enabled)
**Status:** ✅ PRODUCTION READY
**Last Updated:** January 20, 2026

Enjoy your voice assistant! 🎉
