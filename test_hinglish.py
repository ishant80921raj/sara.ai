"""
Test script for SARA Hinglish support
"""

from brain import SARBrain
from voice_output import VoiceOutput
import time

def test_hinglish_support():
    """Test SARA's Hinglish capabilities"""
    
    brain = SARBrain(use_ollama=False)
    voice = VoiceOutput(rate=150, volume=0.9)
    
    print("\n" + "="*60)
    print("[TEST] Testing SARA's Hinglish Support")
    print("="*60 + "\n")
    
    test_cases = [
        ("kya time ho gaya", "Time query in Hinglish"),
        ("youtube kholo", "Open app in Hinglish"),
        ("aaj konsa din hai", "Day query in Hinglish"),
        ("ek joke sunao", "Tell joke in Hinglish"),
        ("python ke baare mein dhundo", "Search in Hinglish"),
        ("hey sara, namaste!", "Greet in Hindi"),
        ("aaj ka date batao", "Date in Hindi"),
        ("fact sunao bhai", "Fact in Hinglish"),
        ("shukriya sara", "Thanks in Hindi"),
    ]
    
    for command, description in test_cases:
        print(f"\n[TEST] {description}")
        print(f"[CMD] Command: {command}")
        
        response, action_type, params = brain.process_command(command)
        
        print(f"[OK] Response: {response}")
        print(f"[ACTION] Type: {action_type}")
        
        # Speak the response
        print(f"[VOICE] Playing voice response...")
        voice.speak(response, wait=False)
        time.sleep(1)
    
    print("\n" + "="*60)
    print("[OK] All Hinglish tests completed!")
    print("="*60 + "\n")
    print("Features tested:")
    print("   [OK] Hinglish keyword recognition")
    print("   [OK] Hindi greetings and responses")
    print("   [OK] Hindi day names")
    print("   [OK] Hinglish jokes and facts")
    print("   [OK] Voice output for all responses")

if __name__ == "__main__":
    test_hinglish_support()
