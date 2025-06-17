



def shorten(text):
    words = text.split()                 # rozdělíme větu na slova
    first_letters = [word[0] for word in words]  # vezmeme první písmena
    return ''.join(first_letters).upper()        # spojíme a převedeme na velká



print(shorten("Don't repeat yourself"))  # DRY
print(shorten("Read the fine manual"))   # RTFM
print(shorten("All terrain armoured transport"))  # ATAT




def shorten(text):
    """Zkrátí text.
 Text :p aram str: nějaký text     :rtype: str
 :return: zkrácený text     """
    return ''.join(word[0] for word in text.split()).upper()


if __name__ == '__main__':
    shortened = shorten("Don't repeat yourself")
    print(shortened)

    shortened = shorten("Rage Against The Machine")
    print(shortened)

