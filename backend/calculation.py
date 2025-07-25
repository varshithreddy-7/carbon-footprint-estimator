def estimate_travel_footprint(km_per_week, transport_type):
    factors = {
        "car": 0.2,
        "bus": 0.1,
        "train": 0.05,
        "bike": 0,
        "walk": 0
    }
    return km_per_week * 52 * factors.get(transport_type, 0.2)

def estimate_food_footprint(diet_type):
    footprints = {
        "meat_heavy": 3.3,
        "average": 2.5,
        "vegetarian": 1.7,
        "vegan": 1.5
    }
    return footprints.get(diet_type, 2.5) * 1000

def estimate_electricity_footprint(kwh_per_month):
    return kwh_per_month * 12 * 0.85

def calculate_total(travel_km, transport_type, diet_type, electricity_kwh):
    travel_kg = estimate_travel_footprint(float(travel_km), transport_type)
    food_kg = estimate_food_footprint(diet_type)
    electricity_kg = estimate_electricity_footprint(float(electricity_kwh))
    total = travel_kg + food_kg + electricity_kg
    return round(total, 2), round(travel_kg, 2), round(food_kg, 2), round(electricity_kg, 2)

