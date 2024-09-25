def extract_content(lines):
    capturing = False
    content = []
    for line in lines:
        line = line.strip()  # Remove any leading/trailing whitespace
        if line == "---":
            if capturing:
                # We've reached the second marker, stop capturing
                break
            else:
                # We've reached the first marker, start capturing
                capturing = True
        elif capturing:
            # If we're between markers, capture the line
            content.append(line)
    return content

def write_to_file(filename, content):
    with open(filename, 'w') as f:
        for line in content:
            f.write(line + '\n')

# Sample data simulating the file read operation
lines = [
    "---",
    "layout: ../../layouts/MarkdownPostLayout.astro",
    "title: \"What I've been up to 2\"",
    "pubDate: 2024-09-10",
    "description: \"Review of activities from the second quarter of 2024\"",
    "author: 'William Samuel McDonald'",
    "tags: [\"education\", \"programming\", \"python\", \"haskell\"]",
    "---"
]

# Extract content
extracted_content = extract_content(lines)

# Write to file
write_to_file('header.txt', extracted_content)
