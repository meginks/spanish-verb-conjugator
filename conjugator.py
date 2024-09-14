from verbs import * 
from helper_functions import *  
from present_tense import * 
from past_tense import * 
### Methods for manipulating verb data to conjugate 


####################### INDICATIVE ################################################################
# INFINITIVE -> PRESENT 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE: TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_present(infinitive):  
    # form tuple: 
    if verbs[infinitive]:    
        conjugated_verb = tuple((verbs[infinitive][0], 
                                 verbs[infinitive][1],
                                el_present(infinitive),
                                nosotros_present(infinitive),
                                vosotros_present(infinitive),
                                ellos_present(infinitive))); 
        return conjugated_verb
    else: 
       print('Lo siento. No tenemos este verbo en el sistema.')
print(make_present('abrir')) 


# INFINITIVE -> IMPERFECT PAST 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def make_imperfect(infinitive): 
    if verbs[infinitive]:    
        conjugated_verb = tuple((verbs[infinitive][0], 
                                 verbs[infinitive][1],
                                yo_el_imperfecto(infinitive),
                                nosotros_imperfecto(infinitive),
                                vosotros_imperfecto(infinitive),
                                ellos_imperfecto(infinitive))); 
        return conjugated_verb
    else: 
        print('Lo siento. No tenemos este verbo en el sistema.')

print(make_imperfect('abrir'))
# INFINITIVE -> PRETERITE PAST 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def makePreterite(infinitive):  ## MIGHT GET TRICKY WITH IRREGULAR...
    if verbs[infinitive]:    
        conjugated_verb = tuple((verbs[infinitive][2], 
                                 verbs[infinitive][1],
                                yo_el_imperfecto(infinitive),
                                nosotros_imperfecto(infinitive),
                                vosotros_imperfecto(infinitive),
                                ellos_imperfecto(infinitive))); 
        return conjugated_verb
    else: 
        print('Lo siento. No tenemos este verbo en el sistema.')

# INFINITIVE -> FUTURE 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def makeFuture(infinitive): 
    if verbs[infinitive]:    
        conjugated_verb = tuple((verbs[infinitive][0], 
                                 verbs[infinitive][1],
                                yo_el_imperfecto(infinitive),
                                nosotros_imperfecto(infinitive),
                                vosotros_imperfecto(infinitive),
                                ellos_imperfecto(infinitive))); 
        return conjugated_verb
    else: 
        print('Lo siento. No tenemos este verbo en el sistema.')

# INFINITIVE -> CONDITIONAL  
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def makeConditional(infinitive): 
    if verbs[infinitive]:    
        conjugated_verb = tuple((verbs[infinitive][0], 
                                 verbs[infinitive][1],
                                yo_el_imperfecto(infinitive),
                                nosotros_imperfecto(infinitive),
                                vosotros_imperfecto(infinitive),
                                ellos_imperfecto(infinitive))); 
        return conjugated_verb
    else: 
        print('Lo siento. No tenemos este verbo en el sistema.')

####################### SUBJUNCTIVE ################################################################
# INFINITIVE -> PRESENT SUBJUNCTIVE 
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def makePresentSubjunctive(infinitive): 
    return 

# INFINITIVE -> IMPERFECT SUBJUNCTIVE  
# PARAMETER : STRING in infinitive form 
#RETURN TYPE : TUPLE in this order (yo, tú, él/ella/usted, nosotro/as, vosotros/as, ellos/ellas/ustedes) 
def makeImperfectSubjunctive(infinitive): 
    return 
## COMPOUND TENSES 




# GET SPECIFIC FORM GENERIC METHOD 
def getSpecificForm(): 
    return 



print(get_infinitive_ending('abrir'))
print(get_infinitive_ending('comprar'))
print(get_infinitive_ending('sentarse'))


print(get_infinitive_stem('abrir'))
print(get_infinitive_stem('comprar'))
print(get_infinitive_stem('sentarse'))
