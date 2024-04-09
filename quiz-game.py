questions = [
  {
    "prompt": "What is the capital of India?",
    "options": ["A. Delhi", "B. Goa", "C. Karnataka", "D. Gujarat"],
    "answer": "A"
  },
  {
    "prompt": "Which language is primarily spoken in USA?",
    "options": ["A. Spanish", "B. Kannada", "C. French", "D. English"],
    "answer": "D"
  },
  {
    "prompt": "What is the smallest prime number?",
    "options": ["A. 0", "B. 1", "C. 2", "D. 3"],
    "answer": "C"
  },
  {
    "prompt": "Who is the CEO of Apple?",
    "options": ["A. Elon Musk", "B. Tim Cook", "C. Jeff Bezos", "D. Bill Gates"],
    "answer": "B"
  }
]

def run_quiz(questions):
  score = 0
  
  for question in questions:
    print(question["prompt"])
    for option in question["options"]:
      print(option)
    if input("Enter your answer (A, B, C or D): ").upper() == question["answer"]:
      print("Correct, horray!!!\n")
      score += 1
    else:
      print("Wrong, loser!!!\n The correct answer was ", question["answer"], "\n")
    
  print(f"You got {score} out of {len(questions)} questions correct.")

run_quiz(questions)
