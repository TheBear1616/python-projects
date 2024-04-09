import json

def addExpense(expenses, description, amount):
  expenses.append({"description": description, "amount": amount})
  print(f"Added Expense: {description}, Amount: {amount}")

def getTotalExpense(expenses):
  totalExpense = 0
  for expense in expenses:
    totalExpense += expense['amount']
  return totalExpense

def getBalance(budget, expenses):
  return budget - getTotalExpense(expenses)

def showBudgetDetails(budget, expenses):
  print(f"Total Budget: {budget}")
  print("Expenses:")
  for expense in expenses:
    print(f" - {expense['description']}: {expense['amount']}")
  print(f"Total Spent: {getTotalExpense(expenses)}")
  print(f"Remaining Balance: {getBalance(budget, expenses)}")

def loadBudgetData(filePath):
  try:
    with open(filePath, 'r') as file:
      data = json.load(file)
      return data['initialBudget'], data['expenses']
  except (FileNotFoundError, json.JSONDecodeError):
    return 0, []
  
def saveBudgetDetails(filePath, initialBudget, expenses):
  data = {
    "initialBudget": initialBudget,
    "expenses": expenses
  }
  with open(filePath, 'w') as file:
    json.dump(data, file, indent=4)

def main():
  print("Welcome to the Budget App!\n")
  filePath = "budget-data.json"
  initialBudget, expenses = loadBudgetData(filePath)
  if initialBudget == 0:
    initialBudget = float(input("Please enter your budget: "))
  budget = initialBudget

  while True:
    print("\n What would you like to do?")
    print("1. Add an expense")
    print("2. Show budget details")
    print("3. Exit")
    choice = input("Enter your choice (1, 2, or 3): ")

    if choice == "1":
      description = input("Enter expense description: ")
      amount = float(input("Enter expense amount: "))
      addExpense(expenses, description, amount)
    elif choice == "2":
      showBudgetDetails(budget, expenses)
    elif choice == "3":
      saveBudgetDetails(filePath, initialBudget, expenses)
      print("Exiting Budget Application. GoodBye!!!\n")
      break
    else:
      print("Invalid choice, please choose again.\n")

if __name__ == "__main__":
  main()