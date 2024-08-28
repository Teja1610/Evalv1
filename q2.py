def reverse_words_string(s):
    
    words = s.split()
    
    
    reversed_words = words[::-1]
    
    
    reversed_string = ' '.join(reversed_words)
    
    return reversed_string

input_string = input("Type the string:")
reversed_string = reverse_words_string(input_string)
print("Original String:", input_string)
print("Reversed Words String:", reversed_string)
