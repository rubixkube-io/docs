#!/usr/bin/env python3
import os
import re

def normalize_line(line: str) -> str:
    # Remove inner spaces inside bold markers: ** text ** -> **text**
    line = re.sub(r"\*\*\s+(.+?)\s+\*\*", r"**\1**", line)

    # Handle cases with space only on one side
    line = re.sub(r"\*\*\s+", r"**", line)
    line = re.sub(r"\s+\*\*", r"**", line)

    # Normalize list item hyphen spacing before bold: -** -> - **
    line = re.sub(r"-\*\*", r"- **", line)

    # Add proper spacing around bold markers only where needed
    line = re.sub(r"\*\*([A-Za-z0-9])", r"** \1", line)
    line = re.sub(r"([A-Za-z0-9])\*\*", r"\1 **", line)

    return line

def test_normalize_file():
    path = '/Users/magician/Documents/Dream/Code/docs/index.mdx'

    print(f'Processing file: {path}')
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f'Error reading file: {e}')
        return False

    in_code_block = False
    changed = False
    result_lines = []

    for i, raw_line in enumerate(content.splitlines(True)):
        line = raw_line.rstrip('\n')
        if re.match(r"^\s*```", line):
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
        print(f'Writing {len(result_lines)} lines to {path}')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(''.join(result_lines))
        print('File updated successfully!')
    else:
        print('No changes needed for this file')

    return changed

# Test on the index.mdx file
test_normalize_file()
