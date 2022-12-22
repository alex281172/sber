russian = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'
alphabet = {}
for i in range(len(russian)):
    alphabet.update({russian[i]:(i+1)})


