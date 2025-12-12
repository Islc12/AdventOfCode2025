s = False
count = 0

with open('d7.txt', 'r') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    chars = list(line.rstrip('\n'))
    
    if not s and 'S' in chars:
        start_point = chars.index('S')
        if i + 1 < len(lines):
            next_chars = list(lines[i + 1].rstrip('\n'))
            next_chars[start_point] = '|'
            lines[i + 1] = ''.join(next_chars)
        s = True

    lines[i] = ''.join(chars)

for i in range(len(lines) - 1):
    chars = list(lines[i])
    beam_indices = [j for j, c in enumerate(chars) if c == '|']

    if not beam_indices:
        continue

    next_chars = list(lines[i + 1])

    for bi in beam_indices:
        if next_chars[bi] != '^':
            next_chars[bi] = '|'
        elif bi and next_chars[bi] == '^':
            next_chars[bi - 1] = '|'
            next_chars[bi + 1] = '|'
            count += 1
            
        lines[i + 1] = ''.join(next_chars)
    
    lines[i] = ''.join(chars)

for line in lines:
    print(line)

print(count)