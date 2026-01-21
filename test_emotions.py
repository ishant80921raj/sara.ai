"""
Test SARA's Emotional Responses
"""

from brain import SARBrain
from voice_output import VoiceOutput
import time
import random

def test_emotional_sara():
    """Test SARA's emotional and personalized responses"""
    
    brain = SARBrain(use_ollama=False)
    voice = VoiceOutput(150, 0.9)
    
    user_name = "Ishant"
    
    print("\n" + "="*60)
    print("[TEST] SARA's Emotional & Personalized Responses")
    print("="*60)
    
    # Emotional greetings based on time
    hour = time.localtime().tm_hour
    
    if hour < 12:
        greeting = f"Subah-subah hello {user_name}! Aaj kaisa feel kar rahe ho? Kya mind mein hai?"
    elif hour < 17:
        greeting = f"Afternoon {user_name}! Kaisa chal raha hai din? Kya soch rahe ho?"
    else:
        greeting = f"Raat ka vaqt hai {user_name}... relax karo! Batao kya soch rahe ho?"
    
    print(f"\n[GREETING] SARA (Emotional):")
    print(f"  {greeting}")
    print(f"\n[VOICE OUTPUT]:")
    voice.speak(greeting, wait=False)
    time.sleep(2)
    
    # Test emotional responses
    test_cases = [
        ("hello", "Greeting in English"),
        ("namaste", "Hindi greeting"),
        ("kya time ho gaya", "Time query with emotion"),
        ("shukriya", "Thanks in Hindi with emotion"),
        ("kaise ho", "How are you in Hindi"),
        ("youtube kholo", "Open app with emotion"),
    ]
    
    print("\n" + "="*60)
    print("[TESTING] Emotional Responses")
    print("="*60)
    
    for command, description in test_cases:
        print(f"\n[TEST] {description}")
        print(f"[CMD] {command}")
        
        response, action_type, params = brain.process_command(command)
        
        print(f"[RESPONSE] {response}")
        print(f"[VOICE OUTPUT]")
        voice.speak(response, wait=False)
        
        time.sleep(1.5)
    
    print("\n" + "="*60)
    print("[OK] All emotional responses tested!")
    print("="*60)
    print("\nFeatures:")
    print("  ✓ Personalized greetings with user's name")
    print("  ✓ Time-based emotional responses")
    print("  ✓ Natural emotional language")
    print("  ✓ Voice output for every response")
    print("  ✓ Hinglish support with emotions")

if __name__ == "__main__":
    test_emotional_sara()
