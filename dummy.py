import classification as classify
import comparison as compare

# my_dict = {1: [0.5, 0.6, 0.7]}
# threshold = 0.5

# classify.thresholdClassify(my_dict, threshold)

# attr_val = 'christen'

val1 = '2107'
val2 = '2106'

print(compare.edit_dist_sim_comp(val1, val2))


def phonetic_encode(attr_val):
    # Keep first letter
    first_letter = attr_val[0]

    # Remove a,e,i,o,u,y,h,w
    attr_val_exc_first_letter = attr_val[1:]
    char_to_remove = ['a', 'e', 'i', 'o', 'u', 'y', 'h', 'w']
    for char in char_to_remove:
        attr_val_exc_first_letter = attr_val_exc_first_letter.replace(char, '')

    # Replace all consonants from position 2 onwards with digits
    char_to_1 = ['b', 'f', 'p', 'v']
    char_to_2 = ['c', 'g', 'j', 'k', 'q', 's', 'x', 'z']
    char_to_3 = ['d', 't']
    char_to_4 = ['l']
    char_to_5 = ['m', 'n']
    char_to_6 = ['r']

    for char in char_to_1:
        attr_val_exc_first_letter = attr_val_exc_first_letter.replace(
            char, '1')
    for char in char_to_2:
        attr_val_exc_first_letter = attr_val_exc_first_letter.replace(
            char, '2')
    for char in char_to_3:
        attr_val_exc_first_letter = attr_val_exc_first_letter.replace(
            char, '3')
    for char in char_to_4:
        attr_val_exc_first_letter = attr_val_exc_first_letter.replace(
            char, '4')
    for char in char_to_5:
        attr_val_exc_first_letter = attr_val_exc_first_letter.replace(
            char, '5')
    for char in char_to_6:
        attr_val_exc_first_letter = attr_val_exc_first_letter.replace(
            char, '6')

    # Only keep unique adjacent digits
    for i in range(len(attr_val_exc_first_letter) - 1):
        if (attr_val_exc_first_letter[i] == attr_val_exc_first_letter[i+1]):
            attr_val_exc_first_letter = attr_val_exc_first_letter[:i] + \
                attr_val_exc_first_letter[i+1:]

    # If length of a code is less than 4 then add zeros, if longer truncate at length 4
    result = first_letter + attr_val_exc_first_letter
    if len(result) > 4:
        result = result[:4]
    elif len(result) < 4:
        no_missing_chars = 4 - len(result)
        for x in range(no_missing_chars):
            result = result + '0'

    print(result)
