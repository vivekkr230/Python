def capitalize_or_join_words(sentence):
    # Check if the sentence starts with '*'
    if sentence.startswith('*'):
        # Remove the leading '*'
        sentence = sentence[1:]
        # Split the sentence into words
        words = sentence.split()
        # Capitalize the first and last letters of each word
        capitalized_words = []
        for word in words:
            if len(word) > 1:
                new_word = word[0].upper() + word[1:-1] + word[-1].upper()
            else:
                new_word = word.upper()
            capitalized_words.append(new_word)
        # Join the words back into a sentence and return it
        return ' '.join(capitalized_words)
    else:
        # Split the sentence into words, strip excess whitespace, and join with commas
        words = sentence.split()
        return ','.join(words)

# Examples:
print(capitalize_or_join_words("my name is vivek kumar"))  # Output: "I LovE PythoN"
print(capitalize_or_join_words("i love python"))  # Output: "i,love,python"
print(capitalize_or_join_words("i love    python  "))  # Output: "i,love,python"
