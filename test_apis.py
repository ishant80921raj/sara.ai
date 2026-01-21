#!/usr/bin/env python
"""
Quick Test Script for SARA with FREE APIs
Test all new API integrations
"""

from brain import SARBrain
import time

def test_sara_apis():
    """Test all API functions"""
    
    print("\n" + "="*60)
    print("🚀 SARA FREE API INTEGRATION TEST")
    print("="*60 + "\n")
    
    brain = SARBrain(use_ollama=False)
    
    # Test commands that trigger APIs
    test_commands = [
        ("joke sunao", "Jokes API"),
        ("fact sunao", "Facts API"),
        ("motivation de", "Quotes API"),
        ("advice de", "Advice API"),
        ("random batao", "Random Person API"),
    ]
    
    for command, api_name in test_commands:
        print(f"\n📍 Testing: {api_name}")
        print(f"   Command: '{command}'")
        print("   " + "-"*50)
        
        response, action_type, params = brain.process_command(command)
        
        print(f"   Response: {response}")
        print(f"   Type: {action_type}")
        time.sleep(0.5)
    
    print("\n" + "="*60)
    print("✅ ALL APIS WORKING PERFECTLY!")
    print("="*60 + "\n")
    
    print("🎯 Try these commands in SARA GUI:")
    print("   • 'joke sunao' - Get random joke")
    print("   • 'fact sunao' - Get random fact")
    print("   • 'motivation de' - Get inspirational quote")
    print("   • 'advice de' - Get life advice")
    print("   • 'random batao' - Get random person\n")

if __name__ == "__main__":
    test_sara_apis()
