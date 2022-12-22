morze = {'a': '•—', 'b': '—•••', 'c': '—•—•', 'd': '—••',
         'e': '•', 'f': '••—•', 'g': '——•', 'h': '••••',
         'i': '••', 'j': '•———', 'k': '—•—', 'l': '•—••',
         'm': '——', 'n': '—•', 'o': '———', 'p': '•——•',
         'q': '——•—', 'r': '•—•', 's': '•••', 't': '—',
         'u': '••—', 'v': '•••—', 'w': '•——', 'x': '—••—',
         'y': '—•——', 'z': '——••'}

my_text = list(map(str, input().split(' ')))
# print(my_text)
count = 0
# my_text = 'Ignition sequence start'
for my_word in my_text:
    count1 = 1
    for my_letters in my_word:
        my_letters = my_letters.lower()
        print(morze.get(my_letters), end=' ') if count1 < len(my_word) else print(morze.get(my_letters), end='')
        count1 +=1
    count +=1
    print('') if count < len(my_text) else None


