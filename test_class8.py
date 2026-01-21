#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Test SARA's Class 8 Level Intelligence"""

from brain import SARBrain

print("\n" + "="*70)
print("🧠 SARA - CLASS 8TH LEVEL INTELLIGENCE TEST")
print("="*70 + "\n")

# Initialize brain
brain = SARBrain(api_key='invalid_test')

# Test cases
test_cases = {
    "📊 Multiplication Tables": [
        "5 ka table",
        "table 12",
        "10 times",
    ],
    "🔤 Alphabet": [
        "ABCD sikhao",
        "A letter",
        "alphabet",
    ],
    "📚 Grammar": [
        "noun kya hai",
        "verb samjhao",
        "adjective batao",
    ],
    "🌍 General Knowledge": [
        "India ka capital",
        "largest planet",
        "capitals of states",
    ],
    "🧮 Math": [
        "5 + 3",
        "10 minus 4",
        "sqrt 144",
        "12 times 8",
    ],
    "🔬 Science": [
        "gravity kya hai",
        "light speed",
        "DNA kya hota hai",
    ]
}

for category, questions in test_cases.items():
    print(f"\n{category}")
    print("-" * 70)
    
    for question in questions:
        try:
            response, action, _ = brain.process_command(question)
            print(f"\nQ: {question}")
            print(f"A: {response}\n")
        except Exception as e:
            print(f"Error in '{question}': {e}\n")

print("\n" + "="*70)
print("✅ Test Complete!")
print("="*70)
