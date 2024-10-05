import unicodedata
import markdown
import re
import json

class FileToProcess:
    def __init__(self, filepath):
        self.filepath = filepath

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


class GenDict:
    def __init__(self, content):
        self.content = content
        self.ref_dict = {}

    def gen_dict(self):
        for line in self.content:
            if ':' in line:
                key, value = line.split(':', 1)
                self.ref_dict[key.strip()] = value.strip()
        return self.ref_dict    

class GenHtml:
    def __init__(self, content):
        self.content = content

    def gen_html(self):
        html = markdown.markdown(' '.join(self.content))
        cleaned_html = re.sub(r'\s+', ' ', html)  # Collapse multiple spaces to one
        cleaned_html = re.sub(r'^\s+|\s+$', '', cleaned_html, flags=re.MULTILINE)  # Trim spaces at each line's start and end
        return cleaned_html
    
    



def main():

    cc_type = ['CC BY: https://creativecommons.org/licenses/by/4.0/', 'CC BY-SA: https://creativecommons.org/licenses/by-sa/4.0/', 'CC BY-NC: https://creativecommons.org/licenses/by-nc/4.0/', 'CC BY-NC-SA: https://creativecommons.org/licenses/by-nc-sa/4.0/', 'CC BY-ND: https://creativecommons.org/licenses/by-nd/4.0/', 'CC BY-NC-ND: https://creativecommons.org/licenses/by-nc-nd/4.0/', ' CC0: https://creativecommons.org/publicdomain/zero/1.0/']

    text_processor = FileToProcess('test.md')
    primary_content, secondary_content = text_processor.extract_content()

    primary_filename = 'processed_header.txt'
    secondary_filename = 'additional_content.txt'

    text_processor.write_to_file(primary_filename, primary_content)
    text_processor.write_to_file(secondary_filename, secondary_content)

    dict_processor = GenDict(primary_content)  # Generate dictionary from primary content
    prim_dict = dict_processor.gen_dict()

    html_processor = GenHtml(secondary_content)  # Generate HTML from secondary content
    html_text = html_processor.gen_html()

    prim_dict['html'] = html_text
    prim_dict['license'] = cc_type[0]
    
    #print(prim_dict)
    #print(html_text)


    with open('entries.json', 'w') as file:
        json.dump(prim_dict,file, indent=4)

if __name__ == '__main__':
    main()



