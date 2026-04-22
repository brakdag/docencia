import os
import re

def fix_utf8_escapes():
    pattern = re.compile(r'\\u([0-9a-fA-F]{4})')
    total_replacements = 0
    
    stack = ['capitulos/']
    while stack:
        current_dir = stack.pop()
        try:
            for entry in os.scandir(current_dir):
                if entry.is_dir():
                    stack.append(entry.path)
                elif entry.is_file() and entry.name.endswith('.tex'):
                    path = entry.path
                    try:
                        with open(path, 'r', encoding='utf-8') as f:
                            content = f.read()
                        
                        new_content, count = pattern.subn(lambda m: chr(int(m.group(1), 16)), content)
                        
                        if count > 0:
                            with open(path, 'w', encoding='utf-8') as f:
                                f.write(new_content)
                            print(f"{path}: {count} replacements made.")
                            total_replacements += count
                        else:
                            print(f"{path}: No replacements needed.")
                    except Exception as e:
                        print(f"Error processing file {path}: {e}")
        except Exception as e:
            print(f"Error scanning directory {current_dir}: {e}")
            
    print(f"\nTotal replacements across all files: {total_replacements}")

if __name__ == "__main__":
    fix_utf8_escapes()
