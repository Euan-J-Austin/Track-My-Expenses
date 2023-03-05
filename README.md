# Track-My-Expenses

My first Python project!

The first of four 'simple' projects for my Python portfolio.

Following the advice of Andy Sterkowitz, my simple project would use the basic Python library; use less than 200 lines of code; use the CLI as opposed to GUI or WebApp.

## What does it do?

Using the CLI, the user can navigate between the Main, Modification and Metric Menus. The Main menu allows users to print their total expenses in something approximating a tabular format (more on this later), exit the program and navigate to the other two menus. The Modification menu allows for the adding, deletion, changing of expense detail and return to the parent menu. The Metric menu gives information about total expenses, how much paid to a given payee and what proportion of total expenses this is, payments over a given amount. Each expense ID is unique, so they can be accessed for modification and deletion.

 The user can also load or save the 'table' array where expenses are stored using the Python library's os module. Making use of the Object-Oriented Programming (OOP) paradigm, as opposed to say procedural code, the program allows efficient creation and use of interactive menus and the methods accessed through them. 

## What doesn't it do?

By definition, the scope of a simple project is limited. The printed table of all expenses is ugly, columns don't line-up. I could have used tkinter or tableau to resolve this. Aforementioned, my simple projects will use only the basic Python library. No unit-testing was performed, so amongst other things incorrect values could be passed such as string for the Sum. If this was a larger project I would make use of both.