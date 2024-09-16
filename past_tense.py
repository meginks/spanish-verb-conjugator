from verbs import * 
from helper_functions import * 

################ IMPERFECTO ##############################

# yo, el, ella, usted in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def yo_el_imperfecto(infinitive):
    verb_ending = get_infinitive_ending(infinitive) 
    verb_stem = get_infinitive_stem(infinitive) 
    if verb_ending == 'ar': 
        conjugated_form = verb_stem + 'aba' 
    elif verb_ending == 'er' or 'ir': 
        conjugated_form = verb_stem + 'ía' 
    return conjugated_form  


# tú in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def tu_imperfecto(infinitive): 
    return yo_el_imperfecto(infinitive) + 's'  

# nosotros, nosotras in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def nosotros_imperfecto(infinitive): 
    verb_ending = get_infinitive_ending(infinitive) 
    verb_stem = get_infinitive_stem(infinitive)
    if verb_ending == 'ar': 
        conjugated_form = verb_stem + 'ábamos' 
    elif verb_ending == 'er' or 'ir': 
        conjugated_form = verb_stem + 'íamos' 
    return conjugated_form 

# vosotros / vosotras in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def vosotros_imperfecto(infinitive): 
    return yo_el_imperfecto(infinitive) + 'is' 

# ellos / ellas / ustedes in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form  
def ellos_imperfecto(infinitive): 
    return yo_el_imperfecto(infinitive) + 'n'  

################### PRETERITO ######################## 




################# SUBJUNTIVO ########################## 