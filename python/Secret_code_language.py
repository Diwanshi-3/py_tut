import random
import string
def random_chars(n=3):
    return ''.join(random.choices(string.ascii_lowercase,k=n))
def encode(word):
    if len(word)>=3:
        first=word[0]
        rest=word[1:]
        new_word=rest+first
        return random_chars() + new_word + random_chars()
    else:
        return word[::-1]
def decode(word):
    if len(word)<3:
        return word[::-1]
    if len(word)<=6:
        return word
    core=word[3:-3]
    last=core[-1]
    rest=core[:-1]
    return last+rest
while True:
    msg=input("Enter Message: ")
    mode=input("Encode or Decode (e/d): ").lower()
    words=msg.split()
    result=[]

    for w in words:
        if mode=='e':
            result.append(encode(w))
        else:
            result.append(decode(w))
    print("Result:"," ".join(result))
    choice=input("Do you want to continue (y/n):").lower()
    if choice=='y':
        continue
    else:
        break



    

