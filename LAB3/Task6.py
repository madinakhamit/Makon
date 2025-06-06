def reverse_words(sentence):
    words = sentence.split()  
    reversed_sentence = " ".join(reversed(words)) 
    return reversed_sentence  

sentence = input("Enter sentence: ")  
print(reverse_words(sentence))  
