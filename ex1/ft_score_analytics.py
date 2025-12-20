import sys


def make_analytics(list, argc):
    total_players = argc - 1
    total = 0
    for i in list:
        total += i
    average = total / total_players
    highest = max(list)
    lowest = min(list)
    range = highest - lowest
    print(list)
    print(f"Total players: {total_players}")
    print(f"Total score: {total}")
    print(f"Average score: {average}")
    print(f"High score: {highest}")
    print(f"Low score: {lowest}")
    print(f"Score range: {range}")


print("=== Player Score Analytics ===")
argc = len(sys.argv)
list = []
i = 1
if argc == 1:
    print("No scores provided. Usage:"
          "python3 ft_score_analytics.py <score1> <score2> ...")
    sys.exit(0)
while i < argc:
    try:
        list.append(int(sys.argv[i]))
    except ValueError:
        print(f"'{sys.argv[i]}' is invalid. please enter numbers")
        sys.exit(1)
    i += 1
make_analytics(list, argc)
