"""
Quick setup script for Groq Free API
This helps users set up the API key easily
"""

import os
import subprocess
import sys

def main():
    print("\n" + "="*70)
    print("🚀 SARA - FREE AI Setup Wizard")
    print("="*70 + "\n")
    
    print("Welcome! This will help you set up SARA with FREE Groq AI!\n")
    
    # Check if API key already set
    existing_key = os.getenv('GROQ_API_KEY')
    if existing_key:
        print(f"✅ Found existing Groq API key: {existing_key[:10]}...")
        use_existing = input("\nUse this key? (y/n): ").strip().lower()
        if use_existing == 'y':
            test_brain()
            return
    
    # Ask if user wants to continue
    print("\n📝 Steps to get FREE API key:")
    print("  1. Go to: https://console.groq.com")
    print("  2. Sign up (free, no credit card needed)")
    print("  3. Create API key (in API Keys section)")
    print("  4. Copy the key (starts with 'gsk_')")
    print("\n")
    
    continue_setup = input("Do you want to continue? (y/n): ").strip().lower()
    
    if continue_setup != 'y':
        print("\n✅ No problem! SARA works great in fallback mode too!")
        print("   Come back when you get the API key from https://console.groq.com")
        print("\n   To set it up later, run: python setup_groq.py")
        return
    
    # Get API key from user
    print("\nPaste your Groq API key here:")
    print("(It should start with 'gsk_')\n")
    api_key = input("API Key: ").strip()
    
    if not api_key.startswith('gsk_'):
        print("\n❌ Invalid API key format! Should start with 'gsk_'")
        print("   Get a valid key from: https://console.groq.com")
        return
    
    # Set environment variable based on OS
    if sys.platform == 'win32':
        # Windows
        print("\n⚙️  Setting up for Windows...")
        
        # Set for current session
        os.environ['GROQ_API_KEY'] = api_key
        
        # Set permanently (add to user environment)
        try:
            subprocess.run([
                'powershell', '-Command',
                f'[Environment]::SetEnvironmentVariable("GROQ_API_KEY", "{api_key}", "User")'
            ], check=True)
            print("✅ API key set permanently in Windows!")
        except:
            print("⚠️  Could not set permanently. Setting for current session only.")
            subprocess.run([
                'powershell', '-Command',
                f'$env:GROQ_API_KEY="{api_key}"'
            ], check=False)
    else:
        # Linux/Mac
        print("\n⚙️  Setting up for Linux/Mac...")
        
        # Add to .bashrc or .zshrc
        shell_rc = os.path.expanduser('~/.bashrc')
        if not os.path.exists(shell_rc):
            shell_rc = os.path.expanduser('~/.zshrc')
        
        export_line = f'export GROQ_API_KEY="{api_key}"'
        
        try:
            with open(shell_rc, 'a') as f:
                f.write(f'\n{export_line}\n')
            print(f"✅ API key added to {shell_rc}")
        except:
            print("⚠️  Could not write to shell config")
        
        os.environ['GROQ_API_KEY'] = api_key
    
    print("\n🎉 API key configured!")
    print("="*70 + "\n")
    
    # Test the connection
    test_brain()

def test_brain():
    """Test if brain works with the API key"""
    print("🧪 Testing SARA with FREE AI brain...\n")
    
    from brain import SARBrain
    brain = SARBrain()
    
    test_commands = [
        "Namaste! Kaisa ho?",
        "Tell me a fun fact",
        "What's the current time?",
    ]
    
    for cmd in test_commands:
        response, _, _ = brain.process_command(cmd)
        print(f"👤 You: {cmd}")
        print(f"🤖 SARA: {response}\n")
    
    print("="*70)
    print("✅ SARA is ready to use!")
    print("="*70)
    print("\n💡 Next steps:")
    print("  1. Try talking to SARA in GUI: python sara_gui_enhanced.py")
    print("  2. Or use the brain directly: from brain import SARBrain")
    print("\n🎉 Enjoy your FREE AI assistant!\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Setup cancelled")
    except Exception as e:
        print(f"\n❌ Error: {e}")
        print("\nTroubleshooting:")
        print("  1. Check your internet connection")
        print("  2. Make sure API key is correct (starts with 'gsk_')")
        print("  3. Visit: https://console.groq.com/docs")
