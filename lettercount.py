# Open file  --done
# Read file (optional: close file) - done
# Loop through text using char - done (essentially telling the computer to read each character on the "list")
# Convert each char in lowercase - done
# Find ordinal value to each char -done
# Create list - done
# Add counter - done
# For every repeated char, increment counter by 1
# Print list
# Pipe through spark utiliy on Python!
# Celebrate!




f = open("text.txt")
filetext = f.read()
f.close()
#print filetext
filetext.lower()

char_count = [0] * 26

for char in filetext:
    if ord(char) > 97 and ord(char) < 122:
        char_count[ord(char)-97] += 1
print char_count

