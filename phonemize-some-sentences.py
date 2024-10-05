import json
from piper_phonemize import phonemize_espeak, phoneme_ids_espeak, get_espeak_map

def phonemize_sentence(text, language="en-us"):
    # Phonemize the input sentence
    phonemes = phonemize_espeak(text, language)
    
    # Flatten the phoneme list (espeak might return a list of lists for sentences)
    phonemes_flat = [phon for sublist in phonemes for phon in sublist]
    
    # Map phonemes to phoneme IDs
    phoneme_ids = phoneme_ids_espeak(phonemes_flat)
    
    # Create the output dictionary
    output = {
        "text": text,
        "phonemes": phonemes_flat,
        "phoneme_ids": phoneme_ids
    }
    
    # Return as a one-line JSON string for jsonl files
    return json.dumps(output, ensure_ascii=False, separators=(',', ':'))

# Example usage
sentence = "cowboy one, this is kenway. bandit bearing one two three, five miles, ten thousand feet. scramble to intercept."
phonemized_output = phonemize_sentence(sentence)
print(phonemized_output)
