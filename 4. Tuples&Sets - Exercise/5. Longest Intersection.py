
def gen_seq(range_info):
    start, end = [int(x) for x in range_info.split(",")]
    return set(range(start, end + 1))

n = int(input())

best_inter = set()

for _ in range(n):
    line_parts = input().split("-")
    first_set = gen_seq(line_parts[0])
    second_set = gen_seq(line_parts[1])
    current_intersection = first_set.intersection(second_set)

    if len(current_intersection) > len(best_inter):
        best_inter = current_intersection

print(f"Longest intersection is [{', '.join([str(x) for x in best_inter])}] with length {len(best_inter)}")