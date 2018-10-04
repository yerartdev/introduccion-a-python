def split_into_words(lyrics):
    """
    Split a string into lowercase words, removing all punctuation characters,
    returning the result.
    """
    result = []
    for word in lyrics.lower().split():  # lower() convierte las palabras en minusculas
        word = word.strip(',.;()"¡!')  # strip() elimina del incio y del final los caracteres que le pasemos
        result.append(word)
    return result

#def words_to_frequencies(lyrics)
def words_to_frequencies(lyrics):
    """
    Convert words into frequencies. Return a dictionarky whose keys are the
    words with the frequency as the value
    """
    freqs = {}
    for word in lyrics:
        if word in freqs:
            freqs[word] += 1
        else:
            freqs[word] = 1
        # Alternativa al if anterior
        # freqs[word] = freqs.get(word, 0) + 1
        # Otra alternativa
        # freqs.setdefault(word, 0)
        # freqs[word] += 1
    return freqs

#def most_common_words(frequencies)
def most_common_words(frequencies):
    """
    Return a tuple containing:
    * The number of occurences of a word in the first tuple element
    * A list containing the words with that frequency
    """
    values = frequencies.values()
    #max = max(values)
    maxim = max(values)
    
    words = []
    for word, score in frequencies.items():
        #if score == max(value):
        if score == max(values):
            words.append(word)
    #return (max, words)
    return (maxim, words)

#def get_more_often_user_words(threshold=10, frequencies):
def get_more_often_user_words(frequencies, threshold=10):
    """
    Return a list of the words that are used more often, above
    the *optional* threshold. If no threshold is passed, use 10.
    """
    result = list() #::GMG::New
    frequencies = frequencies.copy() #::GMG::New
    
    while True:
        score = most_common_words(frequencies)
        if score[0] < threshold:
            break
        for w in score[1]:
            del frequencies[w]
        result.append(score)
        
    return result