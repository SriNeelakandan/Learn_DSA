# Problem statement:
"""
There is a sentence that consists of space-separated strings of upper and lower case English letters. Transform each string according to the given algorithm and return the new sentence.
Each string should be modified as follows:
The first character of the string remains unchanged
For each subsequent character, say x, consider a letter preceding it, say y:
If y precedes x in the English alphabet, transform x to uppercase
If x precedes y in the English alphabet, transform x to lowercase
If x and y are equal, the letter remains unchanged
"""