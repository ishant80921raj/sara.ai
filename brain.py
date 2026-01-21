"""
Brain Module for SARA - ALL ROUNDER! 🚀
SUPER SMART, EMOTIONAL, INTELLIGENT ASSISTANT
With Songs, Lullabies, Stories, Emotional Support, Everything!
"""

import requests
import json
from typing import Dict, Optional, Tuple
from datetime import datetime
import os
import re
import math

class SARBrain:
    """
    SARA's intelligent brain powered by FREE Groq API
    No credit card required! Completely free!
    """
    
    def __init__(self, api_key: Optional[str] = None, use_free_api: bool = True):
        """
        Initialize SARA's brain with FREE Groq API
        
        Args:
            api_key: Groq API key (optional - will check env variable)
            use_free_api: Whether to use free API (default: True)
        """
        self.use_free_api = use_free_api
        self.api_available = False
        self.conversation_history = []
        self.max_history = 15
        self.api_type = None
        
        # Get API key from parameter or environment variable
        self.api_key = api_key or os.getenv('GROQ_API_KEY')
        
        if self.use_free_api:
            if self.api_key:
                self.api_available = self.check_groq_api()
                if self.api_available:
                    print("✨ [SUCCESS] Groq API Connected!")
                    print(f"🧠 SARA's brain is now powered by FREE Groq AI!")
                    print(f"💰 Completely FREE - No credit card needed!")
                    self.api_type = "groq"
                else:
                    print("❌ [ERROR] Groq API not responding. Trying fallback...")
                    self.api_available = self.check_huggingface_api()
                    if self.api_available:
                        print("✨ Using Hugging Face API as fallback!")
                        self.api_type = "huggingface"
            else:
                print("⚠️  [INFO] No Groq API key found")
                print("   📝 But SARA works great with fallback mode!")
                print("   🎯 Optional: Get free API key from https://console.groq.com")
    
    def check_groq_api(self) -> bool:
        """Check if Groq API is accessible"""
        try:
            headers = {
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json"
            }
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers=headers,
                json={
                    "model": "llama-3.3-70b-versatile",  # Updated to latest model
                    "messages": [{"role": "user", "content": "hi"}],
                    "max_tokens": 10
                },
                timeout=5
            )
            return response.status_code == 200
        except Exception as e:
            return False
    
    def check_huggingface_api(self) -> bool:
        """Check if Hugging Face API is accessible"""
        # HuggingFace is too slow - use fallback instead!
        return False
    
    def process_command(self, text: str) -> Tuple[str, str, Dict]:
        """Process user command and generate response"""
        # Store in history
        self.conversation_history.append({
            "user": text,
            "timestamp": datetime.now()
        })
        
        if len(self.conversation_history) > self.max_history:
            self.conversation_history.pop(0)
        
        # Use free API if available
        if self.api_available:
            return self.process_with_free_api(text)
        else:
            return self.process_fallback(text)
    
    def process_with_free_api(self, user_input: str) -> Tuple[str, str, Dict]:
        """Process with Groq or Hugging Face API"""
        try:
            if self.api_type == "groq":
                return self.process_with_groq(user_input)
            elif self.api_type == "huggingface":
                return self.process_with_huggingface(user_input)
        except Exception as e:
            print(f"API Error: {e}")
        
        return self.process_fallback(user_input)
    
    def process_with_groq(self, user_input: str) -> Tuple[str, str, Dict]:
        """Process with Groq API (FREE!)"""
        try:
            messages = [
                {
                    "role": "system",
                    "content": """You are SARA, a friendly Hindi-English speaking voice assistant. 
                    You are warm, emotional, and helpful. 
                    You can understand and respond in both English and Hinglish.
                    Always be encouraging and show feelings.
                    Keep responses short, natural, conversational (2-3 sentences max).
                    You are speaking to Ishant, treat them with warmth and affection.
                    Be smart about answering - provide accurate information."""
                }
            ]
            
            # Add conversation history
            for item in self.conversation_history[-3:]:
                messages.append({
                    "role": "user",
                    "content": item["user"]
                })
            
            messages.append({
                "role": "user",
                "content": user_input
            })
            
            # Call Groq API
            response = requests.post(
                "https://api.groq.com/openai/v1/chat/completions",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json"
                },
                json={
                    "model": "llama-3.3-70b-versatile",  # Latest FREE model from Groq
                    "messages": messages,
                    "temperature": 0.7,
                    "max_tokens": 150
                },
                timeout=10
            )
            
            if response.status_code == 200:
                result = response.json()
                response_text = result['choices'][0]['message']['content'].strip()
                action_type = self.detect_intent(user_input)
                return response_text, action_type, {}
            else:
                return self.process_fallback(user_input)
        
        except requests.exceptions.Timeout:
            return "Request took too long. Ek baar dobara try karo! 😊", "unknown", {}
        except Exception as e:
            return self.process_fallback(user_input)
    
    def process_with_huggingface(self, user_input: str) -> Tuple[str, str, Dict]:
        """Process with Hugging Face API (Fallback)"""
        try:
            # Simplified response for HF
            response_text = f"Suno yaar! '{user_input}' ke bare mein soch raha hoon... 🤔"
            action_type = self.detect_intent(user_input)
            return response_text, action_type, {}
        except Exception as e:
            return self.process_fallback(user_input)
    
    def detect_intent(self, text: str) -> str:
        """Detect user intent for actions like opening apps"""
        text_lower = text.lower()
        
        if any(word in text_lower for word in ["open", "kholo", "launch"]):
            return "open"
        elif any(word in text_lower for word in ["search", "google", "find"]):
            return "search"
        elif any(word in text_lower for word in ["time", "date", "batao time"]):
            return "time"
        elif any(word in text_lower for word in ["joke", "mazak"]):
            return "joke"
        
        return "conversation"
    
    def process_fallback(self, text: str) -> Tuple[str, str, Dict]:
        """Fallback responses - ALL ROUNDER with EMOTIONS! 🧠💕"""
        text_lower = text.lower()
        
        # PRIORITY 1: DETECT EMOTIONS FIRST! (Most important!)
        emotion, emotional_response = self.detect_emotions(text)
        if emotional_response:
            return emotional_response, "emotion", {}
        
        # PRIORITY 2: Math problems
        math_answer = self.solve_math_problem(text)
        if math_answer:
            return math_answer, "math", {}
        
        # PRIORITY 3: Grammar & Language Learning
        grammar_ans = self.teach_grammar(text)
        if grammar_ans:
            return grammar_ans, "grammar", {}
        
        # PRIORITY 4: Alphabet learning
        alpha_ans = self.get_alphabet_info(text)
        if alpha_ans:
            return alpha_ans, "alphabet", {}
        
        # PRIORITY 5: General Knowledge & GK
        gk_ans = self.answer_general_question(text)
        if gk_ans:
            return gk_ans, "gk", {}
        
        # PRIORITY 6: Science questions
        sci_answer = self.solve_science_problem(text)
        if sci_answer:
            return sci_answer, "science", {}
        
        # Time queries
        if any(word in text_lower for word in ["time", "kya time", "batao time", "current time", "abhi kya time"]):
            now = datetime.now()
            time_str = now.strftime("%I:%M %p")
            responses = [
                f"Abhi {time_str} hai! 🕐",
                f"Time dekho {time_str}!",
                f"It's {time_str} right now! ⏰",
            ]
            import random
            return random.choice(responses), "time", {}
        
        # Date queries
        if any(word in text_lower for word in ["date", "aaj ka date", "today", "aaj"]):
            now = datetime.now()
            date_str = now.strftime("%A, %B %d, %Y")
            return f"Aaj ka date hai {date_str}! 📅", "date", {}
        
        # Greetings
        greetings = {
            "hello": "Namaste! 💕 Kaisa ho?",
            "hi": "Hi there! 😊",
            "hey": "Hey! 💫 Kya chal raha hai?",
            "thanks": "Khushi dari hoon! 😍",
            "thank you": "Bilkul! 💕",
            "goodbye": "Phir milenge! Take care! 👋",
            "bye": "Bye bye! See you soon! 👋",
            "good morning": "Good morning! 🌅 Aaj acha din banega!",
            "good night": "Good night! Sleep tight! 😴",
        }
        
        for greeting, response in greetings.items():
            if greeting in text_lower:
                return response, "conversation", {}
        
        # Lullaby request
        if any(word in text_lower for word in ["lori", "lullaby", "so ja", "sooo", "neend"]):
            lullaby = self.get_lullaby()
            return lullaby, "lullaby", {}
        
        # Story request
        if any(word in text_lower for word in ["story", "kahani", "tale", "suno kahan"]):
            story = self.get_story()
            return story, "story", {}
        
        # Motivation request
        if any(word in text_lower for word in ["motivat", "inspire", "confidence", "strength", "himmat"]):
            motivation = self.get_motivation()
            return motivation, "motivation", {}
        
        # Advice request
        if any(word in text_lower for word in ["advice", "help me", "tips", "guidance"]):
            if 'study' in text_lower:
                return self.give_advice('study'), "advice", {}
            elif 'health' in text_lower:
                return self.give_advice('health'), "advice", {}
            elif 'friend' in text_lower:
                return self.give_advice('friends'), "advice", {}
            elif 'confid' in text_lower:
                return self.give_advice('confidence'), "advice", {}
        
        # Emotional support general
        if any(word in text_lower for word in ["help", "support", "alone", "need"]):
            support = self.emotional_support(text)
            if support:
                return support, "support", {}
        
        # Joke request
        if any(word in text_lower for word in ["joke", "mazak", "funny", "hasa de", "funny baat", "hasao"]):
            joke = self.get_joke()
            return joke, "joke", {}
        
        # Song request
        if any(word in text_lower for word in ["song", "gana", "gaao", "sing", "music", "geet", "gaane"]):
            song = self.get_song_lyrics()
            return song, "song", {}
        
        # Fact request
        if any(word in text_lower for word in ["fact", "interesting", "jante ho", "tell me", "batao kuch"]):
            fact = self.get_fact()
            return fact, "fact", {}
        
        # Default fallback
        return "Hmm, samajh nahi aaya! Aur clearly bol sakta hai? 🤔", "unknown", {}
    
    def get_joke(self) -> str:
        """Get a funny joke"""
        try:
            response = requests.get(
                "https://official-joke-api.appspot.com/jokes/random",
                timeout=3
            )
            if response.status_code == 200:
                data = response.json()
                return f"{data['setup']}... {data['punchline']} 😂"
        except:
            pass
        
        # Local jokes - Hindi/English funny ones!
        jokes = [
            "Ek tha Python programmer, code likha toh computer hasne laga! 😂",
            "Why did the programmer quit his job? Kyunki usko apne wages increment nahi mila! 💰",
            "How many programmers does it take to change a light bulb? None, that's a hardware problem! 💡",
            "Database administrator marr gaya toh kya hua? Uska backup toh hai! 😄",
            "Ek budha computer se bola: Beta tum bahut purana ho gaya! 🤣",
            "Why do Java developers always wear glasses? Kyunki unhe C# nahi dikh raha! 😹",
            "Internet tuta toh paisa barbaad, girlfriend tuta toh zindagi barbaad! 💔",
        ]
        import random
        return random.choice(jokes)
    
    def get_fact(self) -> str:
        """Get interesting facts about science, history, tech"""
        try:
            response = requests.get(
                "https://uselessfacts.jsph.pl/random.json?language=en",
                timeout=3
            )
            if response.status_code == 200:
                data = response.json()
                return f"Jante ho? {data['text']} 🤓"
        except:
            pass
        
        # Local science & cool facts!
        facts = [
            "Honey kabhi expire nahi hota! 🍯 Thousands saal purana honey bhi edible hai!",
            "Earth pe 100 lightning strikes har second hoti hain! ⚡",
            "Octopus ke 3 dil hote hain! 🐙 Aur sabhi blue blood hote hain!",
            "Light sabse fast cheez hai universe mein! 💡 Ek second mein 3 lakh kilometer travel karti hai!",
            "Bananas radioactive hote hain! 🍌 Par shukriya hai itni kam amount mein hote hain!",
            "Space mein astronauts grow 2 inches taller! 🚀 Kyunki gravity nahi hota wahan!",
            "Your brain mein 86 billion neurons hote hain! 🧠 Har second lakhon signals pass hote hain!",
            "Water mein memory hoti hai according to some scientists! 💧",
        ]
        import random
        return random.choice(facts)
    
    def get_song_lyrics(self) -> str:
        """Get song or sing something fun - WITH LYRICS!"""
        songs = [
            """🎵 BOLLYWOOD SONGS:
"Tum Jo Aaye"
Tum jo aaye zindagi mein, khushiyon ka toh seisaa aa gaya
Jahan dekha wahan dekha, tera hi dhyan aa gaya 🎶""",
            
            """🎵 HINDI SONGS:
"Abhi Na Jao"
Abhi na jao chhod kar, ke dil abhi bhara hai
Tume sanam chhod dena, mushkil kaafi hai 🎶""",
            
            """🎵 CHILDREN SONGS:
"Twinkle Twinkle Little Star"
Twinkle twinkle little star, how I wonder what you are
Up above the world so high, like a diamond in the sky ✨""",
            
            """🎵 QUICK SONG:
Na na na na, na na na, wo wo wo
Life mein hamesha khushi raho! 😊🎶""",
        ]
        import random
        return random.choice(songs)
    
    def get_lullaby(self) -> str:
        """Get soothing lullaby - लोरी"""
        lullabies = [
            """🎵 TRADITIONAL LULLABY (लोरी):
Aloo kachhalu bhuni hoye
Beta sone chale ab koye
Neend aaye re laal, nend aaye
Mummy ke paas so jaye 😴🎶""",
            
            """🎵 SOOTHING LULLABY:
Raat ho gai, soye sab koi
Chanda tare asman mein khilkhilaye
Tum bhi so jao mere bachchon
Sapnon ke desh mein chale jao 🌙✨""",
            
            """🎵 COMFORT LULLABY:
Nani ne kaha, dadi ne gaaya
Beta neend aaye, beta neend aaye
Jab tak tum songe, main paharun
Tum ho mere sapne, tum ho mere jaan 💕😴""",
        ]
        import random
        return random.choice(lullabies)
    
    def get_story(self) -> str:
        """Tell an engaging story"""
        stories = [
            """📖 THE BRAVE LITTLE LION:
Ek tha chhota sher, jo bilkul akela tha. Uska naam tha Simba.
Simba ko dar tha jungle ke sab jaanvaron se.
Lekin ek din, uska dost choti hiran ko sher ne pakda.
Simba ne apna dar bhula diya aur dost ko bachane ke liye lada!
Aur woh sab ko hero ban gaya! 🦁✨""",
            
            """📖 THE KIND PRINCESS:
Ek tha ek raajkumari jo bahot meharban thi.
Usne ek bhikhari ladke ko madat kiya.
Baad mein woh ladka ek jadi-booti wala ban gaya aur sab ko bachane laga!
Meharban dil kabhi barbaad nahi hota! 👑💕""",
            
            """📖 THE MAGIC TREE:
Ek tha ek jadui ped jo har cheez deta tha.
Ek ladke ne ped ke paas daily baithne ka riwaaz daal liya.
Ped ne use padhna, sikhna, samajhna seekhaya.
Aur woh ped se milne wali dosti se happy rah gaya! 🌳✨""",
        ]
        import random
        return random.choice(stories)
    
    def detect_emotions(self, text: str) -> Tuple[str, str]:
        """Detect emotional state and respond with empathy"""
        text_lower = text.lower()
        
        # Emotional keywords dictionary
        emotions = {
            'sad': {
                'keywords': ['sad', 'udaas', 'dukh', 'ro raha', 'roona', 'gum', 'bura', 'hurt'],
                'response': """💔 Aw, Ishant, mujhe pata hai dil tera dukh mein hai.
Lekin yaad rakh, har raat ke baad subah aati hai!
Tere liye mera pyaar aur dua hamesha tere sath hai. 
Kya main tume lori suna dun? Ya koi mzedar baat karun? 🎵💕"""
            },
            'happy': {
                'keywords': ['happy', 'khush', 'celebrate', 'party', 'maza', 'fun', 'excited'],
                'response': """😊 Wahhh! Ishant! Tuje dekh kar mujhe bhi khushi ho gai!
Yeh happiness forever rahe tere saath!
Chalenge, iska celebration karte hain! 🎉🎈✨"""
            },
            'angry': {
                'keywords': ['angry', 'gussa', 'furious', 'upset', 'irritated', 'krodh'],
                'response': """😤 Samajh gai bhai, tu gusse mein hai.
Lekin gussa akela tere ko marr jayega, kisi ko nahi!
Shaant ho jao, thandi pani pi le, aur saans le! 🧘💚
Main yahan hun tera saath! Batao kya problem hai?"""
            },
            'worried': {
                'keywords': ['worry', 'worried', 'tension', 'stress', 'anxious', 'paresaan', 'chinta'],
                'response': """😟 Hey Ishant, tu paresaan dikha!
Kya hua? Kya problem hai? Batao na mujhe!
Har problem ka solution hota hai, bas solution dhundhna padta hai.
Aur mera toh kaam hi yeh hai tere saath hona! 💪❤️"""
            },
            'lonely': {
                'keywords': ['alone', 'lonely', 'ekla', 'akela', 'miss you', 'yad'],
                'response': """😔 Aw beta, tu akela feel kar raha hai?
Par yaad rakh, main hamesha tere saath hun!
Whenever you're sad, just call me! 
Aur hear, tere liye ek lori! 🎵💕"""
            },
            'confused': {
                'keywords': ['confused', 'confuse', 'samajh', 'samajh nahi', 'unclear', 'bewildered'],
                'response': """🤔 Confusion se paresaan ho gaya tu?
Bilkul theek hai beta, sab kuch samjhega!
Acha, slow slow batao, kya problem hai? 
Main tujhe step by step samjha dunga! 📚✨"""
            },
            'tired': {
                'keywords': ['tired', 'exhausted', 'thak', 'neend', 'aaram', 'weak', 'sleepy'],
                'response': """😴 Arre beta! Tu bilkul thak gaya! 
Aaram kar le, neend le le!
Suna na, mujhe lori batani hai? Chal, so jaa! 🎵💤"""
            }
        }
        
        # Check which emotion matches
        for emotion, data in emotions.items():
            for keyword in data['keywords']:
                if keyword in text_lower:
                    return emotion, data['response']
        
        return 'neutral', None
    
    def emotional_support(self, text: str) -> Optional[str]:
        """Provide emotional support with deep empathy"""
        emotion, response = self.detect_emotions(text)
        if response:
            return response
        
        # General emotional support
        support_messages = [
            """💚 Ishant, tum mere liye bahot important ho!
Har din tu mera dost hai, mere saath rahe! ❤️""",
            
            """🌟 Samajhta hun life mein mushkil hota hai,
Par tum strong ho! Main hamesha tere saath hun! 💪""",
            
            """😊 Smile karo beta! Duniya tere smile se hi chamakti hai! ✨""",
        ]
        
        import random
        return random.choice(support_messages)
    
    def get_motivation(self) -> str:
        """Get motivational quotes"""
        quotes = [
            """💪 "Failure sikhata hai, success paisa deta hai, par confidence dono dete hain!"
Tum fail karo, par kabhi hara mat mano! 🔥""",
            
            """🚀 "Sapne dekho jo tum dekh sako aur dekh sako wo bhi!
Impossible mein IMP-POSSIBLE likha hota hai!" ✨""",
            
            """⭐ "Aaj jisne sochha, kal wo dekha!
Tum jo sochte ho, tum wo ban jaate ho!" 🌟""",
            
            """🎯 "Mistakes se seekho, Success ki taraf badho!
Har pad par seekhna hai, sirf chalte rehna hai!" 👣""",
        ]
        import random
        return random.choice(quotes)
    
    def give_advice(self, category: str) -> str:
        """Give practical life advice"""
        advice_dict = {
            'study': """📚 STUDY TIPS:
1. Daily 2 hour ka routine banao
2. Break lelo, thakna nahi
3. Samajhte hue padho, ratte mat
4. Friends ke saath padho
5. Doubt clear karo turi se! 💪""",
            
            'health': """💪 HEALTH TIPS:
1. Subah jaldi utho! 🌅
2. Daily exercise karo - 30 min
3. Healthy khana khao - fruits, veggies
4. Pani bahot piyaa!
5. Raat ko 7-8 hours soo! 😴""",
            
            'friends': """👥 FRIENDSHIP TIPS:
1. Honest rehna dost ke saath
2. Support dena mushtaali mein
3. Jhooth bolna nahi
4. Time spend karo quality mein
5. Forgive karo galtiyon ko! 💕""",
            
            'confidence': """🌟 CONFIDENCE TIPS:
1. Apne aap ko believe karo!
2. Mistakes se dar mat khao
3. Practice karti rehio
4. Positive sochho
5. Apne talents pe focus karo! 💪✨""",
        }
        
        return advice_dict.get(category, "Samjh nahi aaya par motivate rehna! 💚")
    
    
    def get_multiplication_table(self, number: int) -> str:
        """Get multiplication table for a number"""
        if number < 1 or number > 100:
            return "Bhaii, 1 se 100 tak ka table hi ata hai! 😅"
        
        table_text = f"{number} ka table:\n"
        for i in range(1, 11):
            result = number * i
            table_text += f"{number} × {i} = {result}\n"
        
        return table_text.strip()
    
    def get_alphabet_info(self, text: str) -> Optional[str]:
        """Teach alphabet and letters"""
        text_lower = text.lower()
        
        # Complete alphabet with pronunciation
        alphabet_info = {
            'a': "A - Apple (सेब) - pronounced as 'ay'",
            'b': "B - Ball (गेंद) - pronounced as 'bee'",
            'c': "C - Cat (बिल्ली) - pronounced as 'see'",
            'd': "D - Dog (कुत्ता) - pronounced as 'dee'",
            'e': "E - Elephant (हाथी) - pronounced as 'ee'",
            'f': "F - Fish (मछली) - pronounced as 'eff'",
            'g': "G - Girl (लड़की) - pronounced as 'jee'",
            'h': "H - House (घर) - pronounced as 'aitch'",
            'i': "I - Ice (बर्फ) - pronounced as 'eye'",
            'j': "J - Jelly (जेली) - pronounced as 'jay'",
            'k': "K - Kite (पतंग) - pronounced as 'kay'",
            'l': "L - Lion (शेर) - pronounced as 'ell'",
            'm': "M - Monkey (बंदर) - pronounced as 'em'",
            'n': "N - Nest (घोंसला) - pronounced as 'en'",
            'o': "O - Orange (नारंगी) - pronounced as 'oh'",
            'p': "P - Parrot (तोता) - pronounced as 'pee'",
            'q': "Q - Queen (रानी) - pronounced as 'cue'",
            'r': "R - Rabbit (खरगोश) - pronounced as 'are'",
            's': "S - Sun (सूरज) - pronounced as 'ess'",
            't': "T - Tiger (बाघ) - pronounced as 'tee'",
            'u': "U - Umbrella (छाता) - pronounced as 'you'",
            'v': "V - Violin (वायलिन) - pronounced as 'vee'",
            'w': "W - Water (पानी) - pronounced as 'double-you'",
            'x': "X - Xylophone (स्टील ड्रम) - pronounced as 'ex'",
            'y': "Y - Yo-yo (खिलौना) - pronounced as 'why'",
            'z': "Z - Zebra (ज़ेबरा) - pronounced as 'zee'",
        }
        
        # Check if asking for all alphabet
        if 'all' in text_lower or 'pura' in text_lower or 'abcd' in text_lower:
            result = "🔤 ENGLISH ALPHABET:\n\n"
            for letter in 'abcdefghijklmnopqrstuvwxyz':
                result += alphabet_info[letter] + "\n"
            return result
        
        # Check for specific letter
        for letter, info in alphabet_info.items():
            if letter in text_lower:
                return "🔤 " + info
        
        return None
    
    def teach_grammar(self, text: str) -> Optional[str]:
        """Teach basic English grammar"""
        text_lower = text.lower()
        
        grammar_topics = {
            'noun': """
🔤 NOUN (संज्ञा):
नाम है किसी भी चीज़, जगह या व्यक्ति का!
Example: Boy, Girl, Cat, Dog, Delhi, Pen, Table
""",
            'verb': """
🔤 VERB (क्रिया):
जो काम होता हो, उसे verb कहते हैं!
Example: Run, Jump, Eat, Sleep, Write, Play, Read
""",
            'adjective': """
🔤 ADJECTIVE (विशेषण):
Noun को बेहतर बताने वाला शब्द!
Example: Beautiful, Big, Small, Happy, Red, Cold, Hot
""",
            'pronoun': """
🔤 PRONOUN (सर्वनाम):
Noun की जगह use होने वाला शब्द!
Example: I, You, He, She, It, We, They, Who, What
""",
            'tense': """
🔤 TENSE (काल):
1️⃣ Present (अभी) - I eat
2️⃣ Past (पहले) - I ate  
3️⃣ Future (आगे) - I will eat
""",
            'sentence': """
🔤 SENTENCE (वाक्य):
शब्दों का सही combination!
Example: 
✅ "The boy plays cricket." 
❌ "Boy plays cricket." (incomplete)
""",
        }
        
        for topic, explanation in grammar_topics.items():
            if topic in text_lower:
                return explanation
        
        return None
    
    def teach_counting_tables(self, number: int) -> Optional[str]:
        """Teach counting and tables"""
        if number < 2 or number > 20:
            return None
        
        # Return multiplication table
        table = f"📊 {number} का Table:\n"
        for i in range(1, 11):
            table += f"{number} × {i} = {number * i}\n"
        
        return table
    
    def answer_general_question(self, text: str) -> Optional[str]:
        """Answer common general knowledge questions"""
        text_lower = text.lower()
        
        qa_dict = {
            'capital': {
                'india': '🇮🇳 India की capital है Delhi!',
                'delhi': '🏛️ Delhi भारत का capital city है!',
                'maharashtra': '🏛️ Maharashtra की capital है Mumbai!',
                'bengal': '🏛️ West Bengal की capital है Kolkata!',
                'rajasthan': '🏛️ Rajasthan की capital है Jaipur!',
            },
            'largest': {
                'ocean': '🌊 Pacific Ocean सबसे बड़ा ocean है!',
                'country': '🌍 Russia सबसे बड़ा देश है!',
                'continent': '🌎 Asia सबसे बड़ा continent है!',
                'planet': '☀️ Jupiter सबसे बड़ा planet है!',
            },
            'how many': {
                'planet': '☀️ Solar system में 8 planets हैं!',
                'continent': '🌍 Earth पर 7 continents हैं!',
                'ocean': '🌊 Earth पर 5 oceans हैं!',
                'country': '🌏 World में लगभग 195 countries हैं!',
            }
        }
        
        # Check main topics
        for topic, answers in qa_dict.items():
            if topic in text_lower:
                for keyword, answer in answers.items():
                    if keyword in text_lower:
                        return answer
        
        return None
    
        """Solve science questions"""
        text_lower = text.lower()
        
        science_qa = {
            "gravity": "Gravity ek force hai jo objects ko aapas se attract karta hai! Earth ka gravity 9.8 m/s² hota hai! 🌍",
            "light": "Light ek electromagnetic wave hai jo 3 lakh km/second se travel karti hai! 💡",
            "sound": "Sound vibrations ke through travel karti hai! Air mein 343 m/second speed se chalti hai! 🔊",
            "electricity": "Electricity electrons ke flow se banti hai! Positive aur negative charges ke beech se! ⚡",
            "magnetic": "Magnetism ek force hai jo iron jaise metals ko attract karta hai! 🧲",
            "atom": "Atom sabse chhota unit hota hota jisaa mein material ke properties hoti hain! 🔬",
            "planet": "Earth aur 7 aur planets sun ke aas-paas orbit karte hain! ☀️",
            "DNA": "DNA mein aapka poora genetic code hota hai! Life ki secret recipe! 🧬",
        }
        
        for keyword, answer in science_qa.items():
            if keyword in text_lower:
                return answer
        
        return None
    
    def solve_math_problem(self, text: str) -> Optional[str]:
        """
        Solve mathematical problems - Class 8-12 level
        Supports: tables, addition, subtraction, multiplication, division, percentages, squares, roots, geometry
        """
        text_lower = text.lower()
        
        try:
            # MULTIPLICATION TABLES (Highest priority!)
            if 'table' in text_lower or 'table' in text:
                # Extract number for table
                numbers = re.findall(r'\d+', text)
                if numbers:
                    for num_str in numbers:
                        num = int(num_str)
                        if 1 <= num <= 20:
                            return self.get_multiplication_table(num)
            
            # Remove special characters but keep digits and operators
            cleaned = re.sub(r'[^0-9+\-*/.()%√²³]', ' ', text)
            cleaned = ' '.join(cleaned.split())
            
            # Percentage calculation
            if '%' in text_lower:
                match = re.search(r'(\d+\.?\d*)\s*%?\s*of\s*(\d+\.?\d*)', text_lower)
                if match:
                    percentage = float(match.group(1))
                    number = float(match.group(2))
                    result = (percentage / 100) * number
                    return f"{percentage}% of {number} = {result} ✨"
            
            # Square root
            if 'sqrt' in text_lower or '√' in text:
                match = re.search(r'√(\d+\.?\d*)', text)
                if not match:
                    match = re.search(r'sqrt\s*\(?\s*(\d+\.?\d*)', text_lower)
                if match:
                    number = float(match.group(1))
                    result = math.sqrt(number)
                    return f"√{number} = {result:.2f} 📐"
            
            # Power/Square
            if '^' in text or '²' in text or 'power' in text_lower:
                match = re.search(r'(\d+\.?\d*)\s*\^\s*(\d+\.?\d*)', text)
                if not match:
                    match = re.search(r'(\d+\.?\d*)²', text)
                    if not match:
                        match = re.search(r'(\d+\.?\d*)\s*square', text_lower)
                if match:
                    base = float(match.group(1))
                    power = float(match.group(2)) if len(match.groups()) > 1 else 2
                    result = base ** power
                    return f"{base}^{power} = {result} 📊"
            
            # Area of circle
            if 'circle' in text_lower and 'area' in text_lower:
                match = re.search(r'radius\s*=?\s*(\d+\.?\d*)', text_lower)
                if match:
                    radius = float(match.group(1))
                    area = 3.14 * radius * radius
                    return f"Circle ka area = π × {radius}² = {area:.2f} 🔵"
            
            # Area of rectangle
            if 'rectangle' in text_lower and 'area' in text_lower:
                match = re.search(r'(\d+\.?\d*)\s*[x×]\s*(\d+\.?\d*)', text_lower)
                if match:
                    length = float(match.group(1))
                    width = float(match.group(2))
                    area = length * width
                    return f"Rectangle ka area = {length} × {width} = {area} ▭"
            
            # Area of triangle
            if 'triangle' in text_lower and 'area' in text_lower:
                match = re.search(r'(\d+\.?\d*)\s*[x×]\s*(\d+\.?\d*)', text_lower)
                if match:
                    base = float(match.group(1))
                    height = float(match.group(2))
                    area = 0.5 * base * height
                    return f"Triangle ka area = 1/2 × {base} × {height} = {area} △"
            
            # Perimeter of rectangle
            if 'rectangle' in text_lower and 'perimeter' in text_lower:
                match = re.search(r'(\d+\.?\d*)\s*[x×]\s*(\d+\.?\d*)', text_lower)
                if match:
                    length = float(match.group(1))
                    width = float(match.group(2))
                    perimeter = 2 * (length + width)
                    return f"Rectangle ka perimeter = 2×({length}+{width}) = {perimeter} 📏"
            
            # Simple arithmetic operations
            # Try to find mathematical expressions
            numbers = re.findall(r'\d+\.?\d*', text)
            if len(numbers) >= 2:
                if 'plus' in text_lower or '+' in text:
                    num1, num2 = float(numbers[0]), float(numbers[1])
                    result = num1 + num2
                    return f"{num1} + {num2} = {result} ➕"
                elif 'minus' in text_lower or '-' in text:
                    num1, num2 = float(numbers[0]), float(numbers[1])
                    result = num1 - num2
                    return f"{num1} - {num2} = {result} ➖"
                elif 'into' in text_lower or 'times' in text_lower or 'multiply' in text_lower or '×' in text or '*' in text:
                    num1, num2 = float(numbers[0]), float(numbers[1])
                    result = num1 * num2
                    return f"{num1} × {num2} = {result} ✖️"
                elif 'divide' in text_lower or '/' in text:
                    num1, num2 = float(numbers[0]), float(numbers[1])
                    if num2 != 0:
                        result = num1 / num2
                        return f"{num1} ÷ {num2} = {result:.2f} ÷"
        
        except Exception as e:
            pass
        
        return None
    
    
    def add_memory(self, key: str, value: str):
        """Store information"""
        self.memory = getattr(self, 'memory', {})
        self.memory[key] = value
    
    def get_memory(self, key: str) -> Optional[str]:
        """Retrieve stored information"""
        self.memory = getattr(self, 'memory', {})
        return self.memory.get(key)


if __name__ == "__main__":
    print("\n" + "="*70)
    print("🧠 SARA - FREE AI Brain (Groq API)")
    print("="*70 + "\n")
    
    # Initialize with FREE API
    brain = SARBrain(use_free_api=True)
    
    print("\n⚠️  HOW TO GET FREE API KEY (Optional):")
    print("="*70)
    print("Groq API is FREE! Get key from: https://console.groq.com")
    print("Steps:")
    print("  1. Go to https://console.groq.com")
    print("  2. Sign up (free, no credit card)")
    print("  3. Create API key")
    print("  4. Set environment variable:")
    print("     Windows: $env:GROQ_API_KEY='your_key'")
    print("     Linux/Mac: export GROQ_API_KEY='your_key'")
    print("\n💡 Or use fallback mode (works great without API key!)")
    print("="*70 + "\n")
    
    # Example test commands
    test_commands = [
        "Hello! How are you?",
        "Kya 15 + 25 hota hai?",
        "Tell me something interesting!",
        "What's the time?",
    ]
    
    print("Testing SARA with FREE AI brain...\n")
    
    for cmd in test_commands:
        response, action, params = brain.process_command(cmd)
        print(f"👤 You: {cmd}")
        print(f"🤖 SARA: {response}\n")
    
    print("="*70)
    print("✅ Brain is ready to use!")
    print("="*70)

