import random

words = [
    {"kannada": "ಮತ್ತು", "english": ["and"]},
    {"kannada": "ಇದು", "english": ["this"]},
    {"kannada": "ಆ", "english": ["that"]},
    {"kannada": "ಒಂದು", "english": ["one", "a", "an"]},
    {"kannada": "ಹೌದು", "english": ["yes"]},
    {"kannada": "ಇಲ್ಲ", "english": ["no", "not"]},
    {"kannada": "ಬಂದ", "english": ["came"]},
    {"kannada": "ನೋಡಿದ", "english": ["saw", "looked"]},
    {"kannada": "ಮಾಡಿದ", "english": ["did", "made"]},
    {"kannada": "ಅವನು", "english": ["he"]},
    {"kannada": "ಅವಳು", "english": ["she"]},
    {"kannada": "ನಾವು", "english": ["we"]},
    {"kannada": "ನೀವು", "english": ["you"]},
    {"kannada": "ಅವರು", "english": ["they"]},
    {"kannada": "ಇಲ್ಲಿ", "english": ["here"]},
    {"kannada": "ಅಲ್ಲಿ", "english": ["there"]},
    {"kannada": "ಯಾವಾಗ", "english": ["when"]},
    {"kannada": "ಹೇಗೆ", "english": ["how"]},
    {"kannada": "ಏನು", "english": ["what"]},
    {"kannada": "ಯಾರು", "english": ["who"]}
]


def quizUser(words):
  random.shuffle(words)
  score = 0

  for word in words[:5]:
    print(f"What is the English translation of '{word['kannada']}'?")
    userAns = input("Your answer: ").strip().lower()

    if userAns in word["english"]:
      print("Correct!\n")
      score += 1
    else:
      print(f"Wrong! The corect answer is '{'/'.join(word['english'])}'. \n")
  
  print(f"Quiz complete! Your score: {score}/5")
  
def main():
  print("Welcome to the Language Learning Flashcards App!")
  input("Press enter to start the quiz...")
  quizUser(words)

if __name__ == "__main__":
  main()