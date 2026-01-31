"""
Medical Terminology Module for EMR Chatbot
===========================================
This module provides specialized medical terminology translations.
It demonstrates:
- Specialized dictionaries for medical terms
- Category-based organization
- Integration with main translation module

Author: EMR Chatbot Team
Date: 2026-01-31
"""

# ============================================================================
# MEDICAL TERMINOLOGY DICTIONARIES
# ============================================================================
# Organized by medical category for better organization

# Symptoms and Conditions
SYMPTOMS_SPANISH = {
    "headache": "dolor de cabeza",
    "fever": "fiebre",
    "cough": "tos",
    "nausea": "náusea",
    "dizziness": "mareo",
    "fatigue": "fatiga",
    "chest pain": "dolor de pecho",
    "shortness of breath": "falta de aire",
    "abdominal pain": "dolor abdominal",
    "back pain": "dolor de espalda",
}

SYMPTOMS_FRENCH = {
    "headache": "mal de tête",
    "fever": "fièvre",
    "cough": "toux",
    "nausea": "nausée",
    "dizziness": "vertige",
    "fatigue": "fatigue",
    "chest pain": "douleur thoracique",
    "shortness of breath": "essoufflement",
    "abdominal pain": "douleur abdominale",
    "back pain": "mal de dos",
}

# Medical Procedures
PROCEDURES_SPANISH = {
    "x-ray": "radiografía",
    "blood test": "análisis de sangre",
    "surgery": "cirugía",
    "examination": "examen",
    "vaccination": "vacunación",
    "injection": "inyección",
    "ultrasound": "ecografía",
    "mri scan": "resonancia magnética",
    "ct scan": "tomografía computarizada",
}

PROCEDURES_FRENCH = {
    "x-ray": "radiographie",
    "blood test": "analyse de sang",
    "surgery": "chirurgie",
    "examination": "examen",
    "vaccination": "vaccination",
    "injection": "injection",
    "ultrasound": "échographie",
    "mri scan": "irm",
    "ct scan": "scanner",
}

# Medical Departments
DEPARTMENTS_SPANISH = {
    "emergency": "emergencia",
    "cardiology": "cardiología",
    "neurology": "neurología",
    "pediatrics": "pediatría",
    "radiology": "radiología",
    "laboratory": "laboratorio",
    "pharmacy": "farmacia",
    "intensive care": "cuidados intensivos",
}

DEPARTMENTS_FRENCH = {
    "emergency": "urgence",
    "cardiology": "cardiologie",
    "neurology": "neurologie",
    "pediatrics": "pédiatrie",
    "radiology": "radiologie",
    "laboratory": "laboratoire",
    "pharmacy": "pharmacie",
    "intensive care": "soins intensifs",
}


# ============================================================================
# MEDICAL TRANSLATION FUNCTIONS
# ============================================================================

def get_medical_translation(term, target_language, category="all"):
    """
    Translates medical terms to the specified language.
    
    This function demonstrates:
    - Multiple parameters with default value
    - Searching across multiple dictionaries
    - Category-based filtering
    - Error handling
    
    Parameters:
        term (str): The medical term to translate
        target_language (str): Target language ("spanish" or "french")
        category (str): Medical category ("symptoms", "procedures", "departments", or "all")
                       Default is "all"
    
    Returns:
        str: Translated term or message if not found
        
    Example:
        >>> get_medical_translation("headache", "spanish")
        'dolor de cabeza'
        >>> get_medical_translation("x-ray", "french", "procedures")
        'radiographie'
    """
    # Normalize inputs
    # Data Type: str
    normalized_term = term.lower().strip()
    normalized_language = target_language.lower().strip()
    normalized_category = category.lower().strip()
    
    # Select appropriate dictionaries based on target language
    # Data Type: dict
    if normalized_language == "spanish":
        symptom_dict = SYMPTOMS_SPANISH
        procedure_dict = PROCEDURES_SPANISH
        department_dict = DEPARTMENTS_SPANISH
    elif normalized_language == "french":
        symptom_dict = SYMPTOMS_FRENCH
        procedure_dict = PROCEDURES_FRENCH
        department_dict = DEPARTMENTS_FRENCH
    else:
        return f"Language '{target_language}' not supported"
    
    # Search in appropriate category
    if normalized_category == "symptoms" or normalized_category == "all":
        if normalized_term in symptom_dict:
            return symptom_dict[normalized_term]
    
    if normalized_category == "procedures" or normalized_category == "all":
        if normalized_term in procedure_dict:
            return procedure_dict[normalized_term]
    
    if normalized_category == "departments" or normalized_category == "all":
        if normalized_term in department_dict:
            return department_dict[normalized_term]
    
    # Not found
    return f"Medical term '{term}' not found in category '{category}'"


def list_medical_categories():
    """
    Returns list of available medical term categories.
    
    This function demonstrates:
    - No parameters
    - Return value: list data type
    
    Returns:
        list: Available medical categories
        
    Example:
        >>> list_medical_categories()
        ['symptoms', 'procedures', 'departments']
    """
    # Data Type: list
    return ["symptoms", "procedures", "departments"]


def get_category_terms(category):
    """
    Returns all terms in a specific medical category.
    
    This function demonstrates:
    - Single parameter
    - Conditional logic
    - Return value: list
    
    Parameters:
        category (str): The medical category
    
    Returns:
        list: All terms in that category
        
    Example:
        >>> get_category_terms("symptoms")
        ['headache', 'fever', 'cough', ...]
    """
    # Normalize input
    normalized_category = category.lower().strip()
    
    # Return appropriate list based on category
    if normalized_category == "symptoms":
        return sorted(SYMPTOMS_SPANISH.keys())
    elif normalized_category == "procedures":
        return sorted(PROCEDURES_SPANISH.keys())
    elif normalized_category == "departments":
        return sorted(DEPARTMENTS_SPANISH.keys())
    else:
        return []


def get_medical_term_count():
    """
    Returns total number of medical terms available.
    
    This function demonstrates:
    - No parameters
    - Arithmetic operations
    - Return value: int
    
    Returns:
        int: Total number of medical terms
        
    Example:
        >>> get_medical_term_count()
        27
    """
    # Count terms across all categories
    # Data Type: int
    total = len(SYMPTOMS_SPANISH) + len(PROCEDURES_SPANISH) + len(DEPARTMENTS_SPANISH)
    return total


# ============================================================================
# MODULE TEST
# ============================================================================
if __name__ == "__main__":
    print("=== Medical Terminology Module Test ===\n")
    
    # Test medical translations
    print("Testing get_medical_translation:")
    print(f"  'headache' to Spanish: {get_medical_translation('headache', 'spanish')}")
    print(f"  'x-ray' to French: {get_medical_translation('x-ray', 'french')}")
    print(f"  'emergency' to Spanish: {get_medical_translation('emergency', 'spanish')}")
    print()
    
    # Test category listing
    print(f"Medical categories: {list_medical_categories()}")
    print()
    
    # Test category terms
    print("Symptoms available:")
    print(f"  {get_category_terms('symptoms')}")
    print()
    
    # Test count
    print(f"Total medical terms: {get_medical_term_count()}")
