import pandas as pd
import numpy as np

# Set seed for reproducibility
np.random.seed(42)

def generate_building_data(n_samples=768):
    data = []
    
    # Standard architectural values for buildings
    compactness_values = [0.98, 0.90, 0.86, 0.82, 0.79, 0.76, 0.74, 0.71, 0.69, 0.66, 0.64, 0.62]
    orientations = [2, 3, 4, 5]  # North, East, South, West
    glazing_areas = [0.0, 0.1, 0.25, 0.4]
    glazing_dists = [0, 1, 2, 3, 4, 5]

    for i in range(n_samples):
        # Pick features
        cp = np.random.choice(compactness_values)
        height = 7.0 if cp > 0.75 else 3.5
        surface = 800 - (cp * 300) # Surface area inversely related to compactness
        wall = surface * 0.5
        roof = surface - wall
        orient = np.random.choice(orientations)
        glazing = np.random.choice(glazing_areas)
        dist = np.random.choice(glazing_dists)

        # Create synthetic Target Variables with some noise
        # Logic: Loads increase with surface area and glazing, decrease with compactness
        base_load = (surface * 0.05) + (glazing * 20) - (cp * 10)
        h_load = base_load + np.random.normal(0, 2)
        c_load = base_load * 1.2 + np.random.normal(0, 2)

        data.append([
            round(cp, 2), round(surface, 1), round(wall, 1), round(roof, 1),
            height, orient, glazing, dist, round(h_load, 2), round(c_load, 2)
        ])

    columns = [
        'Compactness_Index', 'Surface_Area', 'Wall_Area', 'Roof_Area',
        'Overall_Height', 'Orientation', 'Glazing_Area', 'Glazing_Dist',
        'Heating_Load', 'Cooling_Load'
    ]
    
    return pd.DataFrame(data, columns=columns)

# Generate and save
df = generate_building_data(768)
df.to_csv('building_energy_data.csv', index=False)

print("Success! 'building_energy_data.csv' has been created with 768 rows.")