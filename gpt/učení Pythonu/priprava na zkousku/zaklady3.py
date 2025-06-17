



import string

def check_palindrome(text):
    # Odstranění mezer, interpunkce a převod na malá písmena
    text = text.lower()
    allowed_chars = set(string.ascii_lowercase + "áčďéěíňóřšťúůýž")  # české znaky + anglická abeceda
    filtered = ''.join(c for c in text if c in allowed_chars)

    return filtered == filtered[::-1]


print(check_palindrome("závodní auto"))                   # True
print(check_palindrome("úroveň"))                         # True
print(check_palindrome("Bylo to auto nebo kočka, kterou jsem viděl?"))  # True
print(check_palindrome("ahoj"))                           # False

print(check_palindrome("racecar"))
print(check_palindrome("level" ))
print(check_palindrome("Was it a car or a cat I saw?"))
