"""
SARA GUI - Modern Voice Assistant Interface
Similar to Google Assistant with chat bubbles and voice integration
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox
import threading
import time
from datetime import datetime
from voice_input import VoiceInput
from voice_output import VoiceOutput
from brain import SARBrain
from actions import ActionExecutor


class SARAGui:
    """Modern GUI for SARA Voice Assistant"""
    
    def __init__(self, root, user_name="Ishant"):
        self.root = root
        self.user_name = user_name
        
        # Configure window - MAKE IT VISIBLE AND FOCUSED
        self.root.title("SARA - Smart Assistant for Real-time Actions")
        self.root.geometry("900x750")
        self.root.configure(bg="#0d1117")  # Dark theme
        
        # Bring window to front and focus it
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        self.root.focus()
        self.root.lift()
        
        # Initialize modules
        try:
            self.voice_input = VoiceInput()
            self.voice_output = VoiceOutput(rate=150, volume=0.9)
            self.brain = SARBrain(use_ollama=False)
            self.action_executor = ActionExecutor()
        except Exception as e:
            print(f"Error initializing: {e}")
        
        self.listening = False
        
        # Create GUI
        self.create_ui()
        
        # Emotional greeting on startup
        self.show_greeting()
    
    def create_ui(self):
        """Create the user interface"""
        
        # Top bar with logo and title
        top_frame = tk.Frame(self.root, bg="#161b22", height=80)
        top_frame.pack(fill=tk.X, padx=0, pady=0)
        top_frame.pack_propagate(False)
        
        title_label = tk.Label(
            top_frame,
            text="SARA",
            font=("Segoe UI", 32, "bold"),
            fg="#58a6ff",
            bg="#161b22"
        )
        title_label.pack(pady=15)
        
        subtitle = tk.Label(
            top_frame,
            text="Smart Assistant for Real-time Actions",
            font=("Segoe UI", 10),
            fg="#8b949e",
            bg="#161b22"
        )
        subtitle.pack(pady=2)
        
        # Chat display area
        chat_frame = tk.Frame(self.root, bg="#0d1117")
        chat_frame.pack(fill=tk.BOTH, expand=True, padx=15, pady=15)
        
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame,
            wrap=tk.WORD,
            bg="#0d1117",
            fg="#c9d1d9",
            font=("Segoe UI", 11),
            state=tk.DISABLED,
            relief=tk.FLAT,
            borderwidth=0,
            insertbackground="#58a6ff"
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True)
        
        # Configure tags for styling
        self.chat_display.tag_config("sara_greeting", foreground="#58a6ff", font=("Segoe UI", 11, "italic"))
        self.chat_display.tag_config("sara_response", foreground="#79c0ff", font=("Segoe UI", 11))
        self.chat_display.tag_config("user_input", foreground="#85e89d", font=("Segoe UI", 11))
        self.chat_display.tag_config("timestamp", foreground="#6e7681", font=("Segoe UI", 9))
        
        # Input area
        input_frame = tk.Frame(self.root, bg="#0d1117")
        input_frame.pack(fill=tk.X, padx=15, pady=15)
        
        # Text input field
        self.input_field = tk.Entry(
            input_frame,
            font=("Segoe UI", 12),
            bg="#161b22",
            fg="#c9d1d9",
            relief=tk.FLAT,
            borderwidth=2,
            insertbackground="#58a6ff"
        )
        self.input_field.pack(fill=tk.X, side=tk.LEFT, expand=True, padx=(0, 10))
        self.input_field.bind("<Return>", self.on_text_submit)
        
        # Buttons frame
        buttons_frame = tk.Frame(input_frame, bg="#0d1117")
        buttons_frame.pack(side=tk.RIGHT, padx=0)
        
        # Voice button
        self.voice_btn = tk.Button(
            buttons_frame,
            text="🎤 Listen",
            command=self.on_voice_click,
            bg="#238636",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=8,
            cursor="hand2"
        )
        self.voice_btn.pack(side=tk.LEFT, padx=(0, 8))
        
        # Send button
        send_btn = tk.Button(
            buttons_frame,
            text="Send",
            command=self.on_send_click,
            bg="#1f6feb",
            fg="white",
            font=("Segoe UI", 10, "bold"),
            relief=tk.FLAT,
            padx=15,
            pady=8,
            cursor="hand2"
        )
        send_btn.pack(side=tk.LEFT)
        
        # Status bar
        self.status_var = tk.StringVar(value="Ready to listen...")
        status_bar = tk.Label(
            self.root,
            textvariable=self.status_var,
            font=("Segoe UI", 9),
            fg="#6e7681",
            bg="#161b22",
            relief=tk.SUNKEN,
            anchor=tk.W,
            padx=10,
            pady=5
        )
        status_bar.pack(fill=tk.X, side=tk.BOTTOM)
    
    def show_greeting(self):
        """Show emotional greeting"""
        hour = datetime.now().hour
        
        if hour < 6:
            greeting = f"Raat ka samay hai {self.user_name}... tum abhi bhi jaag rahe ho? 🌙"
        elif hour < 12:
            greeting = f"Subah-subah hello {self.user_name}! Aaj kaisa feel kar rahe ho? ☀️"
        elif hour < 17:
            greeting = f"Afternoon {self.user_name}! Kaisa chal raha hai din? 🌤️"
        elif hour < 21:
            greeting = f"Shaam ka vaqt hai {self.user_name}... relax karo! 🌆"
        else:
            greeting = f"Late night {self.user_name}! Kya soch rahe ho? 💭"
        
        self.add_sara_message(greeting, is_greeting=True)
        self.voice_output.speak(greeting, wait=True)
    
    def add_sara_message(self, message, is_greeting=False):
        """Add SARA's message to chat"""
        self.chat_display.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M")
        
        self.chat_display.insert(tk.END, "\n")
        self.chat_display.insert(tk.END, "SARA: ", "timestamp")
        self.chat_display.insert(tk.END, f"[{timestamp}]\n", "timestamp")
        
        if is_greeting:
            self.chat_display.insert(tk.END, f"{message}\n\n", "sara_greeting")
        else:
            self.chat_display.insert(tk.END, f"{message}\n\n", "sara_response")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def add_user_message(self, message):
        """Add user's message to chat"""
        self.chat_display.config(state=tk.NORMAL)
        
        timestamp = datetime.now().strftime("%H:%M")
        
        self.chat_display.insert(tk.END, f"You ({timestamp}):\n", "timestamp")
        self.chat_display.insert(tk.END, f"{message}\n\n", "user_input")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def on_text_submit(self, event=None):
        """Handle text input submission"""
        text = self.input_field.get().strip()
        if text:
            self.input_field.delete(0, tk.END)
            self.process_command(text)
    
    def on_send_click(self):
        """Handle send button click"""
        self.on_text_submit()
    
    def on_voice_click(self):
        """Handle voice button click"""
        if self.listening:
            return
        
        # Run in separate thread to not freeze UI
        thread = threading.Thread(target=self.listen_for_voice)
        thread.daemon = True
        thread.start()
    
    def listen_for_voice(self):
        """Listen for voice command"""
        self.listening = True
        self.voice_btn.config(state=tk.DISABLED, bg="#da3633", text="🎤 Listening...")
        self.status_var.set("Listening for voice command...")
        self.root.update()
        
        try:
            # Listen for wake word first
            self.add_sara_message("Listening for 'Hey Sara'...")
            command = self.voice_input.listen_for_command()
            
            if command:
                self.process_command(command)
            else:
                self.add_sara_message("Sorry, couldn't understand. Please try again.")
        except Exception as e:
            self.add_sara_message(f"Voice error: {str(e)}")
        finally:
            self.listening = False
            self.voice_btn.config(state=tk.NORMAL, bg="#238636", text="🎤 Listen")
            self.status_var.set("Ready to listen...")
    
    def process_command(self, command):
        """Process user command"""
        self.status_var.set("Processing...")
        self.root.update()
        
        # Add user input to chat
        self.add_user_message(command)
        
        # Get response from brain
        response, action_type, action_params = self.brain.process_command(command)
        
        # Execute action if needed
        if action_type not in ["conversation", "time", "date", "unknown"]:
            self.action_executor.execute(action_type, action_params)
        
        # Special handling for jokes and facts
        if action_type == "joke":
            response = self.action_executor.tell_joke()
        elif action_type == "fact":
            response = self.action_executor.tell_fact()
        
        # Add SARA response to chat and speak it
        self.add_sara_message(response)
        
        # Speak in background thread
        thread = threading.Thread(target=self.voice_output.speak, args=(response, True))
        thread.daemon = True
        thread.start()
        
        self.status_var.set("Ready to listen...")


def run_sara_gui(user_name="Ishant"):
    """Run SARA GUI"""
    root = tk.Tk()
    app = SARAGui(root, user_name=user_name)
    root.mainloop()


if __name__ == "__main__":
    run_sara_gui()
