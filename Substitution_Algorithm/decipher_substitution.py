def decipher_substitution(key: str, text: str, lan="en"):
    """

    Function that decrypts and returns encrypted text according to Substitution Algorithm with entered key

    :param key: (str) Key used to decrypt text encrypted with the Substitution Algorithm
    :param text: (str) Text encrypted with a key using the Substitution Algorithm
    :param lan: ( Default Option = "en" ) Language used to decrypt text encrypted with the Substitution Algorithm
    :return: (str) Output text encrypted with Substitution Algorithm

    Example: decipher_substitution("HELLO", "taxttneaamlryptao")
    return value: "texttobeencrypted"

    """

    for char in text:
        if not char.isalpha():
            text = text.replace(char, "")

    key = "".join(list(dict.fromkeys(key.lower())))
    text = text.lower()

    language_options = {
        "de": ["a", "ä", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "q", "r", "s",
               "t", "u", "ü", "v", "w", "x", "y", "z", "ß"],
        "en": ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
               "v", "w", "x", "y", "z"],
        "fr": ["a", "à", "â", "b", "c", "ç", "d", "e", "é", "è", "ê", "ë", "f", "g", "h", "i", "î", "ï", "j", "k", "l",
               "m", "n", "o", "ô", "p", "q", "r", "s", "t", "u", "ù", "û", "ü", "v", "w", "x", "y", "ÿ", "z", "æ", "œ"],
        "tr": ["a", "b", "c", "ç", "d", "e", "f", "g", "ğ", "h", "ı", "i", "j", "k", "l", "m", "n", "o", "ö", "p", "r",
               "s", "ş", "t", "u", "ü", "v", "y", "z"]
    }

    if len(key) > len(text):
        key = key[:len(text)]
    if len(key) > len(language_options[lan]):
        key = key[:len(language_options)[lan]]

    print(key)

    cipher_alphabet = list(zip(language_options[lan], [i for i in key] + [j for j in language_options[lan] if j not in [i for i in key]]))

    print(cipher_alphabet)
    decrypted_text = ""

    for i in text:
        for j in cipher_alphabet:
            if i == j[1]:
                decrypted_text += j[0]
                break

    return decrypted_text