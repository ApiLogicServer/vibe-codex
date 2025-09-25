# GenAI-Logic Hello World

A simple demonstration of combining Generative AI capabilities with logical processing in a Hello World example.

## Overview

This project showcases how to integrate:
- **GenAI**: Template-based text generation that simulates AI-powered personalized greetings
- **Logic**: Rule-based decision making for contextual responses
- **Hello World**: A clear, simple example that demonstrates both capabilities

## Features

- Personalized AI-generated greetings
- Context-aware logical responses (time-based and mood-based)
- Modular design for easy extension
- Comprehensive test coverage

## Usage

### Basic Usage

```bash
python3 genai_logic_hello.py
```

This will run a demonstration showing all capabilities.

### Programmatic Usage

```python
from genai_logic_hello import GenAILogicHello

# Create instance
genai_logic = GenAILogicHello()

# Basic hello world
result = genai_logic.hello_world()
print(result['combined_message'])

# Personalized greeting
result = genai_logic.hello_world("Alice")
print(result['ai_greeting'])

# With context
result = genai_logic.hello_world("Bob", {"time": "morning", "mood": "excited"})
print(result['combined_message'])
```

## Running Tests

```bash
python3 test_genai_logic_hello.py
```

## File Structure

- `genai_logic_hello.py` - Main implementation
- `test_genai_logic_hello.py` - Test suite
- `requirements.txt` - Dependencies (none required for basic functionality)
- `README.md` - This documentation

## Example Output

```
=== GenAI-Logic Hello World Demonstration ===

1. Basic Hello World:
   Greetings, World! Let's explore AI-powered logic together! Logic processing complete - ready for action!

2. Personalized Greeting:
   Welcome, Alice! Time to blend AI creativity with logical thinking! Logic processing complete - ready for action!

3. Time-based Logic:
   AI: Welcome, Bob! Time to blend AI creativity with logical thinking!
   Logic: Good morning! Perfect time for fresh AI insights.
```

## Future Enhancements

- Integration with real AI APIs (OpenAI, etc.)
- More sophisticated logic rules
- Web interface
- Database persistence
- Advanced natural language processing
