import utils

lines = list(utils.read_all_lines('./eval.csv'))[100:200]

source = []
target = []

for line in lines:
    line = line.split('$')
    if len(source) == len(target):
        source.append(line)
    else:
        target.append(line)

assert len(source) == len(target)

lines = []
for s, t in zip(source, target):
    assert len(s) == len(t)
    line = ''
    for x, y in zip(s, t):
        if y.startswith('S-'):
            line += f'<{y[2:]}>{x}</{y[2:]}>'
        elif y.startswith('B-'):
            line += f'<{y[2:]}>{x}'
        elif y.startswith('E-'):
            line += f'{x}</{y[2:]}>'
        else:
            line += x
    lines.append(line)

utils.write_all_lines('./eval.txt', lines)