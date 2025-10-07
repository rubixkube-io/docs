#!/usr/bin/env python3
import os
import re

def normalize_line(line: str) -> str:
    # Remove inner spaces inside bold markers: ** text ** -> **text**
    line = re.sub(r"\*\*\s+(.+?)\s+\*\*", r"**\1**", line)
    # Handle cases with space only on one side
    line = re.sub(r"\*\*\s+", r"**", line)
    line = re.sub(r"\s+\*\*", r"**", line)
    # Add space AFTER closing ** if followed by alnum/punct (but not another *)
    line = re.sub(r"\*\*([A-Za-z0-9])", r"** \1", line)
    # Add space BEFORE opening ** if preceded by alnum/punct (but not another *)
    line = re.sub(r"([A-Za-z0-9])\*\*", r"\1 **", line)
    # Normalize list item hyphen spacing before bold: -** -> - **
    line = re.sub(r"-\*\*", r"- **", line)
    return line

def normalize_file(path: str) -> bool:
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
    for raw_line in content.splitlines(True):  # keep line endings
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
            print(f'  Changed line: {repr(line)} -> {repr(new_line)}')
        result_lines.append(new_line + ('\n' if raw_line.endswith('\n') else ''))

    if changed:
        print(f'Writing {len(result_lines)} lines to {path}')
        with open(path, 'w', encoding='utf-8') as f:
            f.write(''.join(result_lines))
    else:
        print(f'No changes needed for {path}')

    return changed

# Test on just one file first
test_file = '/Users/magician/Documents/Dream/Code/docs/index.mdx'
changed = normalize_file(test_file)
print(f'File changed: {changed}')

# Now check if the bold issues are fixed
if changed:
    print("Checking if bold issues are fixed...")
    with open(test_file, 'r') as f:
        content = f.read()

    # Look for remaining bold issues
    issues = re.findall(r'\*\*\s+(.+?)\s+\*\*', content)
    if issues:
        print(f'Still found {len(issues)} bold formatting issues: {issues[:3]}...')
    else:
        print("All bold formatting issues appear to be fixed!")
