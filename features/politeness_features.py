"""
file: politeness_features.py
---
Defines a feature that calls the PolitenessStrategies from ConvoKit
and returns them as 21 columns (for each message).

Link to Politness Documentation: https://convokit.cornell.edu/documentation/politenessStrategies.html
Link to ConvoKit GitHub examples: https://github.com/CornellNLP/ConvoKit/tree/master/examples/politeness-strategies

You should follow the samples to create the appropriate imports, process the data, and call the function.
"""

from convokit import PolitenessStrategies, Corpus, Utterance, Speaker, TextParser

"""
function: get_politeness_strategies
(Chat-level function)

This gets the politeness annotations of each message, with some fields 
including HASHEDGE, Factuality, Deference, Gratitude, Apologizing, etc.
"""
def get_politeness_strategies(text, speaker_id, utterance_id):
 
    speaker = Speaker(id=speaker_id)
    utterance = Utterance(id=utterance_id, speaker=speaker, text=text)
    corpus = Corpus(utterances=[utterance])

    parser = TextParser(verbosity=1000)
    corpus = parser.transform(corpus)

    ps = PolitenessStrategies()

    transformed_corpus = ps.transform(corpus)

    politeness_features = transformed_corpus.get_utterance(utterance_id).meta['politeness_strategies']

    return politeness_features

