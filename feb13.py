def intersection(lst1, lst2):
    lst3 = [value for value in lst1 if value in lst2]
    return lst3

def shadow_sentences(s1, s2):
    s1 = s1.split(' ')
    s2 = s2.split(' ')
    if len(s1) != len(s2):
        return False
    for i in range(len(s1)):
        if len(s1[i]) != len(s2[i]) or intersection(s1[i], s2[i]) != []:
            return False
    return True

print(shadow_sentences('they are round', 'fold two times'))
print(shadow_sentences('impossible poetry', 'gargantuan cliffs'))
print(shadow_sentences('seemingly unlimited', 'cutthroat crossbows'))
print(shadow_sentences('empty cookie jar', 'adorn fluffy wig'))
print(shadow_sentences('own a boat', 'buy my wine'))
print(shadow_sentences('his friends', 'our company'))
print(shadow_sentences('a normal sentence', 'a normal sentence'))
print(shadow_sentences('salmonella supper', 'birthright'))

# split two sentences respectively
    # two sentences must have the same length
    # loop through each word in the sentences
        # two words with the same index must have the same length
        # two words with the same index must not share any common letter