def translate(text):
    def translate_word(word):
        vocales = "aeiou"
        
        if text[0] in vocales or text[0:2] == "xr" or text[0:2] == "yt":
            return text + "ay"
    
        else:
            i = 0
            while i < len(word) and word[i] not in vocales and not (word[i] == 'y' and i > 0):
                i += 1
            if i < len(word) and word[i] == 'u' and i > 0 and word[i-1] == 'q':
                i += 1
            return word[i:] + word[:i] + "ay"

    palabras = text.split()

    palabras_traducidas = [translate_word(w) for w in palabras]

    return " ".join(palabras_traducidas)

    
       

    

    
        

    

    
    
    
        
    
