import utils
import re

lines = []
for line in utils.read_all_lines('eval.processed.txt'):
    source = []
    target = []

    def process_others(start, end):
        for c in line[start:end]:
            source.append(c)
            target.append('O')
            
    def append_source(span):
        part = line[span[0]:span[1]]
        for c in part:
            source.append(c)

    def append_target(span, source_span):
        slen = source_span[1] - source_span[0]
        tag = line[span[0]:span[1]].upper()
        global target
        if slen == 1:
            target.append('S-' + tag)
        else:
            target += ['S-'+tag] + ['M-'+tag] * (slen-2) + ['E-'+tag]

    def join(tp):
        return '$'.join(tp)

    last_pos = 0
    for m in re.finditer(r'<(.*?)>(.*?)</.*?>', line):
        start, end = m.span(0)
        process_others(last_pos, start)
        last_pos = end
        append_source(m.span(2))
        append_target(m.span(1), m.span(2))
    process_others(last_pos, len(line))
    lines.append(join(source))
    lines.append(join(target))

utils.write_all_lines('eval.postprocessed.txt', lines)


