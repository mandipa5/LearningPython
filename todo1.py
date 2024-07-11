total_todo = int(input("Enter number of todos: "))
todos = []
for i in range(0,total_todo):
  todo = input(f"Enter todo {i+1}: ")
  todos.append(todo)
for todo in todos:
  print(todo)