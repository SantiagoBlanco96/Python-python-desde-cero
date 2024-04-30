"""
Se va a resolver el problema del viajero para recorrer 24 ciudades, partiendo de "Rosario" y terminando en "Rosario".
Para resolverlo se seguirán dos caminos el primero se resolverá por el algoritmo búsqueda A* y el segundo por el algoritmo Dijkstra
Se cuenta con la distancia en línea recta entre las ciudades y la distancia por caminos
donde g(n) es la distancia por caminos y h(n) es la distancia en línea recta.
"""

from math import radians, sin, cos, sqrt, atan2

def calcular_distancia(lat1, lon1, lat2, lon2):
    # Radio de la Tierra en kilómetros
    R = 6371.0

    lat1 = radians(lat1)
    lon1 = radians(lon1)
    lat2 = radians(lat2)
    lon2 = radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distancia = R * c
    return round(distancia)

# Diccionario con las coordenadas de las capitales
capitales = {
    "Buenos Aires": (-34.6037, -58.3816),
    "Córdoba": (-31.4201, -64.1888),
    "Resistencia": (-27.4515, -58.9867),
    "Corrientes": (-27.4692, -58.8306),
    "Formosa": (-26.1775, -58.1781),
    "La Plata": (-34.9215, -57.9545),
    "La Rioja": (-29.4135, -66.8565),
    "Mendoza": (-32.8895, -68.8458),
    "Posadas": (-27.3671, -55.8960),
    "Neuquén": (-38.9516, -68.0591),
    "Paraná": (-31.7320, -60.5238),
    "Rawson": (-43.3002, -65.1023),
    "San Fernando del Valle de Catamarca": (-28.4696, -65.7795),
    "San Miguel de Tucumán": (-26.8241, -65.2226),
    "San Salvador de Jujuy": (-24.1858, -65.2995),
    "Salta": (-24.7821, -65.4232),
    "San Juan": (-31.5375, -68.5364),
    "Río Gallegos": (-51.6226, -69.2181),
    "Santa Rosa": (-36.6209, -64.2904),
    "Santiago del Estero": (-27.7951, -64.2615),
    "Ushuaia": (-54.8019, -68.3030),
    "Viedma": (-40.8135, -62.9967),
    "San Luis": (-33.3017, -66.3378),
    "Rosario": (-32.9442, -60.6505)
}

# Diccionario para guardar las distancias
distancias_linea_recta = {}

for ciudad1 in capitales:
    distancias_linea_recta[ciudad1] = {}
    for ciudad2 in capitales:
        if ciudad1 != ciudad2:
            distancias_linea_recta[ciudad1][ciudad2] = calcular_distancia(*capitales[ciudad1], *capitales[ciudad2])

distancias_por_ruta = {
    "Buenos Aires": {"Córdoba": 700, "Resistencia": 1040, "Corrientes": 973, "Formosa": 1163, "La Plata": 62, "La Rioja": 940, "Mendoza": 1052, "Posadas": 1095, "Neuquén": 1069, "Paraná": 691, "Rawson": 1411, "San Fernando del Valle de Catamarca": 995, "San Miguel de Tucumán": 945, "San Salvador de Jujuy": 1085, "Salta": 1125, "San Juan": 1015, "Río Gallegos": 2025, "Santa Rosa": 630, "Santiago del Estero": 910, "Ushuaia": 2388, "Viedma": 791, "San Luis": 814, "Rosario": 309},
    "Córdoba": {"Buenos Aires": 700, "Resistencia": 1040, "Corrientes": 973, "Formosa": 1163, "La Plata": 700, "La Rioja": 611, "Mendoza": 338, "Posadas": 1195, "Neuquén": 860, "Paraná": 560, "Rawson": 1550, "San Fernando del Valle de Catamarca": 634, "San Miguel de Tucumán": 569, "San Salvador de Jujuy": 799, "Salta": 829, "San Juan": 710, "Río Gallegos": 2130, "Santa Rosa": 754, "Santiago del Estero": 670, "Ushuaia": 2350, "Viedma": 921, "San Luis": 390, "Rosario": 405},
    "Resistencia": {"Buenos Aires": 1040, "Córdoba": 1040, "Corrientes": 339, "Formosa": 168, "La Plata": 1030, "La Rioja": 1130, "Mendoza": 1030, "Posadas": 680, "Neuquén": 1180, "Paraná": 660, "Rawson": 1520, "San Fernando del Valle de Catamarca": 970, "San Miguel de Tucumán": 950, "San Salvador de Jujuy": 1180, "Salta": 1210, "San Juan": 990, "Río Gallegos": 2400, "Santa Rosa": 1020, "Santiago del Estero": 800, "Ushuaia": 2760, "Viedma": 870, "San Luis": 1160, "Rosario": 842},
    "Corrientes": {"Buenos Aires": 973, "Córdoba": 973, "Resistencia": 339, "Formosa": 301, "La Plata": 973, "La Rioja": 1073, "Mendoza": 973, "Posadas": 640, "Neuquén": 1210, "Paraná": 590, "Rawson": 1440, "San Fernando del Valle de Catamarca": 970, "San Miguel de Tucumán": 950, "San Salvador de Jujuy": 1180, "Salta": 1210, "San Juan": 980, "Río Gallegos": 2420, "Santa Rosa": 890, "Santiago del Estero": 880, "Ushuaia": 2790, "Viedma": 900, "San Luis": 1097, "Rosario": 675},
    "Formosa": {"Buenos Aires": 1163, "Córdoba": 1163, "Resistencia": 168, "Corrientes": 301, "La Plata": 1163, "La Rioja": 1263, "Mendoza": 1163, "Posadas": 680, "Neuquén": 1300, "Paraná": 820, "Rawson": 1380, "San Fernando del Valle de Catamarca": 1060, "San Miguel de Tucumán": 1040, "San Salvador de Jujuy": 1270, "Salta": 1300, "San Juan": 1070, "Río Gallegos": 2500, "Santa Rosa": 930, "Santiago del Estero": 920, "Ushuaia": 2850, "Viedma": 950, "San Luis": 1241, "Rosario": 843},
    "La Plata": {"Buenos Aires": 62, "Córdoba": 700, "Resistencia": 1030, "Corrientes": 973, "Formosa": 1163, "La Rioja": 1012, "Mendoza": 1052, "Posadas": 1095, "Neuquén": 1069, "Paraná": 691, "Rawson": 1411, "San Fernando del Valle de Catamarca": 995, "San Miguel de Tucumán": 945, "San Salvador de Jujuy": 1085, "Salta": 1125, "San Juan": 1015, "Río Gallegos": 2025, "Santa Rosa": 630, "Santiago del Estero": 910, "Ushuaia": 2388, "Viedma": 791, "San Luis": 794, "Rosario": 304},
    "La Rioja": {"Buenos Aires": 940, "Córdoba": 611, "Resistencia": 1130, "Corrientes": 1073, "Formosa": 1263, "La Plata": 1012, "Mendoza": 550, "Posadas": 1110, "Neuquén": 940, "Paraná": 780, "Rawson": 1290, "San Fernando del Valle de Catamarca": 700, "San Miguel de Tucumán": 640, "San Salvador de Jujuy": 870, "Salta": 900, "San Juan": 980, "Río Gallegos": 2340, "Santa Rosa": 810, "Santiago del Estero": 920, "Ushuaia": 2690, "Viedma": 880, "San Luis": 656, "Rosario": 924},
    "Mendoza": {"Buenos Aires": 1052, "Córdoba": 338, "Resistencia": 1030, "Corrientes": 973, "Formosa": 1163, "La Plata": 1052, "La Rioja": 550, "Posadas": 1300, "Neuquén": 475, "Paraná": 935, "Rawson": 1565, "San Fernando del Valle de Catamarca": 980, "San Miguel de Tucumán": 930, "San Salvador de Jujuy": 1060, "Salta": 1090, "San Juan": 980, "Río Gallegos": 2390, "Santa Rosa": 980, "Santiago del Estero": 1020, "Ushuaia": 2650, "Viedma": 1060, "San Luis": 612, "Rosario": 957},
    "Posadas": {"Buenos Aires": 1095, "Córdoba": 1195, "Resistencia": 680, "Corrientes": 640, "Formosa": 680, "La Plata": 1095, "La Rioja": 1110, "Mendoza": 1300, "Neuquén": 1520, "Paraná": 820, "Rawson": 1530, "San Fernando del Valle de Catamarca": 1060, "San Miguel de Tucumán": 1040, "San Salvador de Jujuy": 1270, "Salta": 1300, "San Juan": 1070, "Río Gallegos": 2720, "Santa Rosa": 930, "Santiago del Estero": 920, "Ushuaia": 3070, "Viedma": 940, "San Luis": 1368, "Rosario": 792},
    "Neuquén": {"Buenos Aires": 1069, "Córdoba": 860, "Resistencia": 1180, "Corrientes": 1210, "Formosa": 1300, "La Plata": 1069, "La Rioja": 940, "Mendoza": 475, "Posadas": 1520, "Paraná": 940, "Rawson": 1160, "San Fernando del Valle de Catamarca": 980, "San Miguel de Tucumán": 930, "San Salvador de Jujuy": 1160, "Salta": 1190, "San Juan": 980, "Río Gallegos": 2060, "Santa Rosa": 700, "Santiago del Estero": 1020, "Ushuaia": 2640, "Viedma": 850, "San Luis": 571, "Rosario": 831},
    "Paraná": {"Buenos Aires": 691, "Córdoba": 560, "Resistencia": 660, "Corrientes": 590, "Formosa": 820, "La Plata": 691, "La Rioja": 780, "Mendoza": 935, "Posadas": 820, "Neuquén": 940, "Rawson": 1160, "San Fernando del Valle de Catamarca": 730, "San Miguel de Tucumán": 660, "San Salvador de Jujuy": 890, "Salta": 920, "San Juan": 710, "Río Gallegos": 2120, "Santa Rosa": 740, "Santiago del Estero": 860, "Ushuaia": 2370, "Viedma": 760, "San Luis": 830, "Rosario": 286},
    "Rawson": {"Buenos Aires": 1411, "Córdoba": 1550, "Resistencia": 1520, "Corrientes": 1440, "Formosa": 1380, "La Plata": 1411, "La Rioja": 1290, "Mendoza": 1565, "Posadas": 1530, "Neuquén": 1160, "Paraná": 1160, "San Fernando del Valle de Catamarca": 1410, "San Miguel de Tucumán": 1400, "San Salvador de Jujuy": 1630, "Salta": 1660, "San Juan": 1560, "Río Gallegos": 1062, "Santa Rosa": 1230, "Santiago del Estero": 1200, "Ushuaia": 1030, "Viedma": 950, "San Luis": 1114, "Rosario": 1203},
    "San Fernando del Valle de Catamarca": {"Buenos Aires": 995, "Córdoba": 634, "Resistencia": 970, "Corrientes": 970, "Formosa": 1060, "La Plata": 995, "La Rioja": 700, "Mendoza": 980, "Posadas": 1060, "Neuquén": 980, "Paraná": 730, "Rawson": 1410, "San Miguel de Tucumán": 640, "San Salvador de Jujuy": 870, "Salta": 900, "San Juan": 780, "Río Gallegos": 2450, "Santa Rosa": 810, "Santiago del Estero": 920, "Ushuaia": 2700, "Viedma": 880, "San Luis": 670, "Rosario": 1045},
    "San Miguel de Tucumán": {"Buenos Aires": 945, "Córdoba": 569, "Resistencia": 950, "Corrientes": 950, "Formosa": 1040, "La Plata": 945, "La Rioja": 640, "Mendoza": 930, "Posadas": 1040, "Neuquén": 930, "Paraná": 660, "Rawson": 1400, "San Fernando del Valle de Catamarca": 640, "San Salvador de Jujuy": 870, "Salta": 900, "San Juan": 780, "Río Gallegos": 2360, "Santa Rosa": 830, "Santiago del Estero": 920, "Ushuaia": 2610, "Viedma": 870, "San Luis": 738, "Rosario": 993},
    "San Salvador de Jujuy": {"Buenos Aires": 1085, "Córdoba": 799, "Resistencia": 1180, "Corrientes": 1180, "Formosa": 1270, "La Plata": 1085, "La Rioja": 870, "Mendoza": 1060, "Posadas": 1270, "Neuquén": 1160, "Paraná": 890, "Rawson": 1630, "San Fernando del Valle de Catamarca": 870, "San Miguel de Tucumán": 870, "Salta": 900, "San Juan": 1080, "Río Gallegos": 2450, "Santa Rosa": 970, "Santiago del Estero": 880, "Ushuaia": 2700, "Viedma": 880, "San Luis": 908, "Rosario": 1269},
    "Salta": {"Buenos Aires": 1125, "Córdoba": 829, "Resistencia": 1210, "Corrientes": 1210, "Formosa": 1300, "La Plata": 1125, "La Rioja": 900, "Mendoza": 1090, "Posadas": 1300, "Neuquén": 1190, "Paraná": 920, "Rawson": 1660, "San Fernando del Valle de Catamarca": 900, "San Miguel de Tucumán": 900, "San Salvador de Jujuy": 900, "San Juan": 1120, "Río Gallegos": 2450, "Santa Rosa": 990, "Santiago del Estero": 830, "Ushuaia": 2700, "Viedma": 990, "San Luis": 1045, "Rosario": 1342},
    "San Juan": {"Buenos Aires": 1015, "Córdoba": 710, "Resistencia": 990, "Corrientes": 980, "Formosa": 1070, "La Plata": 1015, "La Rioja": 980, "Mendoza": 980, "Posadas": 1070, "Neuquén": 980, "Paraná": 710, "Rawson": 1560, "San Fernando del Valle de Catamarca": 780, "San Miguel de Tucumán": 780, "San Salvador de Jujuy": 1080, "Salta": 1120, "Río Gallegos": 2340, "Santa Rosa": 750, "Santiago del Estero": 790, "Ushuaia": 2690, "Viedma": 880, "San Luis": 740, "Rosario": 536},
    "Río Gallegos": {"Buenos Aires": 2025, "Córdoba": 2130, "Resistencia": 2400, "Corrientes": 2420, "Formosa": 2500, "La Plata": 2025, "La Rioja": 2340, "Mendoza": 2390, "Posadas": 2720, "Neuquén": 2060, "Paraná": 2120, "Rawson": 1062, "San Fernando del Valle de Catamarca": 2450, "San Miguel de Tucumán": 2360, "San Salvador de Jujuy": 2450, "Salta": 2450, "San Juan": 2340, "Santa Rosa": 2139, "Santiago del Estero": 2420, "Ushuaia": 1100, "Viedma": 1770, "San Luis": 2024, "Rosario": 2402},
    "Santa Rosa": {"Buenos Aires": 630, "Córdoba": 754, "Resistencia": 1020, "Corrientes": 890, "Formosa": 930, "La Plata": 630, "La Rioja": 810, "Mendoza": 980, "Posadas": 930, "Neuquén": 700, "Paraná": 740, "Rawson": 1230, "San Fernando del Valle de Catamarca": 810, "San Miguel de Tucumán": 830, "San Salvador de Jujuy": 970, "Salta": 990, "San Juan": 750, "Río Gallegos": 2139, "Santiago del Estero": 800, "Ushuaia": 2340, "Viedma": 630, "San Luis": 657, "Rosario": 569},
    "Santiago del Estero": {"Buenos Aires": 910, "Córdoba": 670, "Resistencia": 800, "Corrientes": 880, "Formosa": 920, "La Plata": 910, "La Rioja": 920, "Mendoza": 1020, "Posadas": 920, "Neuquén": 1020, "Paraná": 860, "Rawson": 1200, "San Fernando del Valle de Catamarca": 920, "San Miguel de Tucumán": 920, "San Salvador de Jujuy": 880, "Salta": 830, "San Juan": 790, "Río Gallegos": 2420, "Santa Rosa": 800, "Ushuaia": 2770, "Viedma": 900, "San Luis": 817, "Rosario": 724},
    "Ushuaia": {"Buenos Aires": 2388, "Córdoba": 2350, "Resistencia": 2760, "Corrientes": 2790, "Formosa": 2850, "La Plata": 2388, "La Rioja": 2690, "Mendoza": 2650, "Posadas": 3070, "Neuquén": 2640, "Paraná": 2370, "Rawson": 1030, "San Fernando del Valle de Catamarca": 2700, "San Miguel de Tucumán": 2610, "San Salvador de Jujuy": 2700, "Salta": 2700, "San Juan": 2690, "Río Gallegos": 1100, "Santa Rosa": 2340, "Santiago del Estero": 2770, "Viedma": 1913, "San Luis": 2158, "Rosario": 2311},
    "Viedma": {"Buenos Aires": 791, "Córdoba": 921, "Resistencia": 870, "Corrientes": 900, "Formosa": 950, "La Plata": 791, "La Rioja": 880, "Mendoza": 1060, "Posadas": 940, "Neuquén": 850, "Paraná": 760, "Rawson": 950, "San Fernando del Valle de Catamarca": 880, "San Miguel de Tucumán": 870, "San Salvador de Jujuy": 880, "Salta": 990, "San Juan": 880, "Río Gallegos": 1770, "Santa Rosa": 630, "Santiago del Estero": 900, "Ushuaia": 1913, "San Luis": 511, "Rosario": 679},
    "San Luis": {"Buenos Aires": 814, "Córdoba": 390, "Resistencia": 1160, "Corrientes": 1097, "Formosa": 1241, "La Plata": 794, "La Rioja": 656, "Mendoza": 612, "Posadas": 1368, "Neuquén": 571, "Paraná": 830, "Rawson": 1114, "San Fernando del Valle de Catamarca": 670, "San Miguel de Tucumán": 738, "San Salvador de Jujuy": 908, "Salta": 1045, "San Juan": 740, "Río Gallegos": 2024, "Santa Rosa": 657, "Santiago del Estero": 817, "Ushuaia": 2158, "Viedma": 511, "Rosario": 612},
    "Rosario": {"Buenos Aires": 309, "Córdoba": 405, "Resistencia": 842, "Corrientes": 675, "Formosa": 843, "La Plata": 304, "La Rioja": 924, "Mendoza": 957, "Posadas": 792, "Neuquén": 831, "Paraná": 286, "Rawson": 1203, "San Fernando del Valle de Catamarca": 1045, "San Miguel de Tucumán": 993, "San Salvador de Jujuy": 1269, "Salta": 1342, "San Juan": 536, "Río Gallegos": 2402, "Santa Rosa": 569, "Santiago del Estero": 724, "Ushuaia": 2311, "Viedma": 679, "San Luis": 612}
}





            