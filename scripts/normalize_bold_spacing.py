#!/usr/bin/env python3
import os
import re
import sys


def normalize_line(line: str) -> str:
    # Process only non-code inline segments (split by backticks)
    parts = line.split('`')
    for i in range(0, len(parts), 2):
        segment = parts[i]
        # Add space AFTER closing ** if followed by alnum
        segment = re.sub(r"\*\*(?=[A-Za-z0-9])", r"** ", segment)
        # Add space BEFORE opening ** if preceded by alnum
        segment = re.sub(r"(?<=[A-Za-z0-9])\*\*", r" **", segment)
        parts[i] = segment
    return '`'.join(parts)


def normalize_file(path: str) -> bool:
    try:
        with open(path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception:
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
        result_lines.append(new_line + ('\n' if raw_line.endswith('\n') else ''))

    if changed:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(''.join(result_lines))
    return changed


def main() -> int:
    changed_any = False
    for dirpath, _, filenames in os.walk('.'):
        for fn in filenames:
            if not (fn.endswith('.mdx') or fn.endswith('.md')):
                continue
            full_path = os.path.join(dirpath, fn)
            if normalize_file(full_path):
                changed_any = True
    print('changed' if changed_any else 'nochange')
    return 0


if __name__ == '__main__':
    sys.exit(main())


