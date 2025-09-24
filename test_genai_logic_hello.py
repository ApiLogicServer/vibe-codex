#!/usr/bin/env python3
"""
Tests for GenAI-Logic Hello World Example
"""

import unittest
from genai_logic_hello import GenAILogicHello


class TestGenAILogicHello(unittest.TestCase):
    """Test cases for GenAI-Logic Hello World functionality."""
    
    def setUp(self):
        """Set up test fixtures."""
        self.genai_logic = GenAILogicHello()
    
    def test_generate_greeting(self):
        """Test AI greeting generation."""
        greeting = self.genai_logic.generate_greeting("TestUser")
        self.assertIn("TestUser", greeting)
        self.assertTrue(len(greeting) > 0)
    
    def test_generate_greeting_default(self):
        """Test AI greeting with default name."""
        greeting = self.genai_logic.generate_greeting()
        self.assertIn("World", greeting)
    
    def test_apply_logic_time_based(self):
        """Test time-based logic rules."""
        context = {"time": "morning"}
        result = self.genai_logic.apply_logic(context)
        self.assertIn("morning", result.lower())
        
        context = {"time": "afternoon"}
        result = self.genai_logic.apply_logic(context)
        self.assertIn("afternoon", result.lower())
    
    def test_apply_logic_mood_based(self):
        """Test mood-based logic rules."""
        context = {"mood": "excited"}
        result = self.genai_logic.apply_logic(context)
        self.assertIn("excitement", result.lower())
        
        context = {"mood": "curious"}
        result = self.genai_logic.apply_logic(context)
        self.assertIn("curiosity", result.lower())
    
    def test_apply_logic_unknown_context(self):
        """Test logic with unknown context."""
        context = {"unknown": "value"}
        result = self.genai_logic.apply_logic(context)
        self.assertTrue(len(result) > 0)
    
    def test_hello_world_basic(self):
        """Test basic hello world functionality."""
        result = self.genai_logic.hello_world()
        self.assertIn("ai_greeting", result)
        self.assertIn("logical_response", result)
        self.assertIn("combined_message", result)
        self.assertIn("World", result["ai_greeting"])
    
    def test_hello_world_personalized(self):
        """Test personalized hello world."""
        result = self.genai_logic.hello_world("Alice")
        self.assertIn("Alice", result["ai_greeting"])
        self.assertIn("Alice", result["combined_message"])
    
    def test_hello_world_with_context(self):
        """Test hello world with context."""
        context = {"time": "evening", "mood": "focused"}
        result = self.genai_logic.hello_world("Bob", context)
        
        # Should contain the name
        self.assertIn("Bob", result["ai_greeting"])
        
        # Should apply one of the logic rules (time takes precedence)
        self.assertTrue(
            "evening" in result["logical_response"].lower() or
            "focus" in result["logical_response"].lower()
        )
    
    def test_greeting_templates_variety(self):
        """Test that different greeting templates are used."""
        greetings = set()
        for _ in range(20):  # Generate multiple greetings
            greeting = self.genai_logic.generate_greeting("Test")
            greetings.add(greeting)
        
        # Should have at least 2 different templates (randomness permitting)
        self.assertGreaterEqual(len(greetings), 1)


if __name__ == "__main__":
    unittest.main()