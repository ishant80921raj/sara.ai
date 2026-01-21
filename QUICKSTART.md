# ⚡ SARA Quick Start Guide

**Get SARA running in 5 minutes!**

---

## Step 1: Install Python (2 minutes)

### Windows/macOS/Linux:
1. Visit: https://python.org
2. Download Python 3.10 or higher
3. Run installer
4. ✅ **CHECK:** "Add Python to PATH"
5. Click "Install Now"

**Verify installation:**
```bash
python --version
# Should show: Python 3.10.x or higher
```

---

## Step 2: Setup SARA (2 minutes)

```bash
# Navigate to SARA folder
cd C:\Users\Ishant_raj_2006\Desktop\SARA

# Create virtual environment (one-time)
python -m venv sara_env

# Activate it
sara_env\Scripts\activate

# Install packages (one-time, takes 1-2 minutes)
pip install -r requirements.txt

# Done! ✅
```

---

## Step 3: Run SARA (Choose Your Mode)

### 🎬 Option A: Demo Mode (No Microphone Needed)
```bash
python main.py --mode demo
```
**What it does:** Runs through predefined test commands automatically
**Good for:** Quick testing, no hardware needed

### ⌨️ Option B: Interactive Mode (Type Instead of Voice)
```bash
python main.py --mode interactive
```
**What it does:** Type commands instead of speaking
**Good for:** Testing, debugging, quiet environments
**Example:**
```
You: open YouTube
SARA: Opening YouTube.
```

### 🎤 Option C: Voice Mode (Full Experience)
```bash
python main.py --mode voice
```
**What it does:** Listen for "Hey Sara" wake word, then commands
**Good for:** Real voice assistant experience
**Example:**
```
You: "Hey Sara, open YouTube"
SARA: "Opening YouTube." (opens browser)
```

---

## Step 4: Try These Commands

Once SARA is running (in any mode), try:

```
Time:
- "What's the time?"
- "Tell me the date"

Apps:
- "Open Chrome"
- "Open Calculator"
- "Open VS Code"

Websites:
- "Open YouTube"
- "Open Google"
- "Open Gmail"

Search:
- "Search for Python tutorials"
- "Find restaurants near me"

Fun:
- "Tell me a joke"
- "Tell me an interesting fact"

Chat:
- "Hello!"
- "How are you?"
```

---

## Common Issues & Quick Fixes

### ❌ "Module not found" Error
```bash
# Make sure virtual environment is activated
sara_env\Scripts\activate

# Reinstall packages
pip install -r requirements.txt
```

### ❌ Microphone not working
- Check hardware connection
- Settings > Sound > Check input levels
- Try interactive mode first: `python main.py --mode interactive`

### ❌ Apps/websites not opening
- They might already be running in background
- Check firewall settings
- Try opening manually first

### ❌ No audio output
- Check speakers in Settings > Sound
- Test with: `python voice_output.py`
- Try increasing volume

---

## Next: Customize SARA (Optional)

### Change Wake Word
Edit `voice_input.py`, line ~16:
```python
self.wake_words = ["hello sara", "hey ai", "your custom phrase"]
```

### Add Your Own Apps
Edit `actions.py`, find `_setup_app_paths()`, add:
```python
"spotify": "C:\\Users\\YourName\\AppData\\Local\\Spotify\\Spotify.exe",
```

### Enable AI Mode (Optional)
1. Download Ollama: https://ollama.ai
2. Run: `ollama serve`
3. Download model: `ollama pull neural-chat`
4. Restart SARA

---

## Verify Each Component

If something's not working, test individually:

```bash
# Test text-to-speech
python voice_output.py
# You should hear: "Hello! I'm SARA..."

# Test brain logic
python brain.py
# Shows how SARA understands commands

# Test actions
python actions.py
# Tests jokes, facts, website opening

# Test microphone
python voice_input.py
# Say "Hey Sara" to test wake word
```

---

## Useful Commands

```bash
# Activate environment (every time)
sara_env\Scripts\activate

# Run SARA in different modes
python main.py --mode voice        # Voice mode (default)
python main.py --mode interactive  # Text mode
python main.py --mode demo         # Demo mode
python main.py --no-ai             # Disable AI (use rules only)

# Deactivate environment
deactivate

# Update packages
pip install --upgrade -r requirements.txt

# List installed packages
pip list

# Help/documentation
cat README.md       # Overview
cat SETUP.md        # Detailed installation
cat ARCHITECTURE.md # How SARA works
cat FAQ.md          # Frequently asked questions
```

---

## File Structure

```
SARA/
├── main.py              👈 Run this! (python main.py)
├── voice_input.py       (Microphone & speech recognition)
├── voice_output.py      (Speakers & text-to-speech)
├── brain.py             (AI & logic)
├── actions.py           (Open apps, search, etc.)
├── config.py            (Settings & customization)
├── requirements.txt     (Python packages)
├── README.md            (Full documentation)
├── SETUP.md             (Detailed installation)
├── ARCHITECTURE.md      (How it works)
└── FAQ.md               (Questions & answers)
```

---

## Troubleshooting Flowchart

```
SARA not working?
│
├─ Error message?
│  ├─ "Module not found" → pip install -r requirements.txt
│  ├─ "Microphone error" → Check hardware, try interactive mode
│  ├─ "Connection error" → Check internet, try --no-ai
│  └─ Other → Check FAQ.md
│
├─ No output sound?
│  ├─ Try: python voice_output.py
│  ├─ Check Settings > Sound > Output
│  └─ Increase volume
│
├─ Can't hear commands?
│  ├─ Try: python voice_input.py
│  ├─ Check microphone connection
│  ├─ Reduce background noise
│  └─ Try interactive mode instead
│
├─ Apps/websites won't open?
│  ├─ Check firewall
│  ├─ Try: python actions.py
│  ├─ Verify app path in config.py
│  └─ Try opening manually first
│
└─ Still stuck?
   └─ Check FAQ.md or create GitHub issue
```

---

## Success Checklist

- ✅ Python 3.8+ installed
- ✅ Virtual environment created
- ✅ Packages installed (pip install -r requirements.txt)
- ✅ Microphone connected (optional, for voice mode)
- ✅ Speakers working (optional, but recommended)
- ✅ SARA runs without errors
- ✅ Try demo mode: `python main.py --mode demo`
- ✅ Try interactive mode: `python main.py --mode interactive`
- ✅ Try voice mode (if microphone): `python main.py --mode voice`

---

## What Now?

### 🚀 Next Steps:
1. ✅ Get SARA running (you did this!)
2. 🎤 Try voice mode with your microphone
3. 🔧 Customize wake words and apps (config.py)
4. 🧠 Install Ollama for smarter AI (optional)
5. 🎯 Add custom commands (brain.py)
6. 📚 Read full documentation

### 📚 Learn More:
- **README.md** - Full features and capabilities
- **SETUP.md** - Detailed installation & troubleshooting
- **ARCHITECTURE.md** - How SARA actually works
- **FAQ.md** - 50+ common questions answered

### 🤝 Get Help:
- Check FAQ.md (most answers are there!)
- Debug with: `python main.py --mode interactive`
- Test modules individually
- Read error messages carefully

---

## Pro Tips 🎯

1. **Start with interactive mode** (`--mode interactive`)
   - Easier to test without microphone
   - Can see exactly what SARA understands

2. **Reduce background noise**
   - Speak clearly at normal pace
   - Position microphone 6-12 inches away
   - Close windows/doors to reduce noise

3. **Customize for yourself**
   - Add your favorite apps to app_paths
   - Change wake words to your preference
   - Adjust voice speed/volume in config.py

4. **Use Ollama for smarter AI**
   - Download Ollama from ollama.ai
   - Much smarter responses
   - Still 100% free and local

5. **Test each module**
   - Don't assume everything works together
   - Test voice_output.py, brain.py, actions.py separately
   - Helps identify actual issues

---

## Common Commands Quick Reference

```
Time & Date:
✓ "What's the time?"
✓ "Tell me the date"
✓ "What day is it?"

Open Apps:
✓ "Open Chrome"
✓ "Open Calculator"
✓ "Open VS Code"

Open Websites:
✓ "Open YouTube"
✓ "Open Google"
✓ "Open Gmail"

Search:
✓ "Search for Python"
✓ "Find restaurants"
✓ "Tell me about AI"

Fun:
✓ "Tell me a joke"
✓ "Tell me a fact"

Chat:
✓ "Hello!"
✓ "How are you?"
✓ "Thanks!"
```

---

## Keyboard Shortcuts

```
Ctrl+C     - Stop SARA (any mode)
Ctrl+L     - Clear screen (some terminals)
Enter      - Submit command (interactive mode)
```

---

## Need More Help?

1. **First time?** → Start with this Quick Start Guide ✅
2. **Installation issues?** → Read SETUP.md
3. **How does SARA work?** → Check ARCHITECTURE.md
4. **Can't find answer?** → Read FAQ.md (50+ questions)
5. **Something broken?** → Test individual modules
6. **Want to customize?** → Edit config.py

---

## Final Checklist Before Running

- [ ] Python 3.8+ installed
- [ ] Virtual environment activated
- [ ] `pip install -r requirements.txt` completed
- [ ] No error messages during installation
- [ ] Ready to test SARA

---

**🎉 Ready to start?**

```bash
# One command to rule them all:
python main.py --mode interactive

# Then type some commands and have fun!
```

---

**Happy coding! Enjoy SARA! 🚀**

*For detailed documentation, see README.md*
