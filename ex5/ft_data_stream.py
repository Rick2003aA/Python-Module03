import random


def event_stream(n):
    event_list = ["found treasure", "leveled up", "kill monster"]
    for event_id in range(1, n + 1):
        if event_id % 3 == 1:
            player = "alice"
        elif event_id % 3 == 2:
            player = "bob"
        else:
            player = "charlie"

        level = (event_id * 3) % 15 + 1

        # if level >= 10 and event_id % 5 == 0:
        #     event_type = "found treasure"
        # elif event_id % 7 == 0:
        #     event_type = "leveled up"
        # else:
        #     event_type = "killed monster"
        event_type = random.choice(event_list)

        yield (event_id, player, level, event_type)


print("=== Game Data Stream Processor ===")
data_num = 1000
print()
print(f"Processing {data_num} game events ...")
total = 0
high_num = 0
for event_id, player, level, event_type in event_stream(1000):
    total += 1
    if level > 10:
        high_num += 1
    print(f"Event {event_id}: Player {player}(level {level}) {event_type}")
print("=== Stream Analytics ===")
print(f"Total events processed: {total}")
print(f"High-level players (+10): {high_num}")
print(f"Treasure events: {}")
print(f"Processing time: ")
