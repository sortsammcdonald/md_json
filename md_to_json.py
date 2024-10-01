import unicodedata
import markdown

class FileToProcess:
    def __init__(self, filepath):
        self.filepath = filepath
        self.ref_dict = {}

    def extract_content(self):
        capturing = False
        content = []
        additional_content = []
        second_marker_found = False
        with open(self.filepath, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.strip()
                if line == "---":
                    if capturing:
                        if second_marker_found:
                            break
                        second_marker_found = True
                        continue
                    capturing = True
                    continue
                if second_marker_found:
                    additional_content.append(line)
                elif capturing:
                    content.append(line)
        return content, additional_content

    def write_to_file(self, filename, content):
        with open(filename, 'w', encoding='utf-8') as file:
            for line in content:
                file.write(line + '\n')

    def gen_dict(self, content):
        for line in content:
            if ':' in line:
                key, value = line.split(':', 1)
                self.ref_dict[key.strip()] = value.strip()

    def gen_html(self, filename):
        with open(filename, "r", encoding="utf-8") as input_file:
            text = input_file.read()
        html = markdown.markdown(text)
        return html

def main():
    text_processor = FileToProcess('test.md')
    primary_content, secondary_content = text_processor.extract_content()

    primary_filename = 'processed_header.txt'
    secondary_filename = 'additional_content.txt'

    text_processor.write_to_file(primary_filename, primary_content)
    text_processor.write_to_file(secondary_filename, secondary_content)

    text_processor.gen_dict(primary_content)  # Generate dictionary from primary content

    html_text = text_processor.gen_html(secondary_filename)  # Generate HTML from secondary content

    print(text_processor.ref_dict)  # Display the dictionary to see the results
    print(html_text)  # Display generated HTML

if __name__ == '__main__':
    main()
