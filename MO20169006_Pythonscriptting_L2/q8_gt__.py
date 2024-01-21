class length_comparator:
    def __init__(self, string):
        self.string = string

    def __gt__(self, another):
        return len(self.string) > len(another.string)


# Example usage
string1 = length_comparator("afysswukopxkkz")
string2 = length_comparator("ifgers")

if string1 > string2:
    print("String 1 is longer than String 2.")
else:
    print("String 1 is not longer than String 2.")
