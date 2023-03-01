#PSEUDO CODE

#scope -- simple
#materials -- limited scope, no importing of packages/modules just the basic Python library
#type -- CLI, not GUI or webapp
#len -- less than 200 lines of code 

#inputs -- add, modify, view, or delete expense (index number, type (fixed/one-off) data, payee, amount, description, mode, note )
#outputs -- view segments of expenses (total by time period, payee, type,), comparison (fixed this month vs last) ... uses classes?
#database- stores inputs, queried for outputs ... arrays and sub arrays?, need some key by which always identified like ID? 

#okay, good progress so far ... next is to return user to previous input menu, return to parent input menu, print the table so it is legible
#as opposed to arrays, make sure no duplicate IDs ... generate unique ID by combination of inputs, new class for outputDB e.g. summing total
#expenses, expenses for certain payee etc. 

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
              return x.insert(1, new_sum)
            elif usr_inp == 'Payee':
              del[x[2]]
              print(x)
              new_payee = input("Enter a new payee: ")
              return x.insert(2, new_payee)
            else:
              break
    
db = modifyDb()

print("""
Welcome to Track-My-Expenses! 

Type '1' to see your expenses.

Type '2' to modify expenses.

Type '3' for metrics.\n
""")

open = input()


if open == "1":
  print(table)
if open == "2":
  print ("""
Type 1' to add an expense.

Type '2' to delete an expense.

Type '3' to change expense details.\n
  """)
  modify_inpt = input()
  if modify_inpt == "1":
    add_exp = input("Enter an expense in 'ID, Amount, Payee' format e.g. 1, 17.00, James: ").split(',')
    id = add_exp[0]
    amount = add_exp[1]
    payee = add_exp[2]
    db.add_expense(id, amount, payee)
    print(f'Your expense has been added:\n {table}')

