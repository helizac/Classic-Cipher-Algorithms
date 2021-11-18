def encrypt_improved_caesar(key: str, text: str):
    """

    Function that returns the text encrypted with the Caesar algorithm based on the key and text entered

    :param key: (str) Key to be used in order to decrypt text that is requested to be encrypted w/ Improved Caesar algorithm
    :param text: (str) Text to be encrypted with the Improved Caesar algorithm
    :return: (str) Output text encrypted with Improved Caesar algorithm

    Example: encrypt_improved_caesar("HELLO", "Text to be encrypted")
    return value: "ebrdtocexeyteptnt"

    """

    for char in text:
        if not char.isalpha():
            text = text.replace(char, "")

    text = text.lower()

    key_length = len(key)
    text_length = len(text)
    row_number = int(text_length / key_length) + (text_length / key_length > 0)
    myMatrix = []
    myList = [[] for i in range(key_length)]

    for i in range(row_number):
        if i == row_number - 1:
            myMatrix.append([x for x in text[i * key_length:]])
        elif i != row_number - 1:
            myMatrix.append([x for x in text[i * key_length:(i + 1) * key_length]])

    for j in range(key_length):
        myList[j].append(key[j])
        for k in range(row_number):
            if k == row_number - 1:
                if len(myMatrix[-1]) - 1 >= j:
                    myList[j].append(myMatrix[k][j])
            elif k != row_number - 1:
                myList[j].append(myMatrix[k][j])

    return "".join("".join(x[1:]) for x in sorted(myList, key=lambda x: list(x[0])))