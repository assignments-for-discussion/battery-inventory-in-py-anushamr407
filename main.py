def calculate_soh(present_capacity, rated_capacity):
    return (present_capacity / rated_capacity) * 100

def classify_battery(soh):
    if soh > 80:
        return "Healthy"
    elif 65 <= soh <= 80:
        return "Replace"
    else:
        return "Failed"

def count_battery_classification(present_capacities, rated_capacity=120):
    classifications = {"Healthy": 0, "Replace": 0, "Failed": 0}

    for capacity in present_capacities:
        soh = calculate_soh(capacity, rated_capacity)
        classification = classify_battery(soh)
        classifications[classification] += 1

    return classifications

# Example usage:
present_capacities = [105, 95, 60, 110, 75, 100]
classification_counts = count_battery_classification(present_capacities)

print("Classification Counts:")
for classification, count in classification_counts.items():
    print(f"{classification}: {count}")
