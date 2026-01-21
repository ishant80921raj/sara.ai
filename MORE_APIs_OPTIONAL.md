# 🔥 ADVANCED: SARA WITH MORE FREE APIs (OPTIONAL)

Want even MORE features? Here are additional FREE APIs you can add!

---

## 🌤️ WEATHER API
**Free Forever, No Auth Needed**

```python
def get_weather_api(self, city: str = "Delhi") -> str:
    """Get weather for any city - NO API KEY!"""
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3",
            timeout=3
        )
        if response.status_code == 200:
            weather = response.text
            return f"Weather report: {weather} 🌤️"
    except:
        pass
    return "Cloud cover visible... kya pata weather kya hai! ☁️"
```

**Try saying:**
- "weather batao"
- "bahar kaisa hai"
- "Delhi ka weather"

---

## 📰 NEWS API (FREE TIER)
**NewsAPI - Latest News**

```python
def get_latest_news(self) -> str:
    """Get latest news headlines"""
    try:
        response = requests.get(
            "https://newsapi.org/v2/top-headlines?country=in&apiKey=demo",
            timeout=3
        )
        if response.status_code == 200:
            articles = response.json()['articles']
            headline = articles[0]['title']
            return f"Breaking! {headline} 📰"
    except:
        pass
    return "Latest news dekh raha hoon... ek second! 📻"
```

**Try saying:**
- "news de"
- "latest news"
- "kya chal raha hai duniya mein"

---

## 🦸 SUPERHERO API
**Get Superhero Info - Completely FREE**

```python
def get_superhero_info(self) -> str:
    """Get random superhero details"""
    try:
        import random
        hero_id = random.randint(1, 643)
        response = requests.get(
            f"https://superheroapi.com/api/10123456789/{hero_id}",
            timeout=3
        )
        if response.status_code == 200:
            hero = response.json()
            name = hero.get('name', 'Unknown')
            power = hero['powerstats'].get('strength', 'Mystery')
            return f"Superhero: {name} with strength {power}! 🦸"
    except:
        pass
    return "Ek superhero soch raha hoon... Batman? Superman? 🦸"
```

**Try saying:**
- "superhero batao"
- "kaunsa superhero"
- "hero ke baare mein"

---

## 🎮 POKEMON API
**Get Random Pokemon - Completely FREE**

```python
def get_pokemon_info(self) -> str:
    """Get random Pokemon details"""
    try:
        import random
        poke_id = random.randint(1, 898)
        response = requests.get(
            f"https://pokeapi.co/api/v2/pokemon/{poke_id}/",
            timeout=3
        )
        if response.status_code == 200:
            pokemon = response.json()
            name = pokemon['name'].capitalize()
            height = pokemon['height']
            return f"Pokemon: {name}! Height: {height}dm 🎮"
    except:
        pass
    return "Pokemon catch kar raha hoon... pikachu? 🎮"
```

**Try saying:**
- "pokemon batao"
- "kaunsa pokemon"
- "random pokemon"

---

## ✈️ FLIGHTS API
**Random Airline Info - Completely FREE**

```python
def get_airline_info(self) -> str:
    """Get random airline details"""
    try:
        response = requests.get(
            "https://api.api-ninjas.com/v1/airlines",
            timeout=3
        )
        if response.status_code == 200:
            airlines = response.json()
            airline = airlines[0]
            name = airline.get('name', 'Unknown')
            country = airline.get('country', 'Unknown')
            return f"Airline: {name} from {country} ✈️"
    except:
        pass
    return "Ek airline book kar raha hoon! ✈️"
```

---

## 📚 BOOK API
**Get Random Book Info - Completely FREE**

```python
def get_book_info(self) -> str:
    """Get random book details"""
    try:
        response = requests.get(
            "https://openlibrary.org/search.json?q=python&limit=1",
            timeout=3
        )
        if response.status_code == 200:
            book = response.json()['docs'][0]
            title = book.get('title', 'Unknown')
            author = book.get('author_name', ['Unknown'])[0]
            return f"Book: '{title}' by {author} 📚"
    except:
        pass
    return "Ek book padh raha hoon! 📚"
```

**Try saying:**
- "book recommendation"
- "kitaab batao"
- "interesting book"

---

## 🍕 FOOD API
**Get Random Recipe - Completely FREE**

```python
def get_recipe(self) -> str:
    """Get random recipe"""
    try:
        response = requests.get(
            "https://www.themealdb.com/api/json/v1/1/random.php",
            timeout=3
        )
        if response.status_code == 200:
            meal = response.json()['meals'][0]
            name = meal['strMeal']
            cuisine = meal['strArea']
            return f"Recipe: {name} ({cuisine} cuisine) 🍕"
    except:
        pass
    return "Recipe dekh raha hoon! 🍳"
```

**Try saying:**
- "recipe sunao"
- "khana banana seekho"
- "kya banaio aj"

---

## 🎬 MOVIE API
**Get Random Movie - Completely FREE**

```python
def get_movie_info(self) -> str:
    """Get random movie details"""
    try:
        import random
        movie_id = random.randint(1, 500000)
        response = requests.get(
            f"https://yts.mx/api/v2/movie_details.json?movie_id={movie_id}",
            timeout=3
        )
        if response.status_code == 200:
            movie = response.json()['data']['movie']
            title = movie['title']
            rating = movie['rating']
            return f"Movie: {title} (Rating: {rating}/10) 🎬"
    except:
        pass
    return "Movie search kar raha hoon! 🎬"
```

**Try saying:**
- "movie recommendation"
- "film batao"
- "kya dekhu aaj"

---

## 🏆 SPORTS API
**Get Sports Scores - Free Tier Available**

```python
def get_sports_score(self) -> str:
    """Get latest sports updates"""
    try:
        response = requests.get(
            "https://api.api-sports.io/v1/odds?league=6&date=2024-01-21",
            timeout=3
        )
        if response.status_code == 200:
            data = response.json()
            return f"Sports update: Latest matches live! 🏆"
    except:
        pass
    return "Sports match dekh raha hoon! ⚽"
```

---

## 📍 LOCATION API
**Get Random Location - Completely FREE**

```python
def get_random_location(self) -> str:
    """Get random city coordinates"""
    try:
        response = requests.get(
            "https://nominatim.openstreetmap.org/search?q=india&format=json",
            timeout=3
        )
        if response.status_code == 200:
            location = response.json()[0]
            place = location['address']['city']
            return f"Location: {place}, India 📍"
    except:
        pass
    return "Location search kar raha hoon! 🗺️"
```

---

## 🎵 MUSIC API
**Get Random Song Info - Completely FREE**

```python
def get_random_song(self) -> str:
    """Get random song details"""
    try:
        response = requests.get(
            "https://www.jukebox.rocks/api/random",
            timeout=3
        )
        if response.status_code == 200:
            song = response.json()
            title = song.get('title', 'Unknown')
            artist = song.get('artist', 'Unknown')
            return f"Song: '{title}' by {artist} 🎵"
    except:
        pass
    return "Ek gaana search kar raha hoon! 🎵"
```

---

## HOW TO ADD MORE APIs

1. **Create Function:**
```python
def get_new_api(self) -> str:
    """Get data from new API"""
    try:
        response = requests.get("API_URL", timeout=3)
        if response.status_code == 200:
            data = response.json()
            return "Formatted response"
    except:
        return "Fallback response"
```

2. **Add to process_command():**
```python
if any(word in text for word in ["trigger_words"]):
    return self.get_new_api(), "category", {}
```

3. **Test:**
```bash
python test_apis.py
```

---

## ⚡ ALL FREE API SOURCES

| API | Type | Link | Auth |
|-----|------|------|------|
| Open Weather | Weather | openweathermap.org | Free |
| NewsAPI | News | newsapi.org | Free tier |
| Superhero | Heroes | superheroapi.com | Free |
| PokéAPI | Pokemon | pokeapi.co | Free |
| API Ninjas | Airlines | api-ninjas.com | Free tier |
| OpenLibrary | Books | openlibrary.org | Free |
| TheMealDB | Recipes | themealdb.com | Free |
| YTS API | Movies | yts.mx | Free |
| API Sports | Sports | api-sports.io | Free tier |
| OpenStreetMap | Location | nominatim.openstreetmap.org | Free |

---

## 🎯 IMPLEMENTATION ORDER

**Easy to Hard:**

1. **Weather API** - Simple 1 endpoint
2. **Pokemon API** - Random fetching
3. **Superhero API** - Similar pattern
4. **News API** - Slightly complex
5. **Sports API** - More complex
6. **Movie API** - Complex filtering

---

## 🚀 QUICK ADD EXAMPLE

Want to add Weather? Easy!

```python
# Add to brain.py

def get_weather(self, city: str = "Delhi") -> str:
    try:
        response = requests.get(
            f"https://wttr.in/{city}?format=3",
            timeout=3
        )
        return response.text + " 🌤️"
    except:
        return "Weather data fetch nahi ho paya!"

# In process_command(), add:
if any(word in text for word in ["weather", "bahar", "mausam"]):
    city = "Delhi"  # or extract from command
    return self.get_weather(city), "weather", {}
```

That's it! SARA now has weather! 🌤️

---

## 💡 CURRENT STATUS

✅ **Integrated APIs:**
- Jokes
- Facts
- Quotes
- Advice
- Random People

🔥 **Ready to Add:**
- Weather
- News
- Pokemon
- Movies
- Sports
- And 10+ more!

---

## 🎊 POSSIBILITIES ARE ENDLESS!

Mix and match APIs to create:
- **Motivational Bot** - Quotes + Advice
- **Fun Bot** - Jokes + Facts + Pokemon
- **News Reader** - News + Sports + Weather
- **Travel Bot** - Weather + Flights + Hotels
- **Entertainment Bot** - Movies + Music + Games
- **Educational Bot** - Facts + Books + Wikipedia

---

**SARA ko bahut mast banao with unlimited FREE APIs!** 💜🚀
