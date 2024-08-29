def single_root_words(root_word, *other_words):
    same_words = []
    for i in range(len(other_words)):
        if other_words[i].lower() in root_word.lower() or root_word.lower() in other_words[i].lower():
            same_words.append(other_words[i])
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words('riCH', 'Richiest', 'oricHalcum', 'cheers', 'rIchies')
print(result1)
print(result2)
print(result3)
