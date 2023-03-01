import re
import base64

input_file = open("input_file.txt", "r")

pattern = r"([a-zA-Z0-9_]+)\s*=\s*.*?b64decode\(b'([^']*)'\)"

for line in input_file:
    match = re.search(pattern, line)
    if match:
        variable = match.group(1)
        argument = match.group(2)

        a = base64.b64decode(argument)
        print(a)

input_file.close()
print('---- Ended ----')
