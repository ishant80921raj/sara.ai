"""
Test script to verify SARA improvements
- Math capabilities
- Better emotional responses
- General knowledge
- Better language
"""

from brain import SARBrain

def test_sara():
    print("=" * 60)
    print("🤖 SARA IMPROVED VERSION - TESTING")
    print("=" * 60)
    
    brain = SARBrain(use_ollama=False)
    
    # Test categories
    test_commands = {
        "🎯 MATH QUESTIONS": [
            "what is 15 plus 25?",
            "15 aur 25 ka sum kya hai?",
            "10 times 5 kya hota hai?",
            "100 divided by 4",
            "20 percent of 500",
            "15 ka square kya hai?",
            "square root of 144?",
            "circle ka area 5 radius?",
            "rectangle ka area 10 length aur 5 width?",
        ],
        "💬 EMOTIONAL GREETINGS": [
            "hello",
            "hi",
            "how are you",
            "kaise ho",
            "thanks",
            "thank you",
        ],
        "📚 GENERAL KNOWLEDGE": [
            "india ki capital kya hai?",
            "taj mahal kya hai?",
            "triangle ke kitne sides hote hain?",
            "light ki speed kya hai?",
            "earth rotate karti hai?",
            "prime number kya hota hai?",
        ],
        "😄 ENTERTAINMENT": [
            "ek joke sunao",
            "ek fact batao",
            "kuch inspirational sunao",
        ],
    }
    
    for category, commands in test_commands.items():
        print(f"\n{category}")
        print("-" * 60)
        
        for cmd in commands:
            response, action, params = brain.process_command(cmd)
            print(f"👤 User: {cmd}")
            print(f"🤖 SARA: {response}")
            print()

if __name__ == "__main__":
    test_sara()
