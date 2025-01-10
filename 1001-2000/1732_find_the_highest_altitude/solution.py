gain = [-5, 1, 5, 0, -7]


def solve(gain: list):
    max_altitude = 0
    current_altitude = 0
    for item in gain:
        current_altitude = current_altitude + item
        max_altitude = max(current_altitude, max_altitude)

    return max_altitude


print(solve(gain))
