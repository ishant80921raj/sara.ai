"""
Actions Module for SARA
Executes system actions like opening apps, websites, searching, etc.
"""

import webbrowser
import subprocess
import os
import platform
import requests
from typing import Dict, Optional
import urllib.parse

class ActionExecutor:
    """Executes actions based on user commands"""
    
    def __init__(self):
        self.os_type = platform.system()  # Windows, Linux, Darwin
        self.website_urls = {
            "youtube": "https://www.youtube.com",
            "google": "https://www.google.com",
            "whatsapp": "https://web.whatsapp.com",
            "facebook": "https://www.facebook.com",
            "twitter": "https://www.twitter.com",
            "instagram": "https://www.instagram.com",
            "gmail": "https://mail.google.com",
            "github": "https://www.github.com",
            "stackoverflow": "https://stackoverflow.com",
        }
        
        self.app_paths = self._setup_app_paths()
    
    def _setup_app_paths(self) -> Dict[str, str]:
        """Setup application paths based on OS"""
        if self.os_type == "Windows":
            return {
                "chrome": "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe",
                "firefox": "C:\\Program Files\\Mozilla Firefox\\firefox.exe",
                "calc": "calc.exe",
                "notepad": "notepad.exe",
                "vscode": "C:\\Users\\Ishant_raj_2006\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe",
                "mspaint": "mspaint.exe",
            }
        elif self.os_type == "Darwin":  # macOS
            return {
                "chrome": "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
                "firefox": "/Applications/Firefox.app/Contents/MacOS/firefox",
                "vscode": "/Applications/Visual Studio Code.app/Contents/MacOS/Code",
            }
        else:  # Linux
            return {
                "chrome": "google-chrome",
                "firefox": "firefox",
                "vscode": "code",
            }
    
    def execute(self, action_type: str, params: Dict) -> bool:
        """
        Execute an action
        
        Args:
            action_type: Type of action (app, website, search, etc.)
            params: Action parameters
            
        Returns:
            True if successful, False otherwise
        """
        try:
            if action_type == "website":
                return self.open_website(params.get("target"))
            elif action_type == "app":
                return self.open_app(params.get("target"))
            elif action_type == "search":
                return self.search_google(params.get("query"))
            elif action_type == "time" or action_type == "date":
                return True  # Already handled by brain
            elif action_type == "music":
                return self.play_music(params.get("song"))
            elif action_type == "weather":
                return True
            elif action_type == "conversation":
                return True
            else:
                return False
        except Exception as e:
            print(f"❌ Error executing action: {e}")
            return False
    
    def open_website(self, website: str) -> bool:
        """
        Open a website in default browser
        
        Args:
            website: Website name or URL
            
        Returns:
            True if successful
        """
        try:
            if website.lower() in self.website_urls:
                url = self.website_urls[website.lower()]
            elif website.startswith("http"):
                url = website
            else:
                url = f"https://{website}.com"
            
            webbrowser.open(url)
            print(f"✅ Opened {website}")
            return True
        except Exception as e:
            print(f"❌ Failed to open website: {e}")
            return False
    
    def open_app(self, app_name: str) -> bool:
        """
        Open a system application
        
        Args:
            app_name: Application name
            
        Returns:
            True if successful
        """
        try:
            app_lower = app_name.lower()
            
            if app_lower in self.app_paths:
                app_path = self.app_paths[app_lower]
                if os.path.exists(app_path) or app_lower in ["calc", "notepad"]:
                    subprocess.Popen(app_path)
                    print(f"✅ Opening {app_name}")
                    return True
                else:
                    print(f"❌ Application not found at {app_path}")
                    return False
            else:
                print(f"❌ Unknown application: {app_name}")
                return False
        except Exception as e:
            print(f"❌ Failed to open app: {e}")
            return False
    
    def search_google(self, query: str) -> bool:
        """
        Search on Google and open results
        
        Args:
            query: Search query
            
        Returns:
            True if successful
        """
        try:
            if not query:
                return False
            
            # Create Google search URL
            search_url = f"https://www.google.com/search?q={urllib.parse.quote(query)}"
            webbrowser.open(search_url)
            print(f"✅ Searching for: {query}")
            return True
        except Exception as e:
            print(f"❌ Failed to search: {e}")
            return False
    
    def play_music(self, song: Optional[str] = None) -> bool:
        """
        Play music (Spotify or YouTube Music)
        
        Args:
            song: Song name or artist
            
        Returns:
            True if successful
        """
        try:
            if song:
                # Search on YouTube Music
                search_url = f"https://music.youtube.com/search?q={urllib.parse.quote(song)}"
            else:
                # Open Spotify
                search_url = "https://open.spotify.com"
            
            webbrowser.open(search_url)
            print(f"✅ Playing music{f': {song}' if song else ''}")
            return True
        except Exception as e:
            print(f"❌ Failed to play music: {e}")
            return False
    
    def get_internet_speed(self) -> Optional[Dict]:
        """
        Get internet speed information
        
        Returns:
            Dictionary with speed info or None
        """
        try:
            response = requests.get("https://speedtest.net", timeout=5)
            return {"status": "Connected"}
        except:
            return {"status": "Offline"}
    
    def tell_weather(self, city: str = "auto") -> str:
        """
        Get weather information (free API)
        
        Args:
            city: City name
            
        Returns:
            Weather description
        """
        try:
            # Using open-meteo API (free, no key required)
            response = requests.get(
                f"https://api.open-meteo.com/v1/forecast?latitude=0&longitude=0&current=temperature_2m,weather_code"
            )
            
            if response.status_code == 200:
                data = response.json()
                temp = data.get("current", {}).get("temperature_2m", "Unknown")
                return f"Current temperature is {temp} degrees."
            return "Unable to fetch weather."
        except:
            return "I couldn't get the weather information right now."
    
    def set_reminder(self, reminder_text: str, time_str: str = None) -> bool:
        """
        Set a reminder (requires additional setup)
        
        Args:
            reminder_text: What to remind
            time_str: When to remind (optional)
            
        Returns:
            True if successful
        """
        # This would require a task scheduler integration
        print(f"📝 Reminder set: {reminder_text}")
        return True
    
    def get_system_info(self) -> Dict:
        """Get system information"""
        return {
            "os": self.os_type,
            "platform": platform.platform(),
        }
    
    def brightness_control(self, level: int) -> bool:
        """
        Control screen brightness (Windows only)
        
        Args:
            level: Brightness level (0-100)
            
        Returns:
            True if successful
        """
        try:
            if self.os_type == "Windows":
                import screen_brightness_control as sbc
                sbc.set_brightness(level)
                print(f"✅ Brightness set to {level}%")
                return True
        except:
            print("❌ Brightness control not available")
            return False
    
    def tell_joke(self) -> str:
        """Get a random joke from free API"""
        try:
            response = requests.get("https://api.api-ninjas.com/v1/jokes", timeout=5)
            if response.status_code == 200:
                joke = response.json()[0]["joke"]
                return joke
            return "Sorry, I couldn't fetch a joke right now."
        except:
            return "Here's a joke: Why did the Python apply for a job? Because it wanted to make some money with scripts!"
    
    def tell_fact(self) -> str:
        """Get a random interesting fact from free API"""
        try:
            response = requests.get("https://uselessfacts.jsoup.com/random.json", timeout=5)
            if response.status_code == 200:
                fact = response.json()["text"]
                return fact
            return "I couldn't fetch a fact right now."
        except:
            return "Did you know? Python is named after Monty Python, not the snake!"


if __name__ == "__main__":
    # Test actions
    executor = ActionExecutor()
    
    print("🤖 SARA Action Executor Test\n")
    
    # Test opening website
    print("Testing: Open YouTube")
    executor.open_website("youtube")
    
    # Test search
    print("\nTesting: Search for Python")
    executor.search_google("Python programming")
    
    # Test app opening (will try to open calculator)
    print("\nTesting: Open Calculator")
    executor.open_app("calc")
    
    # Test joke
    print(f"\nTesting: Tell a joke")
    print(f"😄 {executor.tell_joke()}")
    
    # Test fact
    print(f"\nTesting: Tell a fact")
    print(f"💡 {executor.tell_fact()}")
