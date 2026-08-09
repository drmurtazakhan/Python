# Python pin_extractor.py
def pin_extractor(poem):
    secret_code = ""

    lines = poem.split("\n")    
    print(lines[0])

    words_line0 = lines[0].split()
    print(words_line0)

    for line_index, line in enumerate(lines):
        words = line.split()

        if line_index < len(words):
            secret_code += str(len(words[line_index]))
        else:
            secret_code += "0"

    return secret_code

poem = """Stars and the moon
shine in the sky
white and
until the end of the night"""

print(pin_extractor(poem))