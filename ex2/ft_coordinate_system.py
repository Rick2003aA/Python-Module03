import sys
import math


def create_position(x, y, z):
    return (x, y, z)


def parse_position(text):
    parts = text.split(",")
    try:
        x = int(parts[0])
        y = int(parts[1])
        z = int(parts[2])
        return (x, y, z)
    except ValueError as e:
        print(f"Parsing invalid coordinates: "
              f'"{parts[0]},{parts[1]},{parts[2]}"')
        print("Error parsing coordinates:", e)
        print("Error details - Type:", type(e).__name__, ", Args:", e.args)


def calc_distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return math.sqrt((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2)


print("=== Game Coordinate System ===\n")
argc = len(sys.argv)
if argc != 4:
    print("please enter with proper format")
    sys.exit(0)
try:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = int(sys.argv[3])
except ValueError as e:
    print(f"Parsing invalid coordinates: "
          f'"{sys.argv[1]},{sys.argv[2]},{sys.argv[3]}"')
    print("Error parsing coordinates:", e)
    print("Error details - Type:", type(e).__name__, ", Args:", e.args)

# set origin position
origin = create_position(0, 0, 0)

# Create player's position with formatted
pos1 = create_position(x, y, z)
print(f"Position created: {pos1}")
distance = calc_distance(origin, pos1)
print(f"Distance between {origin} and {pos1}: {distance:.2f}\n")

# Create player's position with string
print('Parsing coordinates: "3,4,0"')
pos2 = parse_position("3,4,0")
print(f"Parsed position: {pos2}")
distance = calc_distance(origin, pos2)
print(f"Distance between {origin} and {pos2}: {distance:.2f}\n")

# Bad input
pos3 = parse_position("abc,def,ghi")

# unpacking demonstration
print("\nUnpacking demonstration:")
x, y, z = pos2
print(f"Player at x={x}, y={y}, z={z}")
print(f"Coordinates: X={x}, Y={y}, Z={z}")
