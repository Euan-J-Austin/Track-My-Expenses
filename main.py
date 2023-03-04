#PSEUDO CODE

#scope -- simple
#materials -- limited scope, no importing of packages/modules just the basic Python library
#type -- CLI, not GUI or webapp
#len -- less than 200 lines of code 

#inputs -- add, modify, view, or delete expense (index number, type (fixed/one-off) data, payee, amount, description, mode, note )
#outputs -- view segments of expenses (total by time period, payee, type,), comparison (fixed this month vs last) ... uses classes?
#database- stores inputs, queried for outputs ... arrays and sub arrays?, need some key by which always identified like ID? 

#to do: unique id, and print alignments, make mod menu actions a separate class


table = [[1,17,'James'], [2,10,'Henry'],[3,3,'James']]

class modifyDb:
    def __init__(self):
        pass
    def add_expense(self, ID, Amount, Payee):
        return table.append([ID, Amount, Payee])
    def del_expense(self, ID):
        for x in table:
          if x[0] == ID:
            return table.remove(x)
    def mod_expense(self, ID):
        for x in table:
          if x[0] == ID:
            print(x)
            usr_inp = input("Enter the feature you wish to modify e.g. 'Sum': ")
            if usr_inp == 'Sum':
              del[x[1]]
              print(x)
              new_sum = input("\nEnter a new sum: ")
              x.insert(1, new_sum)
              return print(f'\nSum modified:\n{x}')
            elif usr_inp == 'Payee':
              del[x[2]]
              print(x)
              new_payee = input("\nEnter a new payee: ")
              x.insert(2, new_payee)
              return print(f'\nPayee modified:\n{x}')
              
class measureDb():
  def __init__(self):
    pass
  def total_expenses(self):
    total_expenses = int(sum([0 + int(x[1]) for x in table if x[1] != 'Sum']))
    print(f'\nYour total expenses are £{total_expenses}')
  def payee_stats(self):
    total_expenses = int(sum([0 + int(x[1]) for x in table if x[1] != 'Sum']))
    payee_name = input("Enter the payee's name: ")
    payee_total = sum([0 + x[1] for x in table if x[2] == payee_name])
    payee_perc = round(int(payee_total)/total_expenses * 100, ndigits = 2)
    print(f'\nYou paid {payee_name} £{payee_total}, this accounts for {payee_perc}% of your total expenses.')
  def over_amt(self):
    amt = int(input("\nEnter an amount: "))
    total_counter = 0
    for x in table:
      if int(x[1]) > amt:
        total_counter += 1
      elif int(x[1]) > amt == 0:
        print(f'\nYou have not paid out a sum greater than £{amt}')
    print(f'\nYou have {total_counter} transactions over £{amt}.')

class navMenus(modifyDb, measureDb):
  def __init__(self):
    self.parent_menu_vis = """
*** MAIN MENU ***

Type '1' to see your expenses.

Type '2' to modify expenses.

Type '3' for metrics.

Type '4' to end program.\n
"""
    self.mod_menu_vis = """
*** MODIFICATION MENU ***

Type 1' to add an expense.

Type '2' to delete an expense.

Type '3' to change expense details.

Type '4' to return to the main menu.\n
  """
    self.metric_menu_vis = """
*** METRICS MENU ***

Type '1' to see your total expenses.

Type '2' to find statistics about a payee.

Type '3' to find total payments over a given amount.

Type '4' to return to the main menu.\n
"""
    self.end_message = '\nClosing Track-My-Expenses.'
  def parent_menu(self):
    print(self.parent_menu_vis)
    open = input()
    if open == "1":
      self.print_db()
    if open == "2":
      self.mod_menu()
    if open == "3":
      self.metric_menu()
    if open == "4":
      print(self.end_message)
      while 1 == 1:
        break
  def mod_menu(self):
    print(self.mod_menu_vis)
    self.mod_menu_actions()
  def mod_menu_actions(self):
    modify_inpt = input()
    if modify_inpt == "1":
      add_exp = input("\nEnter an expense for addition in the 'ID, Amount, Payee' format e.g. 1, 17.00, James: ").split(',')
      id = add_exp[0]
      amount = round(float(add_exp[1]), ndigits = 2)
      payee = add_exp[2]
      mdb.add_expense(id, amount, payee)
      print(f'\nYour expense has been added:\n{table}')
      self.mod_menu()
    if modify_inpt == "2":
      del_exp = input("Enter ID of expense for deletion: ")
      ID = del_exp
      mdb.del_expense(ID)
      print(f'Expense ID {del_exp} was deleted:\n{table}')
      self.mod_menu()
    if modify_inpt == "3":
      mod_exp = input("Enter ID of expense for modification: ")
      ID = int(mod_exp)
      #this need to be passed as an integer for the function to work
      mdb.mod_expense(ID)
      self.mod_menu()
    if modify_inpt == "4":
      self.parent_menu()
  def metric_menu(self):
    print(self.metric_menu_vis)
    metric_input = input()
    if metric_input == '1':
      measureDb.total_expenses(self)
      self.metric_menu()
    if metric_input == '2':
      measureDb.payee_stats(self)
      self.metric_menu()
    if metric_input == '3':
      measureDb.over_amt(self)
      self.metric_menu()
    if metric_input == '4':
      self.parent_menu()
  def print_db(self):
    table.insert(0, ['ID', 'Sum', 'Payee'])
    for row in table:
      print(*row)
    self.parent_menu()

mdb = modifyDb()
nm = navMenus()

print("Welcome to Track-My-Expenses!\U0001F911\n")
nm.parent_menu()