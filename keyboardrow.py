# Scenario:
# Imagine you're developing a language learning application that focuses on helping users type words correctly. One feature of your app is to identify and categorize words based on the rows of the keyboard they can be typed with. This feature could be particularly useful for new typists or language learners, as it can help them practice words that require minimal finger movement.

# Objective:
# You want to identify and highlight words that can be typed using letters from only one row of the keyboard. This helps beginners focus on typing simpler words first, improving their typing efficiency and confidence.

# Code

firstRow = "qwertyuiop"
secondRow = "asdfghjkl"
thirdRow = "zxcvbnm"
rows = [firstRow,secondRow,thirdRow]
words = ["Hello","Alaska","Dad","Peace","cvm","8"]

def check_rows(row):
    valid_words = []
    for word in words:
        word = word.lower()
        if all(letter in row for letter in word):
            valid_words.append(word)
    return valid_words

for row in rows:
    result = check_rows(row)
    if result:
        print(f"Words that can be typed using row '{row}': {result}")