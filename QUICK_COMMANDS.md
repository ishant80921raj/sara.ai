# SARA 2.0 - QUICK START COMMANDS

## START SARA NOW

```bash
cd "C:\Users\Ishant_raj_2006\Desktop\SARA"
python main.py --mode voice
```

Then say: **"Hey Sara, ..."** followed by your command

---

## 30 TESTED HINGLISH COMMANDS

### Time & Date (4 commands)
```
"Hey Sara, kya time ho gaya?"              → Time in Hinglish
"Hey Sara, time batao"                     → Current time
"Hey Sara, aaj konsa din hai?"             → Day name in Hindi
"Hey Sara, aaj ka date batao"              → Date in Hindi format
```

### Open Apps/Websites (9 commands)
```
"Hey Sara, youtube kholo"                  → Opens YouTube
"Hey Sara, chrome kholo"                   → Launches Chrome
"Hey Sara, google kholo"                   → Opens Google
"Hey Sara, gmail kholo"                    → Opens Gmail
"Hey Sara, facebook kholo"                 → Opens Facebook
"Hey Sara, twitter kholo"                  → Opens Twitter
"Hey Sara, github kholo"                   → Opens GitHub
"Hey Sara, spotify kholo"                  → Opens Spotify
"Hey Sara, discord kholo"                  → Opens Discord
```

### Search (3 commands)
```
"Hey Sara, python dhundo"                  → Searches for Python
"Hey Sara, ML ke baare mein zyada jano"   → Searches for ML info
"Hey Sara, web development tutorial dhundo" → Searches web dev
```

### Fun - Jokes (3 commands)
```
"Hey Sara, ek joke sunao"                  → Tells Hinglish joke
"Hey Sara, mazak sunao"                    → Tells funny joke
"Hey Sara, maza karo"                      → Another Hinglish joke
```

### Fun - Facts (3 commands)
```
"Hey Sara, fact sunao"                     → Tells interesting fact
"Hey Sara, fact sunao bhai"                → Fact in Hinglish
"Hey Sara, kuch interesting batao"         → Fun fact
```

### Greetings (4 commands)
```
"Hey Sara, namaste!"                       → Hindi greeting reply
"Hey Sara, kaise ho?"                      → Hindi how are you
"Hey Sara, hi!"                            → English greeting
"Hey Sara, hey sara!"                      → Casual greeting
```

### Thanks (3 commands)
```
"Hey Sara, shukriya"                       → Thanks in Hindi
"Hey Sara, dhanyavaad"                     → Gratitude in Hindi
"Hey Sara, thank you"                      → English thanks
```

### Exit (2 commands)
```
"Hey Sara, ruko"                           → Stop/pause
"Hey Sara, bye"                            → Exit SARA
```

---

## TEST MODES

### Mode 1: Voice (Main Mode)
```bash
python main.py --mode voice
```
**Use:** For actual voice interactions
**How:** Say "Hey Sara" followed by commands

### Mode 2: Interactive (Text Input)
```bash
python main.py --mode interactive
```
**Use:** For testing without microphone
**How:** Type commands instead of speaking

### Mode 3: Demo (Automated)
```bash
python main.py --mode demo
```
**Use:** Watch SARA automatically
**How:** Runs 8 predefined commands

### Mode 4: Test Suite
```bash
python test_hinglish.py
```
**Use:** Verify all Hinglish features
**How:** Runs 9 comprehensive tests with voice

---

## CUSTOMIZATION

Edit `config.py` to change:

```python
# Wake words
WAKE_WORDS = ["hey sara", "ok sara"]

# Speed (words per minute)
SPEECH_RATE = 150

# Volume (0.0 to 1.0)
VOLUME = 0.9
```

---

## TROUBLESHOOTING

**Can't hear responses?**
- Check speakers are on
- Check volume is up
- Run: `python test_hinglish.py`

**Microphone not working?**
- Check microphone is connected
- Check microphone permissions
- Try interactive mode: `python main.py --mode interactive`

**Hinglish not recognized?**
- Speak clearly and loud
- Make sure microphone volume is high
- Check internet connection (for Google Speech API)

---

## QUICK REFERENCE

| Want | Say |
|------|-----|
| Know time | "kya time ho gaya" |
| Open YouTube | "youtube kholo" |
| Search Python | "python dhundo" |
| Tell joke | "joke sunao" |
| Learn fact | "fact sunao" |
| Greet | "namaste" |
| Exit | "bye" |

---

## FILE STRUCTURE

```
SARA/
├── main.py              (Main orchestrator - run this)
├── brain.py             (AI with Hinglish)
├── voice_input.py       (Speech recognition)
├── voice_output.py      (Text-to-speech)
├── actions.py           (App launching)
├── config.py            (Settings)
├── test_hinglish.py     (Test suite)
├── requirements.txt     (Dependencies)
└── docs/                (Documentation)
```

---

## INSTALLATION (First Time Only)

```bash
# Install dependencies
pip install -r requirements.txt

# That's it! SARA is ready to use
```

---

## START NOW

```bash
cd "C:\Users\Ishant_raj_2006\Desktop\SARA"
python main.py --mode voice
```

**Then say:** "Hey Sara, kya time ho gaya?"

**You should hear:** "Abhi [TIME] hai"

---

**Status:** ✓ READY TO USE
**Version:** 2.0 (Hinglish-Enabled)
**All Tests:** PASSING (9/9)
