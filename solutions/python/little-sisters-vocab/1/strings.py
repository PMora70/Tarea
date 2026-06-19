def add_prefix_un(word):
    word_with_un = "un" + word
    return word_with_un

    


def make_word_groups(vocab_words):
    prefix = vocab_words[0]        
    words = vocab_words[1:]        

    new_words = []
    for w in words:               
        new_words.append(prefix + w)

    full_list = [prefix] + new_words   

    return " :: ".join(full_list)  



def remove_suffix_ness(word):
    root = word[:-4]
    if root.endswith("i"):
        root = root[:-1] + "y"
    return root
    
   


def adjective_to_verb(sentence, index):   
    words = sentence.split()
    verb = words[index]
    verb = verb.rstrip(".")
    return verb + "en"

    
