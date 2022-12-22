menu = ["харчо", "солянка", "плов", "ачик-чучук"]
menu.remove('солянка')
print(menu)

shopstring = "яблоки##бананы##говядина##яйца"
shoplist = list(map(str,shopstring.split("##")))
print(shoplist)