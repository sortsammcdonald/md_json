import unicodedata

class FileToProcess:
    def __init__(self, filepath):
        self.filepath = filepath

def extract_content(filepath):
    capturing = False
    content = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()  # Remove any leading/trailing whitespace
            if line == "---":
                if capturing:
                    break  # Stop capturing after the second marker
                else:
                    capturing = True  # Start capturing after the first marker
            elif capturing:
                content.append(line)  # Append line if capturing
    return content

def write_to_file(filename, content):
    with open(filename, 'w', encoding='utf-8') as file:
        for line in content:
            file.write(line + '\n')

def main():
    text_processor = FileToProcess('test.md')
    extracted_content = extract_content(text_processor.filepath)
    write_to_file('processed_header.txt', extracted_content)

if __name__ == '__main__':
    main()
