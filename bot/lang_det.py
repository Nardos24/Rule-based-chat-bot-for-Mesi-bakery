from langdetect import detect, LangDetectException

def detect_language(text: str) -> str:
    """
    detect the language of the given text
    returns:
           'en' for English
            'am' for Amharic
            'unknown' if language cannot be determined"""
    try:
        lang = detect(text)
        if lang == 'en':
            return 'en'
        elif lang == 'am':
            return 'am'
        else:
            return 'unknown'
    except LangDetectException:
        return 'unknown'
    