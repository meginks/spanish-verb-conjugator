
# HELPER METHODS 
def get_infinitive_ending(infinitive): 
    last_2_char = infinitive[-2:] 
    if (last_2_char == 'se'): # handle the case of reflexive infinitives (e.g. sentarse)
        return infinitive[-4:-2]; 
    else: 
        return last_2_char  

def get_infinitive_stem(infinitive): 
    if (infinitive[-2:] == 'se'): 
        endless_infinitive = infinitive[:-4] 
    else: 
        endless_infinitive = infinitive[:-2] 
    return endless_infinitive 

