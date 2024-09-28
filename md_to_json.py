import unicodedata

class FileToProcess:
    def __init__(self, filepath):
        self.filepath = filepath
        self.ref_dict = {}

    def extract_content(self):
        capturing = False
        content = []
        with open(self.filepath, 'r', encoding='utf-8') as file:
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

    def write_to_file(self, filename, content):
        with open(filename, 'w', encoding='utf-8') as file:
            for line in content:
                file.write(line + '\n')

    def gen_dic(self, content):
        lines = content
        for line in lines:
            if ':' in line:  # Ensure there is a colon to split on
                key, value = line.split(':', 1)  # Only split on the first colon
                self.ref_dict[key.strip()] = value.strip()

def main():
    text_processor = FileToProcess('test.md')
    extracted_content = text_processor.extract_content()
    text_processor.write_to_file('processed_header.txt', extracted_content)
    text_processor.gen_dic(extracted_content)
    print(text_processor.ref_dict)  # Display the dictionary to see the results

if __name__ == '__main__':
    main()
