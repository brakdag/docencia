import os
import re

def is_latex_command(word):
    return word.startswith('\')

def is_mixed_alphanumeric(word):
    # Contains both letters and numbers
    has_digit = any(char.isdigit() for char in word)
    has_alpha = any(char.isalpha() for char in word)
    return has_digit and has_alpha

def is_unusual_spanish(word):
    # Spanish characters: a-z, A-Z, áéíóúÁÉÍÓÚñÑüÜ
    # We allow common punctuation and LaTeX symbols
    latex_symbols = r'\$%&_{}~^'
    # Remove latex symbols from the word to check orthography
    cleaned = re.sub(f'[{re.escape(latex_symbols)}]', '', word)
    if not cleaned:
        return False
    # Check if it contains characters not in Spanish alphabet or common punctuation
    # We look for characters that are not alphanumeric (Spanish) and not standard punctuation
    # This will flag things like 'w0rd' (via mixed) or '!!!' or 'abc@123'
    return bool(re.search(r'[^a-zA-ZáéíóúÁÉÍÓÚñÑüÜ\s.,;?!()\'"\-_]', cleaned))

def scan_files(directory):
    results = []
    if not os.path.exists(directory):
        return [f"Error: Directory {directory} not found"]
        
    for filename in os.listdir(directory):
        if filename.endswith('.tex'):
            path = os.path.join(directory, filename)
            try:
                with open(path, 'r', encoding='utf-8') as f:
                    for line_num, line in enumerate(f, 1):
                        # Simple heuristic to skip tables: lines starting with & or containing many &
                        if line.strip().startswith('&') or line.count('&') > 2:
                            continue
                        
                        # Split line into words
                        words = line.split()
                        for word in words:
                            # Strip trailing punctuation
                            clean_word = word.strip('.,;?!()[]{}')
                            
                            if not clean_word:
                                continue
                            
                            if is_latex_command(clean_word):
                                continue
                                
                            if is_mixed_alphanumeric(clean_word) or is_unusual_spanish(clean_word):
                                results.append(f"[{filename} | {line_num} | {clean_word}]")
            except Exception as e:
                results.append(f"Error reading {filename}: {e}")
    return results

if __name__ == "__main__":
    artifacts = scan_files('capitulos/')
    if not artifacts:
        print("No tokenization artifacts found.")
    else:
        for art in artifacts:
            print(art)