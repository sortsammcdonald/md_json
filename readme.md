# Overview

Writing a programme that will extract data from blog entries and return a JSON file.

# 2024.10.04

The programme now generates a JSON file based on a single blog post. Next I will tidy up the code, and then see if it's possible to a main JSON file that I can adjust on an ongoing basis.

# 2024.10.02

Partial progress. I now have the html properly formatted and going into a dictionary. However I have not been able to extract the CC information correctly. I have to have a closer look at this.

# 2024.10.01

The programme can now extract the second section. Next I should convert this to html.

The programme outputs a file contaning the HTML now.

## Next steps
- Format the html to remove lines and unnecessary white space.
- Extract licensing information
- Append dict with relevant html and licencing info
- Write a JSON file
- Potentailly tidy up code, probably only necessary to write JSON file at the end, not write the incremental files along the way.

# 2024.09.30

Not sure how to tell the programme to start capturing text after the second --- symbol.

# 2024.09.28

Have been able to generate a dictionary containing the header materials.

## Next steps
- Convert main body text into html
- Decide to extract licensing info before or after HTML conversion

# 2024.09.24

Some slight progress. The header is now being extracted and added to its own file.

Next steps should be to create a readable object and then doing the processing on that.

Made some additional progress, the programme can now take a blog post and write the header material out in a seperate file.

## Next steps

- Extract the other sections of text and output them as seperate files
- Convert the output file to a diction 
- Merge seperate files into one file
- Append merged file to Main JSON file

# 2024.09.21

Maybe I can modify some elements from the Markov proj to extract the Astro metadata and copyright info.
