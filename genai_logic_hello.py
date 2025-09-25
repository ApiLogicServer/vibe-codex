#!/usr/bin/env python3
"""
GenAI-Logic Hello World Example

This module demonstrates a simple integration of:
1. GenAI capabilities (text generation)
2. Logic processing (rule-based decision making)
3. Hello World functionality
"""

import random
from typing import Dict, List, Any


class GenAILogicHello:
    """A simple Hello World implementation combining GenAI and Logic capabilities."""
    
    def __init__(self):
        # Simple GenAI templates for text generation
        self.greeting_templates = [
            "Hello, {name}! Welcome to the world of GenAI-Logic!",
            "Greetings, {name}! Let's explore AI-powered logic together!",
            "Hi there, {name}! Ready for some intelligent decision making?",
            "Welcome, {name}! Time to blend AI creativity with logical thinking!"
        ]
        
        # Logic rules for different scenarios
        self.logic_rules = {
            "time_based": {
                "morning": "Good morning! Perfect time for fresh AI insights.",
                "afternoon": "Good afternoon! Let's process some logical decisions.",
                "evening": "Good evening! Time to reflect on AI-driven solutions."
            },
            "mood_based": {
                "excited": "Your excitement fuels great AI creativity!",
                "curious": "Curiosity drives the best logical explorations!",
                "focused": "Focus enhances both AI generation and logical reasoning!",
                "default": "Every mood brings unique perspectives to AI-Logic!"
            }
        }
    
    def generate_greeting(self, name: str = "World") -> str:
        """Generate an AI-powered greeting using templates."""
        template = random.choice(self.greeting_templates)
        return template.format(name=name)
    
    def apply_logic(self, context: Dict[str, Any]) -> str:
        """Apply logical rules based on context."""
        if "time" in context:
            time_period = context["time"].lower()
            return self.logic_rules["time_based"].get(time_period, 
                                                     "Hello at any time of day!")
        
        if "mood" in context:
            mood = context["mood"].lower()
            return self.logic_rules["mood_based"].get(mood, 
                                                     self.logic_rules["mood_based"]["default"])
        
        return "Logic processing complete - ready for action!"
    
    def hello_world(self, name: str = "World", context: Dict[str, Any] = None) -> Dict[str, str]:
        """Main Hello World function combining GenAI and Logic."""
        if context is None:
            context = {}
        
        # GenAI component: Generate personalized greeting
        ai_greeting = self.generate_greeting(name)
        
        # Logic component: Apply contextual rules
        logical_response = self.apply_logic(context)
        
        # Combine both for complete response
        return {
            "ai_greeting": ai_greeting,
            "logical_response": logical_response,
            "combined_message": f"{ai_greeting} {logical_response}"
        }
    
    def demonstrate_capabilities(self) -> None:
        """Demonstrate various GenAI-Logic capabilities."""
        print("=== GenAI-Logic Hello World Demonstration ===\n")
        
        # Basic Hello World
        print("1. Basic Hello World:")
        result = self.hello_world()
        print(f"   {result['combined_message']}\n")
        
        # Personalized greeting
        print("2. Personalized Greeting:")
        result = self.hello_world("Alice")
        print(f"   {result['combined_message']}\n")
        
        # Time-based logic
        print("3. Time-based Logic:")
        result = self.hello_world("Bob", {"time": "morning"})
        print(f"   AI: {result['ai_greeting']}")
        print(f"   Logic: {result['logical_response']}\n")
        
        # Mood-based logic
        print("4. Mood-based Logic:")
        result = self.hello_world("Charlie", {"mood": "excited"})
        print(f"   AI: {result['ai_greeting']}")
        print(f"   Logic: {result['logical_response']}\n")
        
        # Multiple contexts
        print("5. Complex Context:")
        result = self.hello_world("Diana", {"time": "evening", "mood": "curious"})
        print(f"   Combined: {result['combined_message']}")


def main():
    """Main function to run the Hello World demonstration."""
    genai_logic = GenAILogicHello()
    genai_logic.demonstrate_capabilities()


if __name__ == "__main__":
    main()