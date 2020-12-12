import sys

adapters = list(sorted([int(line.strip()) for line in sys.stdin.readlines()]))

joltage = 0
one_jolt_cnt = 0
three_jolt_cnt = 1
target = adapters[-1] + 3
print(adapters)
print("Target: {} with {} adapters".format(target, len(adapters)))
for adapter in adapters:
    diff = abs(joltage - adapter)
    if not (1 <= diff <= 3):
        print("Skipping")
        continue
    if diff == 1:
        one_jolt_cnt += 1
    elif diff == 3:
        three_jolt_cnt += 1
    joltage = adapter

print("Part1: 1-jolt: {}, 3-jolt: {}, product: {}".format(one_jolt_cnt, three_jolt_cnt, one_jolt_cnt*three_jolt_cnt))

scores = {}
adapters += [0, max(adapters) + 3]
adapters.sort()
adapters.reverse()
for key, adapter in enumerate(adapters):
    next_adapters = adapters[:key][-3:]

    if not next_adapters:
        scores[adapter] = 1
        continue

    scores[adapter] = 0
    for next_adapter in next_adapters:
        is_valid = next_adapter - adapter <= 3
        if is_valid:
            scores[adapter] += scores[next_adapter]
            # print('Count', scores[adapter], 'Next adapter', next_adapter)

print('Part2 {}'.format(scores[0]))
