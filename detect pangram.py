import string

def is_pangram(s):
    return True if len([i for i in set(list(s.lower())) if i in string.ascii_lowercase]) == 26 else False
    

p = "The quick, brown fox jumps over the lazy dog!"
print(is_pangram(p))

 