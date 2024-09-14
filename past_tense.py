from verbs import * 
from helper_functions import * 

################ IMPERFECTO ##############################

# yo, el, ella, usted in imperfect  
# PARAMETER : STRING infinitive form 
# RETURN TYPE: STRING conjugated form   
def yo_el_imperfecto(infinitive):
    verb_ending = get_infinitive_ending(infinitive) 
    second_person_present = verbs[infinitive][1] 
    if verb_ending == 'ar': 
        conjugated_form = second_person_present[:-2] + 'aba' 
    elif verb_ending == 'er' or 'ir': 
        conjugated_form = second_person_present[:-2] + 'ía' 
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
    second_person_present = verbs[infinitive][1] 
    if verb_ending == 'ar': 
        conjugated_form = second_person_present[:-2] + 'ábamos' 
    elif verb_ending == 'er' or 'ir': 
        conjugated_form = second_person_present[:-2] + 'íamos' 
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