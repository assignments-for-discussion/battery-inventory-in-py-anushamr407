def count_batteries_by_health(present_capacities):
    counts = {
        "healthy": 0,
        "exchange": 0,
        "failed": 0
    }

    for capacity in present_capacities:
        soh = (capacity / 120.0) * 100.0  # Assuming rated capacity is 120 Ah

        if soh > 80.0:
            counts["healthy"] += 1
        elif 65.0 <= soh <= 80.0:
            counts["exchange"] += 1
        else:
            counts["failed"] += 1

    return counts

def test_bucketing_by_health():
    print("Counting batteries by SoH...\n")
    present_capacities = [115, 118, 80, 95, 91, 77]
    counts = count_batteries_by_health(present_capacities)
    assert(counts["healthy"] == 2)
    assert(counts["exchange"] == 3)
    assert(counts["failed"] == 1)
    print("Done counting :)")

if __name__ == '__main__':
    test_bucketing_by_health()
