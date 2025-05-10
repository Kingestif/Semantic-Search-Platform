import re

def highlight_keywords(text, query):
    # Create a pattern for finding the keywords in the text
    # We use re.IGNORECASE to ignore case sensitivity
    pattern = re.compile(r'(\b' + re.escape(query) + r'\b)', re.IGNORECASE)

    highlighted_text = pattern.sub(r'<span style="background-color: #FFFF99; padding: 0 2px; color: black; border-radius: 3px;">\1</span>', text)

    return highlighted_text
