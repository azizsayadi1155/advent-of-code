# PART 1

counts_all = []
with open("/home/cachybtw/Downloads/input.txt", 'r') as f:
    for line in f:
        n_pos = 0
        n_neg = 0
        diffs = []
        sequence = line.split()
        for i in range(len(sequence)-1):
            diffs.append(int(sequence[i]) - int(sequence[i+1]))
            if (int(sequence[i]) - int(sequence[i+1]))>0:
                n_pos += 1
            else:
                n_neg += 1
        counts_all.append(1 if (sum(diff in [1, 2, 3, -1, -2, -3] for diff in diffs)==len(diffs) and ((n_pos>0 and n_neg==0)or(n_neg>0 and n_pos==0))) else 0)
print(sum(counts_all))


# PART 2
def is_safe(sequence):
    diffs = [int(sequence[i]) - int(sequence[i + 1]) for i in range(len(sequence) - 1)]
    if all(-3 <= diff <= -1 or 1 <= diff <= 3 for diff in diffs) and (
            all(diff > 0 for diff in diffs) or all(diff < 0 for diff in diffs)
    ):
        return True
    return False

safe_count = 0

with open("/home/cachybtw/Downloads/input.txt", "r") as f:
    for line in f:
        sequence = line.split()

        if is_safe(sequence):
            safe_count += 1
            continue

        for i in range(len(sequence)):
            new_sequence = sequence[:i] + sequence[i + 1:]
            if is_safe(new_sequence):
                safe_count += 1
                break

print(safe_count)