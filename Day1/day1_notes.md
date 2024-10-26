The first part was no problem at all using regular expressions.

I thought I could just use re and re.sub() for the second part but then realized that there were substrings like "oneight".
Hence, re was not the answer, and neither was simply replacing by "1".

The solution is admittedly hacky. Maybe I should redo it.