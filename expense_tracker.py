def add_expense(expenses, description, amount, category):
    new_expense = {"description": description, "amount": amount, "category": category}
    expenses.append(new_expense)
    return expenses
