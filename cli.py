#!/usr/bin/env python3
"""
Command Line Interface for GenAI-Logic Hello World
"""

import argparse
import sys
from genai_logic_hello import GenAILogicHello


def main():
    """Main CLI function."""
    parser = argparse.ArgumentParser(
        description="GenAI-Logic Hello World CLI",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python3 cli.py                          # Basic hello world
  python3 cli.py --name Alice             # Personalized greeting
  python3 cli.py --name Bob --time morning  # With time context
  python3 cli.py --name Charlie --mood excited  # With mood context
  python3 cli.py --demo                   # Full demonstration
        """
    )
    
    parser.add_argument(
        "--name", 
        default="World",
        help="Name for personalized greeting (default: World)"
    )
    
    parser.add_argument(
        "--time",
        choices=["morning", "afternoon", "evening"],
        help="Time of day for context-aware logic"
    )
    
    parser.add_argument(
        "--mood",
        choices=["excited", "curious", "focused"],
        help="Mood for context-aware logic"
    )
    
    parser.add_argument(
        "--demo",
        action="store_true",
        help="Run full demonstration"
    )
    
    parser.add_argument(
        "--format",
        choices=["simple", "detailed", "json"],
        default="simple",
        help="Output format (default: simple)"
    )
    
    args = parser.parse_args()
    
    # Create GenAI-Logic instance
    genai_logic = GenAILogicHello()
    
    if args.demo:
        genai_logic.demonstrate_capabilities()
        return
    
    # Build context
    context = {}
    if args.time:
        context["time"] = args.time
    if args.mood:
        context["mood"] = args.mood
    
    # Get result
    result = genai_logic.hello_world(args.name, context)
    
    # Format output
    if args.format == "simple":
        print(result["combined_message"])
    elif args.format == "detailed":
        print(f"AI Greeting: {result['ai_greeting']}")
        print(f"Logic Response: {result['logical_response']}")
        print(f"Combined: {result['combined_message']}")
    elif args.format == "json":
        import json
        print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()