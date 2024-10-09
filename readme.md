# Overview

Writing a programme that will extract data from blog entries and return a JSON file.

# 2024.10.08

## 2 

I've been able to adjust the programme so it updatest the JSON file now. It's not quite perfect since it doesn't check if there is any repeated content in the file. But I think this is fine to build the JSON feed

## 1 

Unfortunately it seems the code is not behaving as expected. While it can write a blog post to a JSON file. It cannot write a subsequent post to the file.

The issue seems to be that I need to provide the programme with a UniqueKey. If I comment this section of the code out it also doesn't seem to work.

## Next steps 
- Let's see if I can generate a unique key, maybe some hashable value or even simply a string based on the content of the file.
- Check to see how to append to a JSON file in general. If you can do that then you should be able to apply it to this programme.



# 2024.10.05

## 1 

I have refactored the code to make it slightly tidier.

The next step is create a primary JSON file that all other files can be written to.

## 2 

The programme essentially does everything required at this point. I still feel that the extract content function could be neater, but it's fine.

## Next steps

- Prep JSON file 
- Figure out how to add it as a feature to ql-blog
- Anonymise 
- Write up 

# 2024.10.04

The programme now generates a JSON file based on a single blog post. Next I will tidy up the code, and then see if it's possible to a main JSON file that I can adjust on an ongoing basis.

I am attempting to refactor the code so that it's neater and more portable. Have seperated the html and dictionary elements. Just need to merge them once again, add the licensing, and convert to JSON.

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
