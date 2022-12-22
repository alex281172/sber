text = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. 
Lorem Ipsum has been the industry's standard dummy text ever since the 1500s,
when an unknown printer took a galley of type and scrambled it to make a 
type specimen book. It has survived not only five centuries, but also the 
leap into electronic typesetting, remaining essentially unchanged. 
It was popularised in the 1960s with the release of Letraset sheets 
containing Lorem Ipsum passages, and more recently with desktop publishing 
software like Aldus PageMaker including versions of Lorem Ipsum.
"""

text = text.lower()
exlude_symbol = (' ', '\n', '.', ',')

text_set = set()
word_temp = ''
for i in range(len(text)-1):
    if text[i] not in exlude_symbol:
        word_temp += text[i]
    else:
        if word_temp != '':
            text_set.add(word_temp)
        word_temp = ''
print(len(text_set))



