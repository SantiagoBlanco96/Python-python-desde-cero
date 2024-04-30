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


print(distancias_linea_recta)

