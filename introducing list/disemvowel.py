def disemvowel(word):
    result = []
    for letter in word:
        result.append(letter.lower())
    try:
        result.remove("a")
        result.remove("e")
        result.remove("i")
        result.remove("o")
        result.remove("u")
    except ValueError:
        pass
    else:




disemvowel("halo")