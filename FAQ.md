# 🤔 SARA - Frequently Asked Questions (FAQ)

## General Questions

### Q1: What is SARA?
**A:** SARA (Smart Assistant for Real-time Actions) is a voice-based AI assistant similar to Google Assistant. It's built entirely with free and open-source tools, runs locally on your computer, and requires no API keys or paid subscriptions.

### Q2: Do I need to pay anything?
**A:** No! SARA is 100% free. All dependencies are free and open-source. Optional: Ollama AI is also free, just requires more disk space.

### Q3: What are the system requirements?
**A:** 
- Windows 10/11, macOS, or Linux
- Python 3.8 or higher
- Minimum 2GB RAM (4GB recommended)
- Microphone and speakers
- Internet for some features (speech recognition, web search)

### Q4: Can I use SARA offline?
**A:** Partially. SARA works offline with:
- Rule-based commands (open apps, time, jokes, etc.)
- Local LLM (Ollama) if installed
- Offline speech recognition (Vosk - requires setup)

Features requiring internet:
- Google Speech Recognition
- Web search
- Weather data
- External API calls

### Q5: How is SARA different from Google Assistant?
**A:**
- ✅ SARA: Free, offline-capable, customizable, open-source, local
- ❌ Google Assistant: Paid features, cloud-dependent, limited customization

**Similarities:**
- Natural language understanding
- Voice recognition
- App launching
- Web search
- General conversation

---

## Installation & Setup

### Q6: I'm getting "Python not found" error
**A:** 
1. Install Python from https://python.org
2. During installation, **CHECK** "Add Python to PATH"
3. Restart command prompt
4. Verify: `python --version`

### Q7: How do I create a virtual environment?
**A:**
```bash
# Navigate to SARA folder
cd C:\Users\Ishant_raj_2006\Desktop\SARA

# Create environment
python -m venv sara_env

# Activate it
sara_env\Scripts\activate
```

### Q8: "pip install -r requirements.txt" is failing
**A:**
```bash
# Make sure virtual environment is activated
# Try updating pip first
pip install --upgrade pip

# Install packages one by one
pip install SpeechRecognition==3.10.0
pip install pyttsx3==2.90
pip install requests==2.31.0
pip install python-dotenv==1.0.0

# Check what's installed
pip list
```

### Q9: Which Python version should I use?
**A:** Python 3.8, 3.9, 3.10, 3.11, or 3.12. Avoid Python 3.7 or earlier.

### Q10: Can I install SARA using pip?
**A:** Not yet! But you can:
1. Download SARA folder
2. Rename to your preferred location
3. Run directly from there
4. Future: We'll add pip package support

---

## Voice & Audio

### Q11: Microphone is not working
**A:**
1. Check hardware connection
2. Test in Settings > Sound > Input Devices
3. Grant permissions: Settings > Privacy & Security > Microphone
4. Test SARA module: `python voice_input.py`
5. Try different input device in voice_input.py

### Q12: Speech recognition accuracy is poor
**A:** Improve by:
- Speaking clearly and at normal pace
- Reducing background noise
- Using better microphone hardware
- Speaking in English or Hinglish
- Position microphone 6-12 inches away
- Use interactive mode to test: `python main.py --mode interactive`

### Q13: No audio output / TTS not working
**A:**
- **Windows:** Should work by default. Check Settings > Sound > Output
- **macOS:** System Preferences > Accessibility > Speech > Text to Speech
- **Linux:** `sudo apt install espeak` or `festival`

Test with: `python voice_output.py`

### Q14: Can I change SARA's voice to male?
**A:** Yes! Edit `voice_output.py`:
```python
voices = self.engine.getProperty('voices')
self.engine.setProperty('voice', voices[0].id)  # 0 = male, 1 = female
```

### Q15: How do I change wake words?
**A:** Edit `voice_input.py`:
```python
self.wake_words = ["hello sara", "hey ai", "my custom wake word"]
```

---

## AI & Intelligence

### Q16: Do I need Ollama for SARA to work?
**A:** No! SARA works great with rule-based logic. Ollama is optional for smarter AI responses.

### Q17: How do I install Ollama?
**A:**
1. Download from https://ollama.ai
2. Run installer
3. Open terminal: `ollama serve`
4. In another terminal: `ollama pull neural-chat`
5. Restart SARA - it auto-detects Ollama

### Q18: Which Ollama model should I use?
**A:**
| Model | Size | Speed | Intelligence |
|-------|------|-------|---------------|
| tinyllama | 600MB | ⚡⚡⚡ Fast | ⭐⭐ Basic |
| mistral | 4GB | ⚡⚡ Normal | ⭐⭐⭐⭐ Good |
| neural-chat | 4GB | ⚡⚡ Normal | ⭐⭐⭐⭐ Good |
| llama2 | 7GB | ⚡ Slower | ⭐⭐⭐⭐⭐ Excellent |

Use: `ollama pull model-name`

### Q19: "Ollama not detected" - How do I fix this?
**A:**
1. Download and install Ollama
2. Run: `ollama serve`
3. In another terminal: `ollama pull neural-chat`
4. Verify: `curl http://localhost:11434/api/tags`
5. Restart SARA

### Q20: Can I use other AI models besides Ollama?
**A:** Currently: No, but future plans include:
- OpenAI API support (optional, paid)
- Hugging Face models
- Local Llama.cpp integration
- Custom model support

---

## Commands & Features

### Q21: What commands can SARA understand?
**A:** SARA understands:
- **Time:** "What's the time?" "Tell me the date"
- **Apps:** "Open Chrome" "Open VS Code"
- **Websites:** "Open YouTube" "Go to Google"
- **Search:** "Search for Python" "Find restaurants"
- **Fun:** "Tell me a joke" "Interesting fact"
- **Chat:** "Hello" "How are you?" "Thanks"

### Q22: How do I add custom commands?
**A:** Edit `brain.py` in `process_with_rules()`:
```python
if "my command" in text:
    return "My response", "my_action", {"param": "value"}
```

### Q23: Can SARA control my smart home?
**A:** Not yet! But it's planned for Phase 2. Future support:
- Smart lights (Philips Hue, LIFX)
- Smart thermostat (Nest)
- Smart speakers
- Door locks

### Q24: Can SARA send emails?
**A:** Not yet, but it's on the roadmap for Phase 2.

### Q25: Does SARA support other languages?
**A:** Currently: English + basic Hinglish
Planned: Hindi, Spanish, French, German, etc.

---

## Troubleshooting & Errors

### Q26: "ModuleNotFoundError: No module named 'speech_recognition'"
**A:**
```bash
# Activate virtual environment first
sara_env\Scripts\activate

# Install packages
pip install -r requirements.txt
```

### Q27: "ConnectionError: Failed to connect to microphone"
**A:**
- Check microphone hardware
- Restart computer
- Test with: `python voice_input.py`
- Check audio settings

### Q28: SARA responds slowly
**A:**
- Normal latency: 1-4 seconds
- To improve:
  - Use rule-based mode (--no-ai)
  - Close other applications
  - Reduce network usage
  - Use faster internet connection

### Q29: Apps/websites not opening
**A:**
- Check app path in `actions.py`
- Verify app is installed
- Test: `python actions.py`
- Check Windows/macOS permissions

### Q30: "URLError: urlopen error [Errno 11001]"
**A:** Internet connectivity issue:
- Check internet connection
- Try again in a moment
- Check firewall settings

---

## Performance & Optimization

### Q31: SARA is using too much RAM
**A:**
- Disable Ollama AI: `python main.py --no-ai`
- Close background applications
- Restart SARA

### Q32: How can I make SARA faster?
**A:**
1. Use rule-based mode: `python main.py --mode interactive --no-ai`
2. Use lighter Ollama model: `ollama pull tinyllama`
3. Close other applications
4. Reduce network latency (faster internet)

### Q33: Can I run SARA on Raspberry Pi?
**A:** Yes! But with limitations:
- Use rule-based logic only
- Disable Ollama (requires more resources)
- Use lightweight Linux
- Requires Python 3.8+

---

## Privacy & Security

### Q34: Does SARA collect my data?
**A:** No! 
- No analytics
- No usage tracking
- No data transmission (except Google Speech API)
- All local storage optional

### Q35: How do I protect my privacy?
**A:**
- Use offline speech recognition (Vosk)
- Disable web features
- Use rule-based logic only
- Clear history: `PRIVACY["save_conversations"] = False`

### Q36: Is SARA secure?
**A:** 
- ✅ No network vulnerabilities (runs locally)
- ✅ No API keys stored
- ✅ Open-source (transparent code)
- ⚠️ Note: Google Speech API sends audio to Google

### Q37: Can I self-host SARA?
**A:** Yes! SARA runs on your machine. To share:
1. Use Flask/FastAPI for REST API
2. Create web dashboard
3. Deploy on your server
4. Future: Official cloud option planned

---

## Development & Customization

### Q38: How do I add a new action?
**A:**
1. Create method in `actions.py`
2. Add detection in `brain.py`
3. Update `main.py` to handle action
4. Test in interactive mode
5. Document in README

### Q39: Can I use SARA as a library?
**A:** Yes!
```python
from main import SARA

sara = SARA()
sara.handle_command("open YouTube")
```

### Q40: How do I contribute to SARA?
**A:**
- Report bugs on GitHub
- Suggest features
- Improve documentation
- Submit code improvements
- Test and provide feedback

---

## Frequently Asked "How to" Questions

### Q41: How do I change SARA's name?
**A:** Search and replace in all files:
- Change `"Sara"` or `"SARA"` in all .py files
- Update wake words in voice_input.py
- Update documentation

### Q42: How do I backup my SARA installation?
**A:**
```bash
# Create backup copy
robocopy SARA SARA_backup /E

# Or zip it
Compress-Archive -Path SARA -DestinationPath SARA_backup.zip
```

### Q43: How do I update SARA to latest version?
**A:**
```bash
# Download latest version
# Backup current installation
# Replace files (keep config.py if customized)
# Test thoroughly
```

### Q44: How do I uninstall SARA?
**A:**
```bash
# Just delete the SARA folder
# Uninstall Ollama if no longer needed
# Remove Python if not using for other projects
```

### Q45: Can I run multiple instances of SARA?
**A:** Not recommended. Use interactive or demo mode for testing multiple configurations.

---

## Future Features FAQ

### Q46: Will SARA support Android?
**A:** Yes, planned for Phase 3. Using React Native or Flutter.

### Q47: Will SARA have a web interface?
**A:** Yes, planned for Phase 3. Using Flask/FastAPI + React.

### Q48: Can SARA integrate with smart homes?
**A:** Yes, planned for Phase 2. Supporting Home Assistant, IFTTT, etc.

### Q49: Will SARA have premium features?
**A:** No! SARA will always be free and open-source.

### Q50: How can I stay updated on new features?
**A:** 
- Star this repository on GitHub
- Watch for releases
- Check README for updates
- Join community discussions

---

## Still Have Questions?

If you can't find the answer here:

1. **Check Documentation:**
   - README.md - Overview
   - SETUP.md - Installation
   - ARCHITECTURE.md - Design details

2. **Debug with Logs:**
   - Run in debug mode
   - Check console output
   - Enable verbose logging

3. **Test Modules:**
   - `python voice_input.py`
   - `python voice_output.py`
   - `python brain.py`
   - `python actions.py`

4. **Community Help:**
   - Create GitHub issue
   - Check existing issues
   - Start discussion

---

**Last Updated:** January 2026
**Version:** 1.0

*Hope this FAQ helps! Enjoy using SARA! 🚀*
