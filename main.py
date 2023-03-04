#PSEUDO CODE

#scope -- simple
#materials -- limited scope, no importing of packages/modules just the basic Python library
#type -- CLI, not GUI or webapp
#len -- less than 200 lines of code 

#inputs -- add, modify, view, or delete expense (index number, type (fixed/one-off) data, payee, amount, description, mode, note )
#outputs -- view segments of expenses (total by time period, payee, type,), comparison (fixed this month vs last) ... uses classes?
#database- stores inputs, queried for outputs ... arrays and sub arrays?, need some key by which always identified like ID? 

#to do: pretty table, unique id, measures class


table = [['ID', 'Sum', 'Payee']]

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
              new_sum = input("Enter a new sum: ")
              x.insert(1, new_sum)
              return print(x)
            elif usr_inp == 'Payee':
              del[x[2]]
              print(x)
              new_payee = input("Enter a new payee: ")
              x.insert(2, new_payee)
              return print(x)
            else:
              break

class navMenus(modifyDb):
  def __init__(self):
    self.parent_menu_vis = """
*** MAIN MENU ***

Type '1' to see your expenses.

Type '2' to modify expenses.

Type '3' for metrics.

Type '4' to end program.\n
"""
    self.mod_menu_vis = """
Type 1' to add an expense.

Type '2' to delete an expense.

Type '3' to change expense details.

Type '4' to return to the parent menu.
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
      pass
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
      amount = round(float(add_exp[1]))
      payee = add_exp[2]
      mdb.add_expense(id, amount, payee)
      print(f'\nYour expense has been added:\n{table}')
      self.mod_menu()
    if modify_inpt == "2":
      del_exp = input("Enter ID of expense for deletion: ")
      id = del_exp
      mdb.del_expense(id)
      print(f'Expense ID {id} was deleted:\n{table}')
      self.mod_menu()
    if modify_inpt == "3":
      mod_exp = input("Enter ID of expense for modification: ")
      id = mod_exp
      mdb.mod_expense(id)
      self.mod_menu()
    if modify_inpt == "4":
      self.parent_menu()
  def print_db(self):
    for row in table:
      print(*row)
    self.parent_menu()
      

mdb = modifyDb()
nm = navMenus()

print("Welcome to Track-My-Expenses!\U0001F911\n")
nm.parent_menu()

