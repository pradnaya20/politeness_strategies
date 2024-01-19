"""
file: type_token_ratio.py
---
Defines a feature that outputs the word type-token ratio.
"""

from features.word_count import *
  
"""
function: get_word_TTR
@param text: The message for which we are calculating the word type-token ratio.
Recall that the type-token ratio is equal to (# of unique words) / (# of total words).
The output of this function should be a number (specifically, a float).
Example: “Please, oh please can I go to the ball?” → 8 / 9 → 0.889
"""
def get_word_TTR(text):
    words = text.split()
    
    unique_words_count = len(set(words))
    
    total_words_count = count_words(text)
    
    type_token_ratio = unique_words_count / total_words_count if total_words_count > 0 else 0
    
    return type_token_ratio
