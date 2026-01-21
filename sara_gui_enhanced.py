"""
SARA - ALL ROUNDER VOICE ASSISTANT
Features: Math, Science, Grammar, Entertainment, Emotions, Camera, Stories, Lullabies
A complete AI companion with voice, camera, and emotional intelligence!
"""

import tkinter as tk
from tkinter import scrolledtext, messagebox, font
import threading
import time
from datetime import datetime
from voice_input import VoiceInput
from voice_output import VoiceOutput
from brain import SARBrain
from actions import ActionExecutor
import random


class SARACharacter:
    """2D Animated SARA Cartoon Character with Expressions"""
    
    def __init__(self, canvas, x, y, size=150):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.size = size
        self.expression = "neutral"  # neutral, happy, speaking, thinking, sad
        self.eye_state = "open"  # open, closed, wink
        self.draw_character()
    
    def draw_character(self):
        """Draw 2D cartoon character"""
        self.canvas.delete("character")
        
        # Head (circle)
        head = self.canvas.create_oval(
            self.x - self.size//2, self.y - self.size//2,
            self.x + self.size//2, self.y + self.size//2,
            fill="#FFD700", outline="#FF69B4", width=3, tags="character"
        )
        
        # Eyes
        eye_y = self.y - self.size//6
        
        if self.eye_state == "open":
            # Left eye
            self.canvas.create_oval(
                self.x - self.size//5 - 15, eye_y - 15,
                self.x - self.size//5 + 15, eye_y + 15,
                fill="white", outline="black", width=2, tags="character"
            )
            self.canvas.create_oval(
                self.x - self.size//5 - 8, eye_y - 8,
                self.x - self.size//5 + 8, eye_y + 8,
                fill="black", tags="character"
            )
            
            # Right eye
            self.canvas.create_oval(
                self.x + self.size//5 - 15, eye_y - 15,
                self.x + self.size//5 + 15, eye_y + 15,
                fill="white", outline="black", width=2, tags="character"
            )
            self.canvas.create_oval(
                self.x + self.size//5 - 8, eye_y - 8,
                self.x + self.size//5 + 8, eye_y + 8,
                fill="black", tags="character"
            )
        
        elif self.eye_state == "closed":
            # Closed eyes (lines)
            self.canvas.create_line(
                self.x - self.size//5 - 15, eye_y,
                self.x - self.size//5 + 15, eye_y,
                width=3, fill="black", tags="character"
            )
            self.canvas.create_line(
                self.x + self.size//5 - 15, eye_y,
                self.x + self.size//5 + 15, eye_y,
                width=3, fill="black", tags="character"
            )
        
        elif self.eye_state == "wink":
            # Left eye open
            self.canvas.create_oval(
                self.x - self.size//5 - 15, eye_y - 15,
                self.x - self.size//5 + 15, eye_y + 15,
                fill="white", outline="black", width=2, tags="character"
            )
            self.canvas.create_oval(
                self.x - self.size//5 - 8, eye_y - 8,
                self.x - self.size//5 + 8, eye_y + 8,
                fill="black", tags="character"
            )
            
            # Right eye closed (wink)
            self.canvas.create_line(
                self.x + self.size//5 - 15, eye_y,
                self.x + self.size//5 + 15, eye_y,
                width=3, fill="black", tags="character"
            )
        
        # Mouth based on expression
        mouth_y = self.y + self.size//6
        
        if self.expression == "happy":
            # Smiling mouth (arc)
            self.canvas.create_arc(
                self.x - 40, mouth_y - 20,
                self.x + 40, mouth_y + 30,
                start=0, extent=180, fill="#FF1493", outline="black", width=2, tags="character"
            )
        
        elif self.expression == "speaking":
            # Open mouth (oval)
            self.canvas.create_oval(
                self.x - 30, mouth_y - 10,
                self.x + 30, mouth_y + 25,
                fill="#8B0000", outline="black", width=2, tags="character"
            )
            # Tongue
            self.canvas.create_oval(
                self.x - 15, mouth_y + 15,
                self.x + 15, mouth_y + 22,
                fill="#FF69B4", tags="character"
            )
        
        elif self.expression == "thinking":
            # Thinking mouth (neutral line)
            self.canvas.create_line(
                self.x - 35, mouth_y,
                self.x + 35, mouth_y,
                width=3, fill="black", tags="character"
            )
            # Thinking bubble
            self.canvas.create_oval(
                self.x + 80, self.y - 80,
                self.x + 110, self.y - 50,
                fill="white", outline="black", width=2, tags="character"
            )
        
        elif self.expression == "sad":
            # Sad mouth (inverted arc)
            self.canvas.create_arc(
                self.x - 40, mouth_y - 30,
                self.x + 40, mouth_y + 20,
                start=180, extent=180, fill="#FF1493", outline="black", width=2, tags="character"
            )
        
        else:  # neutral
            # Neutral mouth
            self.canvas.create_line(
                self.x - 30, mouth_y,
                self.x + 30, mouth_y,
                width=2, fill="black", tags="character"
            )
        
        # Blush (optional)
        if self.expression in ["happy", "speaking"]:
            self.canvas.create_oval(
                self.x - self.size//2 + 20, self.y - 10,
                self.x - self.size//2 + 50, self.y + 20,
                fill="#FFB6C1", outline="", tags="character"
            )
            self.canvas.create_oval(
                self.x + self.size//2 - 50, self.y - 10,
                self.x + self.size//2 - 20, self.y + 20,
                fill="#FFB6C1", outline="", tags="character"
            )
    
    def set_expression(self, expression):
        """Change facial expression"""
        self.expression = expression
        self.draw_character()
    
    def set_eye_state(self, state):
        """Change eye state"""
        self.eye_state = state
        self.draw_character()
    
    def animate_speaking(self):
        """Animate character speaking"""
        states = ["speaking", "happy", "speaking"]
        for state in states:
            self.set_expression(state)
            self.canvas.update()
            time.sleep(0.3)
        self.set_expression("happy")


class SARAGui:
    """Enhanced SARA GUI with Animation, Controls, and Voice"""
    
    def __init__(self, root, user_name="Ishant"):
        self.root = root
        self.user_name = user_name
        self.is_muted = False
        self.conversation_active = False
        self.listening = False
        
        # Configure window
        self.root.title("🎤 SARA - Advanced Voice Assistant")
        self.root.geometry("1100x850")
        self.root.configure(bg="#0d1117")
        
        # Make window visible and focused
        self.root.attributes('-topmost', True)
        self.root.after_idle(self.root.attributes, '-topmost', False)
        self.root.focus()
        self.root.lift()
        
        # Initialize modules
        try:
            self.voice_input = VoiceInput()
            self.voice_output = VoiceOutput(rate=150, volume=0.9)
            self.brain = SARBrain(use_free_api=True)
            self.action_executor = ActionExecutor()
        except Exception as e:
            messagebox.showerror("Error", f"Error initializing modules: {e}")
            return


        # Initialize modules
    
        # Create GUI
        self.create_ui()
        
        # Show greeting on startup
        self.show_greeting()
    
    def create_ui(self):
        """Create the GUI layout"""
        
        # Main container
        main_frame = tk.Frame(self.root, bg="#0d1117")
        main_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # ==================== TOP SECTION: ANIMATION & CONTROLS ====================
        top_frame = tk.Frame(main_frame, bg="#161B22", bd=2, relief=tk.RAISED)
        top_frame.pack(fill=tk.X, pady=(0, 10))
        
        # Character canvas on left
        left_frame = tk.Frame(top_frame, bg="#161B22")
        left_frame.pack(side=tk.LEFT, padx=20, pady=15)
        
        self.canvas = tk.Canvas(
            left_frame, width=250, height=250, bg="#E8F4F8",
            bd=3, relief=tk.RIDGE, highlightbackground="#58a6ff"
        )
        self.canvas.pack()
        
        # Create character
        self.character = SARACharacter(self.canvas, 125, 125, size=140)
        
        # Controls on right
        controls_frame = tk.Frame(top_frame, bg="#161B22")
        controls_frame.pack(side=tk.RIGHT, padx=20, pady=15, fill=tk.BOTH, expand=True)
        
        # Title
        title_label = tk.Label(
            controls_frame, text="🎤 SARA - Voice Assistant",
            font=("Arial", 18, "bold"), fg="#58a6ff", bg="#161B22"
        )
        title_label.pack(pady=(0, 10))
        
        # Status
        self.status_var = tk.StringVar(value="Ready to chat! Click START")
        status_label = tk.Label(
            controls_frame, textvariable=self.status_var,
            font=("Arial", 11), fg="#79c0ff", bg="#161B22"
        )
        status_label.pack(pady=(0, 15))
        
        # Buttons Frame
        buttons_frame = tk.Frame(controls_frame, bg="#161B22")
        buttons_frame.pack(fill=tk.BOTH, expand=True)
        
        # START Button
        self.start_btn = tk.Button(
            buttons_frame, text="▶️ START", font=("Arial", 13, "bold"),
            bg="#238636", fg="white", padx=20, pady=12,
            command=self.start_conversation,
            cursor="hand2", activebackground="#2ea043"
        )
        self.start_btn.pack(pady=5, fill=tk.X)
        
        # END Button
        self.end_btn = tk.Button(
            buttons_frame, text="⏹️ END", font=("Arial", 13, "bold"),
            bg="#da3633", fg="white", padx=20, pady=12,
            command=self.end_conversation, state=tk.DISABLED,
            cursor="hand2", activebackground="#f85149"
        )
        self.end_btn.pack(pady=5, fill=tk.X)
        
        # MUTE/UNMUTE Button
        self.mute_btn = tk.Button(
            buttons_frame, text="🔊 Unmuted", font=("Arial", 13, "bold"),
            bg="#1f6feb", fg="white", padx=20, pady=12,
            command=self.toggle_mute,
            cursor="hand2", activebackground="#388bfd"
        )
        self.mute_btn.pack(pady=5, fill=tk.X)
        
        # CAMERA Button - NEW FEATURE!
        self.camera_btn = tk.Button(
            buttons_frame, text="📷 CAMERA", font=("Arial", 13, "bold"),
            bg="#1f6feb", fg="white", padx=20, pady=12,
            command=self.open_camera,
            cursor="hand2", activebackground="#388bfd"
        )
        self.camera_btn.pack(pady=5, fill=tk.X)
        
        # Status indicators
        indicator_frame = tk.Frame(controls_frame, bg="#161B22")
        indicator_frame.pack(fill=tk.X, pady=(15, 0))
        
        tk.Label(
            indicator_frame, text="● Voice:", fg="#79c0ff", bg="#161B22",
            font=("Arial", 10)
        ).pack(side=tk.LEFT, padx=(0, 5))
        
        self.voice_status = tk.Label(
            indicator_frame, text="Enabled", fg="#85e89d", bg="#161B22",
            font=("Arial", 10, "bold")
        )
        self.voice_status.pack(side=tk.LEFT)
        
        # ==================== MIDDLE SECTION: CHAT AREA ====================
        chat_frame = tk.Frame(main_frame, bg="#161B22", bd=2, relief=tk.SUNKEN)
        chat_frame.pack(fill=tk.BOTH, expand=True, pady=(0, 10))
        
        # Chat label
        tk.Label(
            chat_frame, text="💬 CONVERSATION", font=("Arial", 12, "bold"),
            fg="#58a6ff", bg="#161B22"
        ).pack(pady=(5, 0))
        
        # Chat display
        self.chat_display = scrolledtext.ScrolledText(
            chat_frame, height=12, width=70,
            bg="#0d1117", fg="#c9d1d9", font=("Consolas", 10),
            wrap=tk.WORD, bd=0, padx=10, pady=10
        )
        self.chat_display.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
        
        # Configure colors for messages
        self.chat_display.tag_config("user", foreground="#85e89d", font=("Consolas", 10, "bold"))
        self.chat_display.tag_config("sara", foreground="#79c0ff", font=("Consolas", 10, "bold"))
        self.chat_display.tag_config("time", foreground="#8b949e", font=("Consolas", 8))
        self.chat_display.config(state=tk.DISABLED)
        
        # ==================== BOTTOM SECTION: INPUT & BUTTONS ====================
        input_frame = tk.Frame(main_frame, bg="#161B22", bd=2, relief=tk.RAISED)
        input_frame.pack(fill=tk.X)
        
        # Input field
        self.input_field = tk.Entry(
            input_frame, font=("Arial", 11), bg="#0d1117", fg="#c9d1d9",
            insertbackground="#58a6ff", bd=0
        )
        self.input_field.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
        self.input_field.bind("<Return>", lambda e: self.send_text_message())
        
        # Listen button
        self.listen_btn = tk.Button(
            input_frame, text="🎤 LISTEN", font=("Arial", 11, "bold"),
            bg="#238636", fg="white", padx=15, pady=8,
            command=self.listen_for_voice, cursor="hand2",
            activebackground="#2ea043"
        )
        self.listen_btn.pack(side=tk.LEFT, padx=5, pady=10)
        
        # Send button
        send_btn = tk.Button(
            input_frame, text="SEND", font=("Arial", 11, "bold"),
            bg="#1f6feb", fg="white", padx=15, pady=8,
            command=self.send_text_message, cursor="hand2",
            activebackground="#388bfd"
        )
        send_btn.pack(side=tk.LEFT, padx=(0, 10), pady=10)
        
        # Disable send button initially
        self.input_field.config(state=tk.DISABLED)
        self.listen_btn.config(state=tk.DISABLED)
        send_btn.config(state=tk.DISABLED)
        self.send_btn = send_btn
    
    def start_conversation(self):
        """Start conversation"""
        self.conversation_active = True
        self.start_btn.config(state=tk.DISABLED)
        self.end_btn.config(state=tk.NORMAL)
        self.input_field.config(state=tk.NORMAL)
        self.listen_btn.config(state=tk.NORMAL)
        self.send_btn.config(state=tk.NORMAL)
        
        self.status_var.set("🟢 Conversation Active - Ready to listen!")
        self.character.set_expression("happy")
        
        # Add message to chat
        self.add_sara_message("Ready! Click 🎤 LISTEN or type your message!")
    
    def end_conversation(self):
        """End conversation"""
        self.conversation_active = False
        self.start_btn.config(state=tk.NORMAL)
        self.end_btn.config(state=tk.DISABLED)
        self.input_field.config(state=tk.DISABLED)
        self.listen_btn.config(state=tk.DISABLED)
        self.send_btn.config(state=tk.DISABLED)
        
        self.status_var.set("🔴 Conversation Ended - Click START to begin again")
        self.character.set_expression("neutral")
        
        self.add_sara_message("Conversation ended! Click START to chat again.")
    
    def toggle_mute(self):
        """Toggle mute/unmute"""
        self.is_muted = not self.is_muted
        
        if self.is_muted:
            self.mute_btn.config(text="🔇 Muted", bg="#6e40aa")
            self.voice_status.config(text="Disabled", fg="#d1640c")
        else:
            self.mute_btn.config(text="🔊 Unmuted", bg="#1f6feb")
            self.voice_status.config(text="Enabled", fg="#85e89d")
    
    def show_greeting(self):
        """Show emotional greeting on startup"""
        if not self.conversation_active:
            return
        
        greeting_thread = threading.Thread(target=self._show_greeting_async)
        greeting_thread.daemon = True
        greeting_thread.start()
    
    def _show_greeting_async(self):
        """Async greeting"""
        from datetime import datetime
        hour = datetime.now().hour
        
        if hour < 12:
            greeting = f"🌅 Namaste {self.user_name}! Suprabhat! Kaise ho aaj?"
        elif hour < 18:
            greeting = f"☀️ Namaste {self.user_name}! Afternoon mast chal raha hai?"
            self.character.set_expression("happy")
        else:
            greeting = f"🌙 Raat ka samay hai {self.user_name}... tum abhi bhi jaag rahe ho?"
            self.character.set_expression("thinking")
        
        self.add_sara_message(greeting)
        
        if not self.is_muted:
            self.character.animate_speaking()
            self.voice_output.speak(greeting, wait=True)
    
    def listen_for_voice(self):
        """Listen for voice input"""
        if not self.conversation_active:
            messagebox.showwarning("Error", "Please click START first!")
            return
        
        listen_thread = threading.Thread(target=self._listen_async)
        listen_thread.daemon = True
        listen_thread.start()
    
    def _listen_async(self):
        """Async voice listening"""
        self.listen_btn.config(state=tk.DISABLED, text="🎤 LISTENING...", bg="#da3633")
        self.root.update()
        self.status_var.set("👂 Listening... Speak now!")
        self.character.set_expression("thinking")
        
        try:
            command = self.voice_input.listen_for_audio(timeout=10)
            
            if command:
                self.input_field.delete(0, tk.END)
                self.input_field.insert(0, command)
                self.add_user_message(command)
                
                # Process command
                response, action_type, params = self.brain.process_command(command)
                
                self.add_sara_message(response)
                
                # Animate and speak
                if not self.is_muted:
                    self.character.animate_speaking()
                    self.voice_output.speak(response, wait=True)
                
                self.character.set_expression("happy")
        
        except Exception as e:
            self.status_var.set(f"❌ Error: {str(e)}")
            self.character.set_expression("sad")
        
        finally:
            self.listen_btn.config(state=tk.NORMAL, text="🎤 LISTEN", bg="#238636")
            self.status_var.set("🟢 Ready to listen!")
    
    def send_text_message(self):
        """Send text message"""
        if not self.conversation_active:
            messagebox.showwarning("Error", "Please click START first!")
            return
        
        text = self.input_field.get().strip()
        if not text:
            return
        
        self.input_field.delete(0, tk.END)
        self.add_user_message(text)
        
        # Process in background
        process_thread = threading.Thread(target=self._process_text_async, args=(text,))
        process_thread.daemon = True
        process_thread.start()
    
    def _process_text_async(self, text):
        """Async text processing"""
        try:
            self.status_var.set("⏳ Processing...")
            self.character.set_expression("thinking")
            
            response, action_type, params = self.brain.process_command(text)
            
            self.add_sara_message(response)
            
            # Animate and speak
            if not self.is_muted:
                self.character.animate_speaking()
                self.voice_output.speak(response, wait=True)
            
            self.character.set_expression("happy")
            self.status_var.set("🟢 Ready!")
        
        except Exception as e:
            self.status_var.set(f"❌ Error: {str(e)}")
            self.character.set_expression("sad")
    
    def add_user_message(self, message):
        """Add user message to chat"""
        self.chat_display.config(state=tk.NORMAL)
        
        time_str = datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"You [{time_str}]:\n", "time")
        self.chat_display.insert(tk.END, f"{message}\n\n", "user")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def add_sara_message(self, message):
        """Add SARA message to chat"""
        self.chat_display.config(state=tk.NORMAL)
        
        time_str = datetime.now().strftime("%H:%M:%S")
        self.chat_display.insert(tk.END, f"SARA [{time_str}]:\n", "time")
        self.chat_display.insert(tk.END, f"{message}\n\n", "sara")
        
        self.chat_display.config(state=tk.DISABLED)
        self.chat_display.see(tk.END)
    
    def open_camera(self):
        """Open camera with circular face display in GUI"""
        try:
            import cv2
            import numpy as np
            from PIL import Image, ImageDraw, ImageTk
        except ImportError:
            messagebox.showwarning("Camera Error", "Missing libraries. Install: pip install opencv-python pillow")
            return
        
        # Try multiple camera indices
        cap = None
        for camera_idx in [0, 1, 2]:
            cap = cv2.VideoCapture(camera_idx)
            if cap.isOpened():
                break
        
        if cap is None or not cap.isOpened():
            messagebox.showerror("Camera Error", "कैमरा खुल नहीं सका! Check if camera is connected.")
            return
        
        # Set camera properties
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 480)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        cap.set(cv2.CAP_PROP_FPS, 30)
        
        self.character.set_expression("happy")
        self.add_sara_message("📷 Kamera khul gya! Tera mukhra dekh raha hun! 😊")
        
        # Create camera window
        camera_window = tk.Toplevel(self.root)
        camera_window.title("SARA - Camera (S=Sad, H=Happy, A=Angry, Q=Quit)")
        camera_window.geometry("600x680")
        camera_window.configure(bg="#1a1a1a")
        
        # Title
        title_label = tk.Label(camera_window, text="📷 SARA's Mood Detector", 
                               font=("Arial", 16, "bold"), bg="#1a1a1a", fg="#00ffff")
        title_label.pack(pady=10)
        
        # Canvas for camera feed
        canvas = tk.Canvas(camera_window, width=450, height=450, bg="#000000", highlightthickness=0)
        canvas.pack(pady=10)
        
        # Instructions
        instr_label = tk.Label(camera_window, 
                               text="Position your face in the circle\nPress: S(Sad) H(Happy) A(Angry) Q(Quit)",
                               font=("Arial", 11), bg="#1a1a1a", fg="#ffff00")
        instr_label.pack(pady=5)
        
        status_label = tk.Label(camera_window, text="Loading camera...", 
                               font=("Arial", 10), bg="#1a1a1a", fg="#00ff00")
        status_label.pack()
        
        self.camera_running = True
        photo_ref = [None]  # Use list to store reference in nested function
        
        def update_frame():
            """Update camera frame in canvas"""
            if not self.camera_running:
                cap.release()
                return
            
            ret, frame = cap.read()
            if not ret:
                status_label.config(text="Camera Error!", fg="#ff0000")
                if self.camera_running:
                    camera_window.after(100, update_frame)
                return
            
            try:
                # Flip for selfie view
                frame = cv2.flip(frame, 1)
                h, w = frame.shape[:2]
                
                # Crop to square
                size = min(h, w)
                top = (h - size) // 2
                left = (w - size) // 2
                frame = frame[top:top+size, left:left+size]
                
                # Resize
                frame = cv2.resize(frame, (450, 450))
                
                # Create circular mask
                mask = Image.new('L', (450, 450), 0)
                draw_mask = ImageDraw.Draw(mask)
                draw_mask.ellipse([25, 25, 425, 425], fill=255)
                
                # Convert to PIL
                frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                pil_image = Image.fromarray(frame_rgb)
                pil_image.putalpha(mask)
                
                # Create background
                bg = Image.new('RGB', (450, 450), color=(40, 40, 40))
                draw_bg = ImageDraw.Draw(bg)
                draw_bg.ellipse([25, 25, 425, 425], outline=(0, 255, 255), width=3)
                
                # Paste circular image
                bg.paste(pil_image, (0, 0), pil_image)
                
                # Convert to PhotoImage using ImageTk
                photo_ref[0] = ImageTk.PhotoImage(bg)
                canvas.delete("all")
                canvas.create_image(225, 225, image=photo_ref[0])
                
                status_label.config(text="✓ Camera Active", fg="#00ff00")
                
            except Exception as e:
                status_label.config(text=f"Error: {str(e)[:25]}", fg="#ff6600")
            
            if self.camera_running:
                camera_window.after(30, update_frame)
        
        camera_window.after(100, update_frame)
        
        # Key binding
        def on_key(event):
            key = event.char.lower()
            if key == 'q':
                self.camera_running = False
                camera_window.destroy()
            elif key == 's':  # Sad
                self.camera_running = False
                camera_window.destroy()
                self.character.set_expression("sad")
                self.add_sara_message("💔 Aw beta, tu udaas dikh raha hai!")
                emotion_response = self.brain.get_lullaby()
                self.add_sara_message(emotion_response)
                if not self.is_muted:
                    self.voice_output.speak(emotion_response, wait=False)
            elif key == 'h':  # Happy
                self.camera_running = False
                camera_window.destroy()
                self.character.set_expression("happy")
                self.add_sara_message("😊 Tu khush dikh raha hai! 🎉✨")
                if not self.is_muted:
                    self.voice_output.speak("Great! Keep smiling!", wait=False)
            elif key == 'a':  # Angry
                self.camera_running = False
                camera_window.destroy()
                self.character.set_expression("thinking")
                self.add_sara_message("😤 Kya problem hai? Batao!")
                emotion_response = self.brain.get_motivation()
                self.add_sara_message(emotion_response)
                if not self.is_muted:
                    self.voice_output.speak(emotion_response, wait=False)
        
        camera_window.bind('<Key>', on_key)
        camera_window.focus()
        
        def on_closing():
            self.camera_running = False
            cap.release()
            camera_window.destroy()
        
        camera_window.protocol("WM_DELETE_WINDOW", on_closing)
        self.character.set_expression("happy")


def main():
    root = tk.Tk()
    gui = SARAGui(root, user_name="Ishant")
    root.mainloop()


if __name__ == "__main__":
    main()
