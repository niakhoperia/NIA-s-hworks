#Can you find the needle in the haystack?
#Write a function findNeedle() that takes an array full of junk but containing one "needle"
#After your function finds the needle it should return a message (as a string) that says:
#"found the needle at position " plus the index it found the needle, so
def find_needle(haystack):
    if "needle" in haystack:
        index = haystack.index("needle")
        return "found the needle at position {index}"
    else:
        return "needle not found in the haystack"
