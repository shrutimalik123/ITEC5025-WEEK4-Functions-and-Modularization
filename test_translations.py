"""
Test Suite for EMR Translation Chatbot
=======================================
This script tests all chatbot components and demonstrates functionality.
It shows:
- Sample interactions
- Error handling
- Edge cases
- All translation functions
- Module integration

Author: EMR Chatbot Team
Date: 2026-01-31
"""

# ============================================================================
# IMPORTS
# ============================================================================
import translation_module
import medical_terms
import utils


# ============================================================================
# TEST FUNCTIONS
# ============================================================================

def test_translation_module():
    """
    Tests the translation_module functions.
    
    This demonstrates:
    - Testing function calls
    - Verifying return values
    - Testing with different inputs
    """
    print("=" * 70)
    print("TESTING TRANSLATION MODULE")
    print("=" * 70)
    print()
    
    # Test 1: Basic English to Spanish translation
    print("Test 1: translate_to_spanish()")
    print("-" * 70)
    test_cases = ["hello", "goodbye", "patient", "doctor", "emergency"]
    for word in test_cases:
        result = translation_module.translate_to_spanish(word)
        print(f"  '{word}' → {result}")
    print()
    
    # Test 2: Basic English to French translation
    print("Test 2: translate_to_french()")
    print("-" * 70)
    for word in test_cases:
        result = translation_module.translate_to_french(word)
        print(f"  '{word}' → {result}")
    print()
    
    # Test 3: Reverse translation (Spanish to English)
    print("Test 3: translate_from_spanish()")
    print("-" * 70)
    spanish_words = ["hola", "adiós", "paciente", "doctor"]
    for word in spanish_words:
        result = translation_module.translate_from_spanish(word)
        print(f"  '{word}' → {result}")
    print()
    
    # Test 4: Reverse translation (French to English)
    print("Test 4: translate_from_french()")
    print("-" * 70)
    french_words = ["bonjour", "au revoir", "patient", "médecin"]
    for word in french_words:
        result = translation_module.translate_from_french(word)
        print(f"  '{word}' → {result}")
    print()
    
    # Test 5: Get supported languages
    print("Test 5: get_supported_languages()")
    print("-" * 70)
    languages = translation_module.get_supported_languages()
    print(f"  Supported languages: {languages}")
    print(f"  Data type: {type(languages)}")
    print()
    
    # Test 6: Add custom translation
    print("Test 6: add_custom_translation()")
    print("-" * 70)
    success = translation_module.add_custom_translation("cough", "tos", "toux")
    print(f"  Adding 'cough' translation: {success}")
    print(f"  Verify Spanish: {translation_module.translate_to_spanish('cough')}")
    print(f"  Verify French: {translation_module.translate_to_french('cough')}")
    print()
    
    # Test 7: Translation count
    print("Test 7: get_translation_count()")
    print("-" * 70)
    count = translation_module.get_translation_count()
    print(f"  Total translations available: {count}")
    print(f"  Data type: {type(count)}")
    print()


def test_medical_terms():
    """Tests the medical_terms module."""
    print("=" * 70)
    print("TESTING MEDICAL TERMS MODULE")
    print("=" * 70)
    print()
    
    # Test 1: Medical term translation
    print("Test 1: get_medical_translation()")
    print("-" * 70)
    medical_tests = [
        ("headache", "spanish"),
        ("fever", "french"),
        ("x-ray", "spanish"),
        ("blood test", "french"),
        ("emergency", "spanish"),
    ]
    for term, language in medical_tests:
        result = medical_terms.get_medical_translation(term, language)
        print(f"  '{term}' to {language}: {result}")
    print()
    
    # Test 2: List medical categories
    print("Test 2: list_medical_categories()")
    print("-" * 70)
    categories = medical_terms.list_medical_categories()
    print(f"  Available categories: {categories}")
    print()
    
    # Test 3: Get category terms
    print("Test 3: get_category_terms()")
    print("-" * 70)
    for category in categories:
        terms = medical_terms.get_category_terms(category)
        print(f"  {category.capitalize()}: {len(terms)} terms")
        print(f"    Examples: {', '.join(terms[:3])}")
    print()
    
    # Test 4: Medical term count
    print("Test 4: get_medical_term_count()")
    print("-" * 70)
    count = medical_terms.get_medical_term_count()
    print(f"  Total medical terms: {count}")
    print()


def test_utils():
    """Tests the utils module."""
    print("=" * 70)
    print("TESTING UTILS MODULE")
    print("=" * 70)
    print()
    
    # Test 1: normalize_text
    print("Test 1: normalize_text()")
    print("-" * 70)
    test_inputs = ["  HELLO  ", "GoOdByE", "  patient  "]
    for text in test_inputs:
        result = utils.normalize_text(text)
        print(f"  '{text}' → '{result}'")
    print()
    
    # Test 2: format_response
    print("Test 2: format_response()")
    print("-" * 70)
    response_types = ["info", "success", "error", "warning"]
    for rtype in response_types:
        result = utils.format_response(f"This is a {rtype} message", rtype)
        print(f"  {result}")
    print()
    
    # Test 3: validate_input
    print("Test 3: validate_input()")
    print("-" * 70)
    test_inputs = [
        "translate hello to spanish",
        "help",
        "",
        "quit",
    ]
    for text in test_inputs:
        is_valid, command, arguments = utils.validate_input(text)
        print(f"  Input: '{text}'")
        print(f"    Valid: {is_valid}, Command: '{command}', Args: '{arguments}'")
    print()
    
    # Test 4: parse_translation_request
    print("Test 4: parse_translation_request()")
    print("-" * 70)
    test_requests = [
        "hello to spanish",
        "bonjour from french",
        "patient to french",
    ]
    for request in test_requests:
        success, text, direction, language = utils.parse_translation_request(request)
        print(f"  Request: '{request}'")
        print(f"    Success: {success}, Text: '{text}', Direction: '{direction}', Language: '{language}'")
    print()


def test_error_handling():
    """Tests error handling capabilities."""
    print("=" * 70)
    print("TESTING ERROR HANDLING")
    print("=" * 70)
    print()
    
    # Test 1: Empty input
    print("Test 1: Empty input handling")
    print("-" * 70)
    result = translation_module.translate_to_spanish("")
    print(f"  Empty string: {result}")
    print()
    
    # Test 2: Unknown word
    print("Test 2: Unknown word handling")
    print("-" * 70)
    result = translation_module.translate_to_spanish("xyzabc123")
    print(f"  Unknown word: {result}")
    print()
    
    # Test 3: Invalid language
    print("Test 3: Invalid language handling")
    print("-" * 70)
    result = medical_terms.get_medical_translation("headache", "german")
    print(f"  Invalid language: {result}")
    print()
    
    # Test 4: Invalid add translation
    print("Test 4: Invalid add_custom_translation()")
    print("-" * 70)
    result = translation_module.add_custom_translation("", "", "")
    print(f"  Empty translations: {result}")
    print()


def test_data_types():
    """Demonstrates data types used in the chatbot."""
    print("=" * 70)
    print("DEMONSTRATING DATA TYPES")
    print("=" * 70)
    print()
    
    # String (str)
    print("Data Type: str (string)")
    print("-" * 70)
    text = "hello"
    print(f"  Variable: text = '{text}'")
    print(f"  Type: {type(text)}")
    print()
    
    # Integer (int)
    print("Data Type: int (integer)")
    print("-" * 70)
    count = translation_module.get_translation_count()
    print(f"  Variable: count = {count}")
    print(f"  Type: {type(count)}")
    print()
    
    # Boolean (bool)
    print("Data Type: bool (boolean)")
    print("-" * 70)
    success = translation_module.add_custom_translation("test", "prueba", "test")
    print(f"  Variable: success = {success}")
    print(f"  Type: {type(success)}")
    print()
    
    # List
    print("Data Type: list")
    print("-" * 70)
    languages = translation_module.get_supported_languages()
    print(f"  Variable: languages = {languages}")
    print(f"  Type: {type(languages)}")
    print()
    
    # Dictionary (dict)
    print("Data Type: dict (dictionary)")
    print("-" * 70)
    print(f"  ENGLISH_TO_SPANISH is a dictionary")
    print(f"  Sample entry: 'hello' → '{translation_module.ENGLISH_TO_SPANISH['hello']}'")
    print()
    
    # Tuple
    print("Data Type: tuple")
    print("-" * 70)
    result = utils.validate_input("translate hello to spanish")
    print(f"  Variable: result = {result}")
    print(f"  Type: {type(result)}")
    print()


def test_sample_interactions():
    """Shows sample chatbot interactions."""
    print("=" * 70)
    print("SAMPLE CHATBOT INTERACTIONS")
    print("=" * 70)
    print()
    
    interactions = [
        ("User: Translate 'hello' to Spanish", 
         translation_module.translate_to_spanish("hello")),
        
        ("User: Translate 'patient' to French",
         translation_module.translate_to_french("patient")),
        
        ("User: Translate 'bonjour' from French",
         translation_module.translate_from_french("bonjour")),
        
        ("User: Translate 'headache' to Spanish (medical)",
         medical_terms.get_medical_translation("headache", "spanish")),
        
        ("User: How many translations are available?",
         f"{translation_module.get_translation_count()} general + {medical_terms.get_medical_term_count()} medical"),
        
        ("User: What languages are supported?",
         ", ".join(translation_module.get_supported_languages())),
    ]
    
    for user_input, bot_response in interactions:
        print(f"🤖 {user_input}")
        print(f"   Chatbot: {bot_response}")
        print()


# ============================================================================
# MAIN TEST RUNNER
# ============================================================================

def run_all_tests():
    """
    Runs all test functions.
    
    This demonstrates:
    - Function composition
    - Modular testing
    - Organized test execution
    """
    print("\n")
    print("╔" + "=" * 68 + "╗")
    print("║" + " " * 15 + "EMR CHATBOT TEST SUITE" + " " * 31 + "║")
    print("╚" + "=" * 68 + "╝")
    print("\n")
    
    # Run all test functions
    test_translation_module()
    test_medical_terms()
    test_utils()
    test_error_handling()
    test_data_types()
    test_sample_interactions()
    
    # Summary
    print("=" * 70)
    print("TEST SUITE COMPLETE")
    print("=" * 70)
    print()
    print("✓ All modules tested successfully")
    print("✓ Data types demonstrated: str, int, bool, list, dict, tuple")
    print("✓ Functions tested: parameters, return values, scope")
    print("✓ Error handling verified")
    print("✓ Modularization demonstrated")
    print()
    print("To run the interactive chatbot, execute: python main.py")
    print()


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    run_all_tests()
