# our_stopwords/_main__.py

import os
import json


DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
MAIN_REF_URL = "https://raw.githubusercontent.com/ndamulelonemakh/our-stopwords/feature/pip-package/za_stopwords.main.jsonl"


def list_available_languages():
    """
    List all available language codes.

    Returns:
    - list: List of available language codes.
    """
    files = os.listdir(DATA_DIR)
    language_codes = [os.path.splitext(file)[0] for file in files if file.endswith('.jsonl')]
    return language_codes


def get_stopwords(language_code: str):
    """
    Retrieve stop words for a specific language.

    Parameters:
    - language_code (str): Language code (e.g., 'ven' for Venda).

    Returns:
    - list: List of stop words for the specified language.
    """
    # Ensure language code is lowercase
    language_code = language_code.lower()

    # Check if the language code is valid
    valid_codes = list_available_languages()
    if language_code not in valid_codes:
        raise ValueError(f"Unsupported language code '{language_code}'. Please use one of {valid_codes}.")

    # Load stop words from the JSON lines file
    file_path = os.path.join(DATA_DIR, f'{language_code}.jsonl')
    with open(file_path, 'r', encoding='utf-8') as file:
        stop_words = []
        for line in file:
            stop_words.append(json.loads(line.strip()))

    return stop_words
