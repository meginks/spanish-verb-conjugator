# This file is to hold lists of exceptions to the rule that aren't covered by the pattern otherwise 

# Exceptions to the rule for creating stems for FUTURE and CONDITIONAL tenses -- there are relatively few of these in Spanish so it is more practical to store these than to derive a pattern that may not be accurate or would only apply to a handful of verbs. I have chosen to include derived forms of the main 12 verbs that also follow this pattern in this map, because there are exceptions to those exceptions (e.g. bendecir follows the regular pattern despite ending in decir) and I don't want to overcomplicate this unnecessarily by attempting to derive patterns that may not actually be there.
future_cond_exceptions = { 
    'abstenerse': 'abstendr',
    'atenerse': 'atendr',
    'caber': 'cabr',
    'componer': 'compondr', 
    'contener': 'contendr', 
    'convenir': 'convendr',
    'decir': 'dir', 
    'deshacer': 'deshar',
    'detener': 'detendr',
    'haber': 'habr', 
    'hacer': 'har', 
    'mantener': 'mantendr',
    'obtener': 'obtendr',
    'oponerse': 'opondr',
    'poder': 'podr',
    'poner': 'pondr', 
    'ponerse': 'pondr',
    'querer': 'querr', 
    'rehacer': 'rehar',
    'saber': 'sabr', 
    'salir': 'saldr',
    'sostener': 'sostendr',
    'suponer': 'supondr',
    'tener': 'tendr', 
    'valer': 'valdr', 
    'venir': 'vendr', 
} 

imperfect_exceptions = {
    'ser': 'era', 
    'ir': 'iba', 
    'ver': 'veía'
}

imperfect_exceptions_nos = {
    'ser': 'éramos', 
    'ir': 'íbamos', 
    'ver': 'veíamos'
}