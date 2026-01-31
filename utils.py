"""
Utility Module for EMR Chatbot
================================
This module provides helper functions for the chatbot.
It demonstrates:
- String manipulation functions
- Input validation
- Formatting functions
- Default parameter values
- Multiple return values using tuples

Author: EMR Chatbot Team
Date: 2026-01-31
"""

# ============================================================================
# TEXT PROCESSING FUNCTIONS
# ============================================================================

def normalize_text(text):
    """
    Normalizes text by converting to lowercase and removing extra whitespace.
    
    This function demonstrates:
    - Single parameter: text (str)
    - Return value: str (normalized text)
    - String methods: lower(), strip()
    - Local variable scope
    
    Parameters:
        text (str): The text to normalize
    
    Returns:
        str: Normalized text (lowercase, trimmed)
        
    Example:
        >>> normalize_text("  HELLO  ")
        'hello'
    """
    # Local variable - exists only in this function
    # Data Type: str
    normalized = text.lower().strip()
    return normalized


def format_response(message, response_type="info"):
    """
    Formats chatbot responses with visual indicators.
    
    This function demonstrates:
    - Multiple parameters: message (str), response_type (str)
    - Default parameter value: response_type defaults to "info"
    - Conditional logic based on parameter value
    - String formatting
    
    Parameters:
        message (str): The message to format
        response_type (str): Type of response - "info", "success", "error", or "warning"
                            Default is "info"
    
    Returns:
        str: Formatted message with visual indicators
        
    Example:
        >>> format_response("Translation complete", "success")
        '✓ Translation complete'
        >>> format_response("Invalid input", "error")
        '✗ Invalid input'
    """
    # Local variables with function scope
    # Data Type: str
    prefix = ""
    
    # Determine prefix based on response type
    if response_type == "success":
        prefix = "✓"
    elif response_type == "error":
        prefix = "✗"
    elif response_type == "warning":
        prefix = "⚠"
    else:  # "info" or default
        prefix = "ℹ"
    
    # Format and return the message
    # Data Type: str
    formatted_message = f"{prefix} {message}"
    return formatted_message


# ============================================================================
# INPUT VALIDATION FUNCTIONS
# ============================================================================

def validate_input(user_input):
    """
    Validates and parses user input commands.
    
    This function demonstrates:
    - Single parameter: user_input (str)
    - Multiple return values using tuple
    - Data Types: tuple containing (bool, str, str)
    - String parsing and manipulation
    - Error handling
    
    Parameters:
        user_input (str): Raw user input to validate
    
    Returns:
        tuple: (is_valid, command, arguments)
            - is_valid (bool): True if input is valid
            - command (str): The parsed command
            - arguments (str): The command arguments
            
    Example:
        >>> validate_input("translate hello to spanish")
        (True, 'translate', 'hello to spanish')
        >>> validate_input("")
        (False, '', '')
    """
    # Input validation - check for empty input
    # Data Type: str
    cleaned_input = user_input.strip()
    
    if not cleaned_input:
        # Return tuple with False status
        # Data Type: tuple (bool, str, str)
        return (False, "", "")
    
    # Parse the input - split into command and arguments
    # Data Type: list
    parts = cleaned_input.split(maxsplit=1)
    
    # Extract command (first word)
    # Data Type: str
    command = parts[0].lower()
    
    # Extract arguments (rest of the input)
    # Data Type: str
    arguments = parts[1] if len(parts) > 1 else ""
    
    # Return tuple with parsed data
    # Data Type: tuple (bool, str, str)
    return (True, command, arguments)


def parse_translation_request(arguments):
    """
    Parses translation command arguments.
    
    This function demonstrates:
    - String parsing with multiple delimiters
    - Error handling for malformed input
    - Multiple return values via tuple
    - Local variable scope
    
    Parameters:
        arguments (str): The translation command arguments
                        Expected format: "text to/from language"
    
    Returns:
        tuple: (success, text, direction, language)
            - success (bool): True if parsing succeeded
            - text (str): The text to translate
            - direction (str): "to" or "from"
            - language (str): Target language
            
    Example:
        >>> parse_translation_request("hello to spanish")
        (True, 'hello', 'to', 'spanish')
        >>> parse_translation_request("bonjour from french")
        (True, 'bonjour', 'from', 'french')
    """
    try:
        # Try to parse with "to" direction
        if " to " in arguments.lower():
            # Data Type: list
            parts = arguments.lower().split(" to ", 1)
            # Data Type: str
            text = parts[0].strip()
            language = parts[1].strip()
            direction = "to"
            
            # Validate that we have both text and language
            if text and language:
                return (True, text, direction, language)
        
        # Try to parse with "from" direction
        elif " from " in arguments.lower():
            parts = arguments.lower().split(" from ", 1)
            text = parts[0].strip()
            language = parts[1].strip()
            direction = "from"
            
            if text and language:
                return (True, text, direction, language)
        
        # Invalid format
        return (False, "", "", "")
        
    except Exception as e:
        # Error handling - return failure tuple
        return (False, "", "", "")


# ============================================================================
# DISPLAY FUNCTIONS
# ============================================================================

def display_help():
    """
    Displays help information about available commands.
    
    This function demonstrates:
    - No parameters (void parameter list)
    - No return value (returns None implicitly)
    - Side effects: prints to console
    - Multi-line string formatting
    
    Returns:
        None
        
    Example:
        >>> display_help()
        (prints help text to console)
    """
    # Multi-line string with help information
    # Data Type: str
    help_text = """
╔══════════════════════════════════════════════════════════════╗
║              EMR CHATBOT - AVAILABLE COMMANDS                ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  TRANSLATION COMMANDS:                                       ║
║    translate "text" to <language>                            ║
║    translate "text" from <language>                          ║
║                                                              ║
║    Supported languages: spanish, french                      ║
║                                                              ║
║  UTILITY COMMANDS:                                           ║
║    help              - Show this help message                ║
║    languages         - List supported languages              ║
║    list              - List all available translations       ║
║    count             - Show number of translations           ║
║    add               - Add custom translation                ║
║    quit / exit       - Exit the chatbot                      ║
║                                                              ║
║  EXAMPLES:                                                   ║
║    translate "hello" to spanish                              ║
║    translate "bonjour" from french                           ║
║    translate "patient" to spanish                            ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    
    # Print help text (side effect - no return value)
    print(help_text)


def display_welcome():
    """
    Displays welcome message when chatbot starts.
    
    This function demonstrates:
    - No parameters
    - No return value (void function)
    - Side effects: prints to console
    
    Returns:
        None
    """
    welcome_text = """
╔══════════════════════════════════════════════════════════════╗
║          WELCOME TO EMR TRANSLATION CHATBOT                  ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  This chatbot can translate medical and common phrases       ║
║  between English, Spanish, and French.                       ║
║                                                              ║
║  Type 'help' for available commands.                         ║
║  Type 'quit' to exit.                                        ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
    """
    print(welcome_text)


def display_separator():
    """
    Displays a visual separator line.
    
    This function demonstrates:
    - No parameters
    - No return value
    - Simple utility function for UI formatting
    
    Returns:
        None
    """
    print("─" * 64)


# ============================================================================
# ERROR HANDLING FUNCTIONS
# ============================================================================

def handle_error(error_message):
    """
    Handles and displays error messages in a consistent format.
    
    This function demonstrates:
    - Single parameter: error_message (str)
    - No return value (void function)
    - Using other module functions (format_response)
    - Function composition
    
    Parameters:
        error_message (str): The error message to display
    
    Returns:
        None
        
    Example:
        >>> handle_error("Invalid command")
        (prints formatted error message)
    """
    # Use format_response function to format the error
    # This demonstrates function composition and code reuse
    formatted_error = format_response(error_message, "error")
    print(formatted_error)


# ============================================================================
# MODULE TEST (runs only when module is executed directly)
# ============================================================================
if __name__ == "__main__":
    print("=== Utility Module Test ===\n")
    
    # Test normalize_text
    print("Testing normalize_text:")
    print(f"  '  HELLO  ' -> '{normalize_text('  HELLO  ')}'")
    print()
    
    # Test format_response with different types
    print("Testing format_response:")
    print(f"  Info: {format_response('This is information', 'info')}")
    print(f"  Success: {format_response('Operation successful', 'success')}")
    print(f"  Error: {format_response('Something went wrong', 'error')}")
    print(f"  Warning: {format_response('Be careful', 'warning')}")
    print()
    
    # Test validate_input
    print("Testing validate_input:")
    result = validate_input("translate hello to spanish")
    print(f"  Input: 'translate hello to spanish'")
    print(f"  Result: {result}")
    print()
    
    # Test parse_translation_request
    print("Testing parse_translation_request:")
    result = parse_translation_request("hello to spanish")
    print(f"  Input: 'hello to spanish'")
    print(f"  Result: {result}")
    print()
    
    # Test display functions
    print("Testing display_welcome:")
    display_welcome()
    print()
    
    print("Testing display_help:")
    display_help()
