"""
SARA - Smart Assistant for Real-time Actions
Main orchestrator module
"""

import sys
from voice_input import VoiceInput
from voice_output import VoiceOutput
from brain import SARBrain
from actions import ActionExecutor
from datetime import datetime
import time

class SARA:
    """
    SARA Assistant - Main class that coordinates all modules with emotions!
    """
    
    def __init__(self, enable_ai: bool = True, user_name: str = "Ishant"):
        """
        Initialize SARA with personalization
        
        Args:
            enable_ai: Use AI if Ollama is available
            user_name: User's name for personalized greetings
        """
        self.user_name = user_name
        
        print("=" * 60)
        print("[SARA] Smart Assistant for Real-time Actions")
        print("=" * 60)
        print()
        
        # Initialize all modules
        print("Initializing modules...")
        self.voice_input = VoiceInput()
        self.voice_output = VoiceOutput(rate=150, volume=0.9)
        self.brain = SARBrain(use_ollama=enable_ai)
        self.action_executor = ActionExecutor()
        
        print("All systems ready!\n")
        
        # Emotional greeting based on time
        self.greet_with_emotion()
        
        print(f"\nTips:")
        print(f"  - Say 'Hey Sara' to activate")
        print(f"  - Try: 'Hey Sara, kya time ho gaya?'")
        print(f"  - Try: 'Hey Sara, youtube kholo'")
        print(f"  - Try: 'Hey Sara, ek joke sunao'\n")
    
    def greet_with_emotion(self):
        """Greet user with emotional and personalized message"""
        import random
        
        hour = datetime.now().hour
        
        # Time-based emotional greeting
        if hour < 6:
            greetings = [
                f"Raat ka samay hai {self.user_name}... tum abhi bhi jaag rahe ho? Mujhe batao kya soch rahe ho?",
                f"Hello {self.user_name}, raat ke 3 baje... kya kaam kar rahe ho?",
            ]
        elif hour < 12:
            greetings = [
                f"Subah-subah hello {self.user_name}! Aaj kaisa feel kar rahe ho?",
                f"Good morning {self.user_name}! Ummeedo ke saath din shuru karte hain! Kya on your mind?",
                f"{self.user_name}! Nayi subah, nayi shuru... batao kya soch rahe ho?",
            ]
        elif hour < 17:
            greetings = [
                f"Afternoon {self.user_name}! Kaisa chal raha hai din? Kya mind mein hai?",
                f"Hello {self.user_name}, deen ka behtareen samay! Suno mera... kya chakkar hai?",
            ]
        elif hour < 21:
            greetings = [
                f"Shaam ka vaqt hai {self.user_name}... relax karo! Batao kya soch rahe ho?",
                f"Good evening {self.user_name}! Thak gaye na? Mujhe sab bataa... kya on your mind?",
            ]
        else:
            greetings = [
                f"Raat-pur ka samay, lekin tum yahan ho {self.user_name}! Suno mera, kya chakkar hai apke mind mein?",
                f"Late night {self.user_name}... khud se poocho kya soch rahe ho? Main sunta hoon!",
            ]
        
        # Select random greeting
        greeting = random.choice(greetings)
        
        # Speak the greeting - wait=True to ensure it completes
        print(f"\n[GREETING] {greeting}")
        self.voice_output.speak(greeting, wait=True)  # Wait for greeting to finish before continuing
    
    def handle_command(self, command: str):
        """
        Process and execute a command
        
        Args:
            command: User command text
        """
        if not command:
            return
        
        print(f"\n👤 Command: {command}")
        
        # Process with brain
        response, action_type, action_params = self.brain.process_command(command)
        
        # Execute action if needed
        if action_type not in ["conversation", "time", "date", "unknown"]:
            self.action_executor.execute(action_type, action_params)
        
        # Special handling for some action types
        if action_type == "joke":
            response = self.action_executor.tell_joke()
        elif action_type == "fact":
            response = self.action_executor.tell_fact()
        elif action_type == "weather":
            response = self.action_executor.tell_weather()
        
        # ALWAYS speak response out loud
        print(f"[RESPONSE] {response}")
        self.voice_output.speak(response, wait=True)  # Wait for response to finish
    
    def run(self):
        """
        Main loop - continuous listening and processing
        """
        try:
            while True:
                # Listen for wake word and command
                command = self.voice_input.listen_for_command()
                
                if command:
                    # Check for exit commands
                    if any(word in command for word in ["exit", "stop", "bye", "goodbye", "quit"]):
                        self.voice_output.speak("Goodbye! See you soon!")
                        print("👋 SARA stopped")
                        break
                    
                    # Handle the command
                    self.handle_command(command)
                    
                    # Small delay before listening again
                    time.sleep(0.5)
                
        except KeyboardInterrupt:
            print("\n👋 SARA stopped by user")
            self.voice_output.speak("Goodbye!")
    
    def run_interactive(self):
        """
        Interactive mode - test SARA with text input instead of voice
        Useful for debugging and testing
        """
        print("\n" + "=" * 60)
        print("🎯 SARA Interactive Mode (Text Input)")
        print("=" * 60)
        print("Type commands (say 'exit' to quit)\n")
        
        self.voice_output.speak("I'm in interactive mode. Type your commands!")
        
        while True:
            try:
                user_input = input("\n👤 You: ").strip()
                
                if not user_input:
                    continue
                
                # Check for exit commands
                if any(word in user_input.lower() for word in ["exit", "stop", "bye", "quit"]):
                    self.voice_output.speak("Goodbye!")
                    print("👋 SARA stopped")
                    break
                
                # Handle command
                self.handle_command(user_input)
                
            except KeyboardInterrupt:
                print("\n👋 SARA stopped")
                break
    
    def run_demo(self):
        """
        Demo mode - run SARA with predefined test commands
        """
        print("\n" + "=" * 60)
        print("🎬 SARA Demo Mode")
        print("=" * 60)
        print()
        
        test_commands = [
            "what's the time?",
            "open YouTube",
            "search for Python tutorials",
            "tell me a joke",
            "what's today's date?",
            "open Google",
            "search for machine learning",
            "tell me an interesting fact",
        ]
        
        for cmd in test_commands:
            print(f"\n{'='*60}")
            print(f"📝 Testing: {cmd}")
            print(f"{'='*60}")
            self.handle_command(cmd)
            time.sleep(2)  # Pause between commands
        
        print(f"\n{'='*60}")
        print("✅ Demo completed!")
        print(f"{'='*60}\n")


def main():
    """
    Main entry point
    """
    import argparse
    
    parser = argparse.ArgumentParser(description="SARA - Smart Assistant for Real-time Actions")
    parser.add_argument(
        "--mode",
        choices=["voice", "interactive", "demo"],
        default="voice",
        help="Operating mode (default: voice)"
    )
    parser.add_argument(
        "--name",
        default="Ishant",
        help="Your name for personalized greetings (default: Ishant)"
    )
    parser.add_argument(
        "--no-ai",
        action="store_true",
        help="Disable AI mode (use rule-based logic only)"
    )
    
    args = parser.parse_args()
    
    # Initialize SARA with user's name
    enable_ai = not args.no_ai
    sara = SARA(enable_ai=enable_ai, user_name=args.name)
    
    # Run in selected mode
    if args.mode == "voice":
        print("[SARA] Voice Mode - Listening for 'Hey Sara'...")
        sara.run()
    elif args.mode == "interactive":
        sara.run_interactive()
    elif args.mode == "demo":
        sara.run_demo()


if __name__ == "__main__":
    main()
