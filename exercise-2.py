# exercise-02 Length of Phrase

# Write the code that:
# 1. Prompts the user to enter a phrase:
#      Please enter a word or phrase: 
# 2. Print the following message:
#      - What you entered is xx characters long
# 3. Return to step 1, unless the word 'quit' was entered.

phrase = input("Please enter a word or phrase:")

while phrase != "quit":
    print(f"what you entered is {len(phrase)} characters long")
    print("type 'quit' to exit loop")
    phrase = input("Please enter a word or phrase:")

