"""
Translation Module for EMR Chatbot
===================================
This module provides language translation functionality for the chatbot.
It demonstrates:
- Data types: dict (for translation dictionaries), str (for text), list (for languages)
- Variables: Module-level dictionaries and function-level variables
- Functions: Translation functions with parameters and return values
- Scope: Module-level data accessible by all functions
- Modularization: Reusable translation functions

Author: EMR Chatbot Team
Date: 2026-01-31
"""

# ============================================================================
# MODULE-LEVEL VARIABLES (Global Scope)
# ============================================================================
# These dictionaries store translation data accessible by all functions
# Data Type: dict (dictionary) - key-value pairs for translations

# English to Spanish translation dictionary
ENGLISH_TO_SPANISH = {
    # Common greetings
    "hello": "hola",
    "goodbye": "adiós",
    "good morning": "buenos días",
    "good afternoon": "buenas tardes",
    "good evening": "buenas noches",
    "thank you": "gracias",
    "please": "por favor",
    "yes": "sí",
    "no": "no",
    
    # Medical/EMR terms
    "patient": "paciente",
    "doctor": "doctor",
    "nurse": "enfermera",
    "hospital": "hospital",
    "diagnosis": "diagnóstico",
    "treatment": "tratamiento",
    "medication": "medicamento",
    "prescription": "receta",
    "appointment": "cita",
    "emergency": "emergencia",
    "pain": "dolor",
    "fever": "fiebre",
    "headache": "dolor de cabeza",
    "blood pressure": "presión arterial",
    "heart rate": "frecuencia cardíaca",
    "test results": "resultados de pruebas",
    "admission": "admisión",
    "discharge": "alta",
    "surgery": "cirugía",
    "laboratory": "laboratorio",
}

# English to French translation dictionary
ENGLISH_TO_FRENCH = {
    # Common greetings
    "hello": "bonjour",
    "goodbye": "au revoir",
    "good morning": "bonjour",
    "good afternoon": "bon après-midi",
    "good evening": "bonsoir",
    "thank you": "merci",
    "please": "s'il vous plaît",
    "yes": "oui",
    "no": "non",
    
    # Medical/EMR terms
    "patient": "patient",
    "doctor": "médecin",
    "nurse": "infirmière",
    "hospital": "hôpital",
    "diagnosis": "diagnostic",
    "treatment": "traitement",
    "medication": "médicament",
    "prescription": "ordonnance",
    "appointment": "rendez-vous",
    "emergency": "urgence",
    "pain": "douleur",
    "fever": "fièvre",
    "headache": "mal de tête",
    "blood pressure": "tension artérielle",
    "heart rate": "fréquence cardiaque",
    "test results": "résultats de tests",
    "admission": "admission",
    "discharge": "sortie",
    "surgery": "chirurgie",
    "laboratory": "laboratoire",
}

# Data Type: list - stores supported language names
SUPPORTED_LANGUAGES = ["english", "spanish", "french"]


# ============================================================================
# TRANSLATION FUNCTIONS
# ============================================================================

def translate_to_spanish(text):
    """
    Translates English text to Spanish.
    
    This function demonstrates:
    - Function parameters: text (str) - the English text to translate
    - Return values: str - the Spanish translation or original text
    - Variable scope: Uses module-level ENGLISH_TO_SPANISH dictionary
    - Local variables: normalized_text has function scope
    
    Parameters:
        text (str): The English text to translate
    
    Returns:
        str: The Spanish translation if found, otherwise the original text
        
    Example:
        >>> translate_to_spanish("hello")
        'hola'
        >>> translate_to_spanish("patient")
        'paciente'
    """
    # Local variable - exists only within this function (function scope)
    # Data Type: str (string)
    normalized_text = text.lower().strip()
    
    # Check if translation exists in dictionary
    # The .get() method returns the value if key exists, otherwise returns the default
    if normalized_text in ENGLISH_TO_SPANISH:
        return ENGLISH_TO_SPANISH[normalized_text]
    else:
        # Return original text if no translation found
        return f"{text} (translation not available)"


def translate_to_french(text):
    """
    Translates English text to French.
    
    This function demonstrates:
    - Function parameters: text (str) - the English text to translate
    - Return values: str - the French translation or original text
    - Variable scope: Uses module-level ENGLISH_TO_FRENCH dictionary
    - Code reusability: Similar structure to translate_to_spanish
    
    Parameters:
        text (str): The English text to translate
    
    Returns:
        str: The French translation if found, otherwise the original text
        
    Example:
        >>> translate_to_french("hello")
        'bonjour'
        >>> translate_to_french("doctor")
        'médecin'
    """
    # Local variable with function scope
    normalized_text = text.lower().strip()
    
    # Dictionary lookup with error handling
    if normalized_text in ENGLISH_TO_FRENCH:
        return ENGLISH_TO_FRENCH[normalized_text]
    else:
        return f"{text} (translation not available)"


def translate_from_spanish(text):
    """
    Translates Spanish text to English (reverse translation).
    
    This function demonstrates:
    - Reverse dictionary lookup
    - Iteration through dictionary items
    - Multiple return points based on conditions
    
    Parameters:
        text (str): The Spanish text to translate
    
    Returns:
        str: The English translation if found, otherwise the original text
        
    Example:
        >>> translate_from_spanish("hola")
        'hello'
        >>> translate_from_spanish("paciente")
        'patient'
    """
    # Local variable with function scope
    normalized_text = text.lower().strip()
    
    # Iterate through dictionary to find matching Spanish value
    # This demonstrates reverse lookup: finding key by value
    for english, spanish in ENGLISH_TO_SPANISH.items():
        if spanish == normalized_text:
            return english
    
    # If no match found, return original text
    return f"{text} (translation not available)"


def translate_from_french(text):
    """
    Translates French text to English (reverse translation).
    
    This function demonstrates:
    - Reverse dictionary lookup (similar to translate_from_spanish)
    - Code modularity and reusability
    
    Parameters:
        text (str): The French text to translate
    
    Returns:
        str: The English translation if found, otherwise the original text
        
    Example:
        >>> translate_from_french("bonjour")
        'hello'
        >>> translate_from_french("médecin")
        'doctor'
    """
    normalized_text = text.lower().strip()
    
    # Reverse lookup in French dictionary
    for english, french in ENGLISH_TO_FRENCH.items():
        if french == normalized_text:
            return english
    
    return f"{text} (translation not available)"


def get_supported_languages():
    """
    Returns a list of supported languages.
    
    This function demonstrates:
    - No parameters (empty parameter list)
    - Return value: list data type
    - Encapsulation: Hides internal data structure
    
    Returns:
        list: List of supported language names
        
    Example:
        >>> get_supported_languages()
        ['english', 'spanish', 'french']
    """
    # Return a copy of the list to prevent external modification
    # Data Type: list
    return SUPPORTED_LANGUAGES.copy()


def add_custom_translation(english, spanish, french):
    """
    Adds a new translation to all language dictionaries.
    
    This function demonstrates:
    - Multiple parameters (3 parameters)
    - Return value: bool (boolean) data type for success/failure
    - Modifying module-level variables
    - Error handling with try-except
    - Input validation
    
    Parameters:
        english (str): The English phrase
        spanish (str): The Spanish translation
        french (str): The French translation
    
    Returns:
        bool: True if translation added successfully, False otherwise
        
    Example:
        >>> add_custom_translation("headache", "dolor de cabeza", "mal de tête")
        True
    """
    try:
        # Input validation - check that all parameters are non-empty strings
        # Data Type: bool (boolean) - result of validation check
        if not english or not spanish or not french:
            return False
        
        # Normalize all inputs (local variables with function scope)
        english_normalized = english.lower().strip()
        spanish_normalized = spanish.lower().strip()
        french_normalized = french.lower().strip()
        
        # Add to both dictionaries (modifying module-level variables)
        ENGLISH_TO_SPANISH[english_normalized] = spanish_normalized
        ENGLISH_TO_FRENCH[english_normalized] = french_normalized
        
        # Return success
        # Data Type: bool
        return True
        
    except Exception as e:
        # Error handling - return False if any error occurs
        print(f"Error adding translation: {e}")
        return False


def get_translation_count():
    """
    Returns the number of available translations.
    
    This function demonstrates:
    - No parameters
    - Return value: int (integer) data type
    - Using built-in len() function
    
    Returns:
        int: Number of translations in the Spanish dictionary
        
    Example:
        >>> get_translation_count()
        20
    """
    # Data Type: int (integer) - result of len() function
    return len(ENGLISH_TO_SPANISH)


def list_all_translations():
    """
    Returns all available English phrases that can be translated.
    
    This function demonstrates:
    - No parameters
    - Return value: list of strings
    - Converting dictionary keys to list
    
    Returns:
        list: All English phrases available for translation
        
    Example:
        >>> list_all_translations()
        ['hello', 'goodbye', 'patient', 'doctor', ...]
    """
    # Data Type: list - sorted list of dictionary keys
    return sorted(ENGLISH_TO_SPANISH.keys())


# ============================================================================
# MODULE TEST (runs only when module is executed directly)
# ============================================================================
if __name__ == "__main__":
    print("=== Translation Module Test ===\n")
    
    # Test translate_to_spanish
    print("Testing translate_to_spanish:")
    print(f"  'hello' -> {translate_to_spanish('hello')}")
    print(f"  'patient' -> {translate_to_spanish('patient')}")
    print()
    
    # Test translate_to_french
    print("Testing translate_to_french:")
    print(f"  'hello' -> {translate_to_french('hello')}")
    print(f"  'doctor' -> {translate_to_french('doctor')}")
    print()
    
    # Test reverse translations
    print("Testing translate_from_spanish:")
    print(f"  'hola' -> {translate_from_spanish('hola')}")
    print()
    
    print("Testing translate_from_french:")
    print(f"  'bonjour' -> {translate_from_french('bonjour')}")
    print()
    
    # Test utility functions
    print(f"Supported languages: {get_supported_languages()}")
    print(f"Total translations: {get_translation_count()}")
    print()
    
    # Test adding custom translation
    print("Testing add_custom_translation:")
    success = add_custom_translation("cough", "tos", "toux")
    print(f"  Added 'cough' translation: {success}")
    print(f"  'cough' -> Spanish: {translate_to_spanish('cough')}")
    print(f"  'cough' -> French: {translate_to_french('cough')}")
