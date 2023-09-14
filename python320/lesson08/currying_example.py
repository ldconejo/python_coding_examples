def your_weight_per_planet(planet, weight):
    planets = {
        'mercury': 0.38,
        'venus': 0.9,
        'earth': 1.0,
        'mars': 0.38,
        'jupiter': 2.53,
        'saturn': 1.07,
        'uranus': 0.89,
        'neptune': 1.14
    }

    return planets[planet]*weight

def custom_weight(planet):
    def your_weight(weight):
        return your_weight_per_planet(planet, weight)
    return your_weight