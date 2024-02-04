def replaсe_words(text):
    words = text.split()
    reversed_string = ' '.join(reversed(words))
    return reversed_string


text = "Hello, World"
result = replaсe_words(text)
print(result)
