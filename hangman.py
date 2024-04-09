import random

words = ["python", "java", "kotlin", "javascript", "ruby", "swift"]

chosenWord = random.choice(words)
wordDisplay = ["_" for _ in chosenWord]
attempts = 9

print("Welcome to Hangman!!!\n")
print("Guess the programming language.\n")
print(f"You've got {attempts} attempts.\n")

while attempts > 0 and "_" in wordDisplay:
  print("".join(wordDisplay) + "\n")
  guess = input("Guess a letter: ").lower()
  if guess in chosenWord:
    for idx, letter in enumerate(chosenWord):
      if letter == guess:
        wordDisplay[idx] = guess
  else:
    print("That letter doesn't appear in the word, idiot!!!.\n")
    attempts -= 1
    print(f"{attempts} left.\n")

if "_" not in wordDisplay:
  print("".join(wordDisplay) + "\n")
  print("You guessed the word correct!")
  print("You survived!")
else:
  print("You ran out of attempts. The word was: " + chosenWord)
  print("You lost!")
