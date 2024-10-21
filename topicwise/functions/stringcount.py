

def strcount(char):
    vowel_count=0
    for c in char:
        if c in "aeiou":
            vowel_count=vowel_count+1
        else:
            vowel_count=vowel_count

    print(vowel_count)

def char_count(char):
    char=char.strip()
    space_count=0
    letter_count=0
    for c in char:
        if " " in c:
            space_count+=1
        else:
            letter_count+=1
    print("The total letter in a sentence is",space_count + letter_count)

strcount("abhishek kumar")
char_count("abhishek kumar")