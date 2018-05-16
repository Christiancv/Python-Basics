def disemvowel(word):
    letters = list(word)
    bad = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    for letter in bad:
        if letter in letters:
            letters.remove(letter)

    disvowl = "".join(letters)
    return disvowl


word = disemvowel("hIatO")
print(word)