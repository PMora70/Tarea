def is_paired(input_string):
    stack = []
    pairs = {
        "}" : "{",
        "]" : "[",
        ")" : "("
    }
    
    for character in input_string:
        if character in ("{", "[", "("):
            stack.append(character)
        elif character in pairs:
            if not stack:
                return False

            last_open = stack.pop()
            ideal_pair = pairs[character]

            if last_open != ideal_pair:
                return False

    return len(stack) == 0
         
        
         
            
        
            
        
        
        
    
