# 🚀 SARA Setup & Installation Guide

## Complete Step-by-Step Installation

### Step 1: Prerequisites Check

**Check Python Version:**
```bash
python --version
# Required: Python 3.8 or higher
```

**Check System Requirements:**
- RAM: Minimum 2GB (4GB recommended, 8GB if using Ollama)
- Storage: 500MB for SARA + dependencies
- Microphone: Required for voice input
- Speakers: Required for voice output
- Internet: Required for some features (speech recognition, web search)

---

### Step 2: Create Virtual Environment

**On Windows:**
```bash
cd C:\Users\Ishant_raj_2006\Desktop\SARA

# Create virtual environment
python -m venv sara_env

# Activate environment
sara_env\Scripts\activate

# You should see (sara_env) in your terminal
```

**On macOS/Linux:**
```bash
cd ~/path/to/SARA

# Create virtual environment
python3 -m venv sara_env

# Activate environment
source sara_env/bin/activate
```

---

### Step 3: Install Dependencies

```bash
# Upgrade pip first
pip install --upgrade pip

# Install all required packages
pip install -r requirements.txt

# Verify installation
python -c "import speech_recognition; import pyttsx3; print('✅ All dependencies installed!')"
```

**Expected Packages:**
- SpeechRecognition (3.10.0+)
- pyttsx3 (2.90+)
- requests (2.31.0+)
- python-dotenv (1.0.0+)

---

### Step 4: Test Individual Modules

**Test 1: Voice Output (TTS)**
```bash
python voice_output.py
# You should hear: "Hello! I'm SARA, your voice assistant."
```

**Test 2: Brain Logic**
```bash
python brain.py
# Tests various commands without voice
```

**Test 3: Actions**
```bash
python actions.py
# Tests opening apps, searching, jokes, etc.
```

**Test 4: Voice Input**
```bash
python voice_input.py
# Listens for "Hey Sara" activation
```

---

### Step 5: Run SARA

**Mode 1: Demo Mode (No Microphone Needed)**
```bash
python main.py --mode demo
# Runs through predefined test commands
```

**Mode 2: Interactive Mode (Type Instead of Speak)**
```bash
python main.py --mode interactive
# Type commands instead of speaking
# Great for testing without microphone
```

**Mode 3: Voice Mode (Full Voice Experience)**
```bash
python main.py --mode voice
# Listens for "Hey Sara" or "Ok Sara"
# Requires working microphone
```

---

## Optional: Setup AI Mode (Ollama)

### Why Use Ollama?
- 🧠 Smarter responses using local AI
- 🔒 Complete privacy (no cloud)
- ⚡ Fast responses (after initial download)
- 🆓 100% free and open-source

### Install Ollama

1. **Download Ollama**
   - Visit: https://ollama.ai
   - Download for your OS (Windows/macOS/Linux)
   - Run the installer

2. **Launch Ollama Server**
   
   **Option A: Command Line (Recommended)**
   ```bash
   # Open a terminal and run
   ollama serve
   # Keep this terminal open
   ```
   
   **Option B: GUI Application**
   - Ollama should be in your applications
   - Double-click to start (runs in background)

3. **Download a Model**
   
   Open another terminal and run:
   ```bash
   # Download neural-chat (7B model, ~4GB)
   ollama pull neural-chat
   
   # Or try lighter models:
   # ollama pull mistral          # 7B, 4GB
   # ollama pull openhermes       # 7B, 4GB
   # ollama pull tinyllama        # 1B, 600MB (very fast but less smart)
   ```

4. **Verify Ollama is Running**
   
   ```bash
   # In another terminal, test the connection
   curl http://localhost:11434/api/tags
   
   # You should see your models listed
   ```

5. **Run SARA with AI**
   
   ```bash
   # Ollama will be auto-detected
   python main.py --mode interactive
   
   # Or disable AI and use rule-based logic
   python main.py --mode interactive --no-ai
   ```

---

## Customization Guide

### Change Wake Words

Edit `voice_input.py`:
```python
# Around line 16
self.wake_words = [
    "hey sara",
    "ok sara",
    "hello sara",  # Add your custom wake word
    "heysara"
]
```

### Change Voice Properties

Edit `voice_output.py`:
```python
# Around line 20
self.engine.setProperty('rate', 150)      # Speed: lower = slower, higher = faster
self.engine.setProperty('volume', 0.9)    # Volume: 0.0 to 1.0

# Change voice gender (if available)
voices = self.engine.getProperty('voices')
# voices[0] = Male voice
# voices[1] = Female voice (default)
self.engine.setProperty('voice', voices[1].id)
```

### Add New App to Open

Edit `actions.py`, find `_setup_app_paths()` method:

```python
# Windows example
self.app_paths = {
    "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
    "vscode": "C:\\Your\\Custom\\Path\\Code.exe",  # Add your app here
    "spotify": "C:\\Users\\YourName\\AppData\\Local\\Spotify\\Spotify.exe",
}
```

To find an app's path:
1. Right-click on app shortcut
2. Click "Properties"
3. Copy path from "Target" field
4. Add to app_paths dictionary

### Add New Website

Edit `brain.py`, find `detect_open_command()` method:

```python
apps_websites = {
    # ... existing websites ...
    "twitch": ("website", "twitch"),  # Add this
    "reddit": ("website", "reddit"),  # Add this
}
```

Or edit in `actions.py`:
```python
self.website_urls = {
    "youtube": "https://www.youtube.com",
    "twitch": "https://www.twitch.tv",  # Add custom URL
}
```

---

## Troubleshooting Guide

### Problem: "No module named 'speech_recognition'"

**Solution:**
```bash
# Make sure virtual environment is activated
sara_env\Scripts\activate  # Windows
source sara_env/bin/activate  # macOS/Linux

# Reinstall packages
pip install --upgrade pip
pip install -r requirements.txt
```

---

### Problem: "Microphone not detected"

**Windows:**
```bash
# Check audio devices
python -c "import pyaudio; print(pyaudio.PyAudio().get_device_count())"

# If no devices, restart PC and check Settings > Sound > Input
```

**macOS:**
```bash
# Grant microphone permissions
# System Preferences > Security & Privacy > Microphone > Allow
```

**Linux:**
```bash
# Install audio tools
sudo apt-get install python3-pyaudio pulseaudio

# Check devices
pactl list short sources
```

---

### Problem: "Speech recognition timeout"

**Possible Causes:**
1. Microphone not working
2. Too quiet or too much background noise
3. Speaking too slowly
4. Network connectivity issue

**Solutions:**
```bash
# Test microphone volume
python voice_input.py

# Try interactive mode first
python main.py --mode interactive

# Reduce ambient noise during listening
# Speak clearly and at normal pace
```

---

### Problem: "TTS not working / No audio output"

**Windows:**
```bash
# Should work out of the box
# Check: Settings > Sound > Output devices
python voice_output.py  # Test audio
```

**macOS:**
```bash
# May need to install voices
# System Preferences > Accessibility > Speech > Text to Speech

# Test with
python voice_output.py
```

**Linux:**
```bash
# Install espeak
sudo apt-get install espeak

# Or try festival
sudo apt-get install festival

# Test with
python voice_output.py
```

---

### Problem: "Ollama not detected (using rule-based only)"

**Solution:**
```bash
# 1. Download and install Ollama from ollama.ai
# 2. Open terminal and run:
ollama serve

# 3. In another terminal, verify:
curl http://localhost:11434/api/tags

# 4. Download a model:
ollama pull neural-chat

# 5. Restart SARA - it will now detect Ollama
```

---

### Problem: "Actions not executing (apps/websites not opening)"

**For Websites:**
- Works with default browser
- Check internet connection
- Verify website name is correct

**For Applications:**
```bash
# Check if app path is correct
# For Windows: Find app via Settings > Apps > Apps & Features
# Copy installation path
# Update app_paths in actions.py

# Common paths:
# Chrome: C:\Program Files\Google\Chrome\Application\chrome.exe
# VS Code: C:\Users\YourName\AppData\Local\Programs\Microsoft VS Code\Code.exe
# Firefox: C:\Program Files\Mozilla Firefox\firefox.exe
```

---

### Problem: "ImportError: No module named 'requests'"

```bash
# Reinstall with verbose output
pip install -r requirements.txt -v

# If still fails, install individually
pip install requests==2.31.0
pip install SpeechRecognition==3.10.0
pip install pyttsx3==2.90
```

---

## Performance Optimization

### For Low-End Systems (2GB RAM)

```bash
# Disable Ollama AI (use rule-based only)
python main.py --mode interactive --no-ai

# This reduces memory usage by ~90%
```

### For Better Accuracy

```bash
# Use in quiet environment
# Speak clearly at normal pace
# Position microphone 6-12 inches away

# For speech recognition improvement:
# - Better microphone hardware
# - Reduce background noise
# - Speak standard English/Hindi
```

### For Faster Response

```bash
# Use lighter models in Ollama
ollama pull tinyllama  # ~600MB, very fast

# Or use rule-based only (--no-ai flag)
```

---

## Backup & Restore

### Backup Your Configuration

```bash
# Backup entire SARA folder
robocopy SARA SARA_backup /E /V  # Windows

# Or create zip file
Compress-Archive -Path SARA -DestinationPath SARA_backup.zip  # PowerShell
```

### Backup Ollama Models

```bash
# Ollama models location:
# Windows: C:\Users\{username}\.ollama\models
# macOS: ~/.ollama/models
# Linux: ~/.ollama/models

# Backup manually or use:
ollama list  # See all installed models
```

---

## Uninstall & Cleanup

```bash
# Deactivate virtual environment
deactivate

# Delete virtual environment (safe)
rmdir sara_env /s  # Windows
rm -rf sara_env    # macOS/Linux

# To reinstall: just run Step 2 and 3 again

# To uninstall Ollama:
# Windows: Add/Remove Programs > Ollama
# macOS: Drag Ollama to Trash
# Linux: sudo apt remove ollama
```

---

## Getting Help

### Debug Mode

```bash
# Run with verbose output
python main.py --mode interactive

# Check logs/errors in console
# Note what error messages appear
```

### Check System Info

```bash
# Create diagnostics script
python -c "
import sys
import platform
import speech_recognition as sr
import pyttsx3

print('Python:', sys.version)
print('OS:', platform.platform())
print('Speech Recognition:', sr.__version__)
print('pyttsx3: OK')
print('Microphones:', sr.Microphone.list_microphone_indexes())
"
```

### Common Error Messages

| Error | Cause | Solution |
|-------|-------|----------|
| `ModuleNotFoundError: No module named 'speech_recognition'` | Package not installed | `pip install -r requirements.txt` |
| `ConnectionError: Failed to connect to microphone` | Microphone not available | Check hardware, restart, try another device |
| `URLError: urlopen error [Errno 11001]` | No internet connection | Connect to internet for speech recognition |
| `OSError: No module named 'pyttsx3'` | TTS not installed | `pip install pyttsx3==2.90` |
| `Requests: ConnectionError` | Network issue | Check internet, retry |

---

## Next Steps

1. ✅ **Installation Complete** - All modules ready
2. 📝 **Try Demo** - `python main.py --mode demo`
3. ⌨️ **Try Interactive** - `python main.py --mode interactive`
4. 🎤 **Try Voice** - `python main.py --mode voice`
5. 🧠 **Optional AI** - Install Ollama and try smart responses
6. 🔧 **Customize** - Add wake words, apps, websites
7. 🚀 **Extend** - Add new features and capabilities

---

## Useful Commands Reference

```bash
# Activate environment
sara_env\Scripts\activate  # Windows

# View installed packages
pip list

# Update packages
pip install --upgrade -r requirements.txt

# Check Python packages
python -m pip check

# Run specific test
python voice_output.py
python brain.py
python actions.py
python voice_input.py

# Run SARA
python main.py                      # Voice mode (default)
python main.py --mode interactive   # Text mode
python main.py --mode demo          # Demo mode
python main.py --no-ai              # Disable AI

# Ollama commands
ollama serve                         # Start Ollama server
ollama pull neural-chat              # Download model
ollama list                          # List models
ollama rm neural-chat                # Remove model
```

---

**Happy coding! Enjoy using SARA! 🚀**

For more help, check README.md or ARCHITECTURE.md
