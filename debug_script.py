#!/usr/bin/env python3
import os
import re

def normalize_line(line: str) -> str:
    line = re.sub(r"\*\*\s+(.+?)\s+\*\*", r"**\1**", line)
    line = re.sub(r"\*\*\s+", r"**", line)
    line = re.sub(r"\s+\*\*", r"**", line)
    line = re.sub(r"-\*\*", r"- **", line)
    line = re.sub(r"\*\*([A-Za-z0-9])", r"** \1", line)
    line = re.sub(r"([A-Za-z0-9])\*\*", r"\1 **", line)
    return line

# Test the file processing logic manually
path = '/Users/magician/Documents/Dream/Code/docs/index.mdx'

with open(path, 'r') as f:
    content = f.read()

print(f'Original file size: {len(content)}')

# Process the file
in_code_block = False
changed = False
result_lines = []

for i, raw_line in enumerate(content.splitlines(True)):
    line = raw_line.rstrip('\n')
    if re.match(r'^\s*```', line):
        in_code_block = not in_code_block
        result_lines.append(raw_line)
        continue
    if in_code_block:
        result_lines.append(raw_line)
        continue

    new_line = normalize_line(line)
    if new_line != line:
        changed = True
        print(f'Line {i+1} changed:')
        print(f'  Before: {repr(line)}')
        print(f'  After:  {repr(new_line)}')
    result_lines.append(new_line + ('\n' if raw_line.endswith('\n') else ''))

if changed:
    print(f'Would write {len(result_lines)} lines')
    print('Changes detected!')
else:
    print('No changes detected')
