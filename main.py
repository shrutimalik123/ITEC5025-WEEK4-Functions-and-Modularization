"""
Main Chatbot Application
=========================
This is the main entry point for the EMR Translation Chatbot.
It demonstrates:
- Module integration and imports
- Main program loop
- User interaction
- Command routing
- Error handling

Author: EMR Chatbot Team
Date: 2026-01-31
"""

# ============================================================================
# IMPORTS - Demonstrates modularization and code reuse
# ============================================================================
# Import our custom modules
import translation_module
import medical_terms
import utils

# Import standard library modules
import sys


# ============================================================================
# MAIN CHATBOT FUNCTIONS
# ============================================================================

def process_translation_command(arguments):
    """
    Processes translation commands from user.
    
    This function demonstrates:
    - Integration of multiple modules
    - Function composition (calling functions from other modules)
    - Error handling
    - Conditional logic
    
    Parameters:
        arguments (str): The translation command arguments
    
    Returns:
        str: The translation result or error message
    """
    # Parse the translation request using utils module
    # Data Type: tuple (bool, str, str, str)
    success, text, direction, language = utils.parse_translation_request(arguments)
    
    if not success:
        return utils.format_response(
            "Invalid format. Use: translate 'text' to/from language",
            "error"
        )
    
    # Validate language support
    # Data Type: list
    supported_langs = translation_module.get_supported_languages()
    
    if language not in supported_langs:
        return utils.format_response(
            f"Language '{language}' not supported. Available: {', '.join(supported_langs)}",
            "error"
        )
    
    # Perform translation based on direction
    # Data Type: str
    result = ""
    
    try:
        if direction == "to":
            # Translate TO target language
            if language == "spanish":
                result = translation_module.translate_to_spanish(text)
            elif language == "french":
                result = translation_module.translate_to_french(text)
        
        elif direction == "from":
            # Translate FROM target language
            if language == "spanish":
                result = translation_module.translate_from_spanish(text)
            elif language == "french":
                result = translation_module.translate_from_french(text)
        
        # Format success response
        return utils.format_response(f"'{text}' → {result}", "success")
        
    except Exception as e:
        return utils.format_response(f"Translation error: {str(e)}", "error")


def process_medical_command(arguments):
    """
    Processes medical term translation commands.
    
    This function demonstrates:
    - Integration with medical_terms module
    - String parsing
    - Error handling
    
    Parameters:
        arguments (str): Medical translation arguments
                        Format: "term to language [category]"
    
    Returns:
        str: Medical term translation result
    """
    # Parse arguments
    # Data Type: str
    parts = arguments.lower().split(" to ")
    
    if len(parts) != 2:
        return utils.format_response(
            "Invalid format. Use: medical 'term' to language",
            "error"
        )
    
    term = parts[0].strip()
    language = parts[1].strip()
    
    # Get medical translation
    result = medical_terms.get_medical_translation(term, language)
    
    return utils.format_response(f"Medical: '{term}' → {result}", "success")


def process_add_command(arguments):
    """
    Processes add custom translation command.
    
    This function demonstrates:
    - String parsing with multiple parts
    - Calling module functions with multiple parameters
    - Boolean return value handling
    
    Parameters:
        arguments (str): Translation data
                        Format: "english" "spanish" "french"
    
    Returns:
        str: Success or error message
    """
    # Parse the three translations
    # Split by quotes to extract the three phrases
    parts = arguments.split('"')
    
    # Filter out empty strings
    phrases = [p.strip() for p in parts if p.strip()]
    
    if len(phrases) != 3:
        return utils.format_response(
            'Invalid format. Use: add "english" "spanish" "french"',
            "error"
        )
    
    # Extract the three translations
    english = phrases[0]
    spanish = phrases[1]
    french = phrases[2]
    
    # Add the translation
    # Data Type: bool
    success = translation_module.add_custom_translation(english, spanish, french)
    
    if success:
        return utils.format_response(
            f"Added translation: {english} → ES: {spanish}, FR: {french}",
            "success"
        )
    else:
        return utils.format_response("Failed to add translation", "error")


def run_chatbot():
    """
    Main chatbot loop - handles user interaction.
    
    This function demonstrates:
    - Program control flow (while loop)
    - User input handling
    - Command routing
    - Error handling
    - Integration of all modules
    
    No parameters, no return value (runs until user quits)
    """
    # Display welcome message
    utils.display_welcome()
    
    # Main loop - Data Type: bool
    running = True
    
    while running:
        try:
            # Display separator for readability
            utils.display_separator()
            
            # Get user input
            # Data Type: str
            user_input = input("\n🤖 You: ").strip()
            
            # Validate input
            # Data Type: tuple (bool, str, str)
            is_valid, command, arguments = utils.validate_input(user_input)
            
            if not is_valid:
                print(utils.format_response("Please enter a command", "warning"))
                continue
            
            # Process commands
            # Data Type: str
            response = ""
            
            # Translation command
            if command == "translate":
                response = process_translation_command(arguments)
            
            # Medical translation command
            elif command == "medical":
                response = process_medical_command(arguments)
            
            # Help command
            elif command == "help":
                utils.display_help()
                continue
            
            # List supported languages
            elif command == "languages":
                langs = translation_module.get_supported_languages()
                response = utils.format_response(
                    f"Supported languages: {', '.join(langs)}",
                    "info"
                )
            
            # List all translations
            elif command == "list":
                translations = translation_module.list_all_translations()
                print(utils.format_response(
                    f"Available translations ({len(translations)}):",
                    "info"
                ))
                # Display in columns for readability
                for i, term in enumerate(translations, 1):
                    print(f"  {i}. {term}")
                continue
            
            # Show translation count
            elif command == "count":
                count = translation_module.get_translation_count()
                medical_count = medical_terms.get_medical_term_count()
                response = utils.format_response(
                    f"Total translations: {count} general + {medical_count} medical = {count + medical_count}",
                    "info"
                )
            
            # Add custom translation
            elif command == "add":
                response = process_add_command(arguments)
            
            # Medical categories
            elif command == "categories":
                categories = medical_terms.list_medical_categories()
                response = utils.format_response(
                    f"Medical categories: {', '.join(categories)}",
                    "info"
                )
            
            # Quit/Exit commands
            elif command in ["quit", "exit", "bye"]:
                print(utils.format_response("Goodbye! Thank you for using EMR Chatbot.", "success"))
                running = False
                continue
            
            # Unknown command
            else:
                response = utils.format_response(
                    f"Unknown command: '{command}'. Type 'help' for available commands.",
                    "error"
                )
            
            # Display response
            print(f"\n🤖 Bot: {response}")
            
        except KeyboardInterrupt:
            # Handle Ctrl+C gracefully
            print("\n" + utils.format_response("Interrupted. Goodbye!", "warning"))
            running = False
        
        except Exception as e:
            # Handle any unexpected errors
            print(utils.format_response(f"Unexpected error: {str(e)}", "error"))
            print(utils.format_response("Type 'help' for usage information", "info"))


# ============================================================================
# MAIN ENTRY POINT
# ============================================================================

def main():
    """
    Main entry point for the application.
    
    This function demonstrates:
    - Program entry point
    - Top-level error handling
    - Clean program exit
    """
    try:
        run_chatbot()
    except Exception as e:
        print(f"Fatal error: {e}")
        sys.exit(1)


# Run the chatbot when script is executed directly
if __name__ == "__main__":
    main()
