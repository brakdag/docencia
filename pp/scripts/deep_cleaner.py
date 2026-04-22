import re

FILES = [
    'capitulos/individual/02_idea.tex',
    'capitulos/individual/02_kanban.tex',
    'capitulos/proyecto/02_idea.tex',
    'capitulos/proyecto/02_kanban.tex'
]

def is_corrupted(word):
    # A word is corrupted if it contains both letters and numbers
    has_letter = any(c.isalpha() for c in word)
    has_digit = any(c.isdigit() for c in word)
    return has_letter and has_digit

def main():
    for path in FILES:
        try:
            with open(path, 'r', encoding='utf-8') as f:
                for line_num, line in enumerate(f, 1):
                    # Split by whitespace
                    words = line.split()
                    for word in words:
                        # Ignore LaTeX commands
                        if word.startswith('\'):
                            continue
                        
                        # Clean word from common punctuation at ends
                        clean_word = word.strip('.,;:()"'{}[]')
                        
                        if is_corrupted(clean_word):
                            print(f'FILE: {path} | LINE: {line_num} | CORRUPTED: {clean_word}')
        except FileNotFoundError:
            print(f'ERR: File not found {path}')
        except Exception as e:
            print(f'ERR: {e}')

if __name__ == '__main__':
    main()