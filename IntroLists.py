# In-class exercise to show how to create and use a list.

ToDo = ["Study, study and study some more."]
print(ToDo)
print(ToDo[1])

TaskNum = 1
for Task in ToDo:
    print(f" {TaskNum}. {Task}")
    TaskNum += 1

NewTask = input("Enter a new task: ")
ToDo.append(NewTask)
TaskNum = 1
for Task in ToDo:
    print(f" {TaskNum}. {Task}")
    TaskNum += 1
print()

DelItem = int(input("What item do you want to delete: "))
ToDo.__delitem__(DelItem - 1)
if len(ToDo) != 0:
    TaskNum = 1
    for Task in ToDo:
        print(f" {TaskNum}. {Task}")
        TaskNum += 1
else:
    print("ToDo list is currently empty.")

