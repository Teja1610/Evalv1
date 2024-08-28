def common_un_characters(s1, s2):
    
    common_chars = []
    un_chars_s1 = []
    un_chars_s2 = []
    
    
    iter_s2 = iter(s2)
    common_chars = [char for char in s1 if char in iter_s2]

    
    set_s1 = set(s1)
    set_s2 = set(s2)

    
    un_chars_s1 = ''.join([char for char in s1 if char not in set_s2])
    un_chars_s2 = ''.join([char for char in s2 if char not in set_s1])
    
    return ''.join(common_chars), un_chars_s1 + un_chars_s2


s1 = input("Enter String1:")
s2 = input("Enter String2:")
common, uncommon = common_un_characters(s1, s2)

print("Common Characters:", common)
print("Uncommon Characters:", uncommon)
