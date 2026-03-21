class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
        print("Task added successfully!")

    def remove_task(self, task):
        for t in self.tasks:
            if t["task"] == task:
                self.tasks.remove(t)
                print("Task removed successfully!")
                return
        print("Task not found in the list.")

    def mark_completed(self, task):
        for t in self.tasks:
            if t["task"] == task:
                t["completed"] = True
                print("Task marked as completed!")
                return
        print("Task not found in the list.")

    def display_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, t in enumerate(self.tasks, start=1):
                status = "Completed" if t["completed"] else "Not Completed"
                print(f"{i}. {t['task']} - {status}")
        else:
            print("No tasks in the list.")

    def save_to_file(self, filename="tasks.txt"):
        with open(filename, "w") as file:
            for t in self.tasks:
                file.write(f"{t['task']}|{t['completed']}\n")
        print("Tasks saved to file!")

    def load_from_file(self, filename="tasks.txt"):
        try:
            with open(filename, "r") as file:
                for line in file:
                    task, completed = line.strip().split("|")
                    self.tasks.append({
                        "task": task,
                        "completed": completed == "True"
                    })
            print("Tasks loaded from file!")
        except FileNotFoundError:
            print("No saved task file found.")


def main():
    todo_list = TodoList()
    todo_list.load_from_file()   # Load tasks when program starts

    while True:
        print("\nTODO LIST MENU:")
        print("1. Add a task")
        print("2. Remove a task")
        print("3. Mark a task as completed")
        print("4. Display tasks")
        print("5. Save tasks")
        print("6. Exit")

        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            task = input("Enter task to add: ")
            todo_list.add_task(task)

        elif choice == '2':
            task = input("Enter task to remove: ")
            todo_list.remove_task(task)

        elif choice == '3':
            task = input("Enter task to mark as completed: ")
            todo_list.mark_completed(task)

        elif choice == '4':
            todo_list.display_tasks()

        elif choice == '5':
            todo_list.save_to_file()

        elif choice == '6':
            todo_list.save_to_file()  # Save before exiting
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

main()






#ToDOList Project ----------> enhanced with AI



# import tkinter as tk
# from tkinter import messagebox

# class TodoList:
#     def __init__(self):
#         self.tasks = []

#     def add_task(self, task):
#         self.tasks.append({"task": task, "completed": False})

#     def remove_task(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks.pop(index)

#     def mark_completed(self, index):
#         if 0 <= index < len(self.tasks):
#             self.tasks[index]["completed"] = True

#     def save_to_file(self, filename="tasks.txt"):
#         with open(filename, "w") as file:
#             for t in self.tasks:
#                 file.write(f"{t['task']}|{t['completed']}\n")

#     def load_from_file(self, filename="tasks.txt"):
#         try:
#             with open(filename, "r") as file:
#                 for line in file:
#                     task, completed = line.strip().split("|")
#                     self.tasks.append({
#                         "task": task,
#                         "completed": completed == "True"
#                     })
#         except FileNotFoundError:
#             pass


# class TodoGUI:
#     def __init__(self, root):
#         self.todo = TodoList()
#         self.todo.load_from_file()

#         self.root = root
#         self.root.title("Todo List App")
#         self.root.geometry("400x400")

#         self.task_entry = tk.Entry(root, width=30)
#         self.task_entry.pack(pady=10)

#         self.add_button = tk.Button(root, text="Add Task", command=self.add_task)
#         self.add_button.pack()

#         self.listbox = tk.Listbox(root, width=50)
#         self.listbox.pack(pady=10)

#         self.complete_button = tk.Button(root, text="Mark Completed", command=self.complete_task)
#         self.complete_button.pack(pady=2)

#         self.remove_button = tk.Button(root, text="Remove Task", command=self.remove_task)
#         self.remove_button.pack(pady=2)

#         self.save_button = tk.Button(root, text="Save Tasks", command=self.save_tasks)
#         self.save_button.pack(pady=2)

#         self.refresh_list()

#     def refresh_list(self):
#         self.listbox.delete(0, tk.END)
#         for task in self.todo.tasks:
#             status = "✔" if task["completed"] else "✘"
#             self.listbox.insert(tk.END, f"{task['task']} [{status}]")

#     def add_task(self):
#         task = self.task_entry.get()
#         if task:
#             self.todo.add_task(task)
#             self.task_entry.delete(0, tk.END)
#             self.refresh_list()
#         else:
#             messagebox.showwarning("Warning", "Enter a task")

#     def remove_task(self):
#         try:
#             index = self.listbox.curselection()[0]
#             self.todo.remove_task(index)
#             self.refresh_list()
#         except:
#             messagebox.showwarning("Warning", "Select a task")

#     def complete_task(self):
#         try:
#             index = self.listbox.curselection()[0]
#             self.todo.mark_completed(index)
#             self.refresh_list()
#         except:
#             messagebox.showwarning("Warning", "Select a task")

#     def save_tasks(self):
#         self.todo.save_to_file()
#         messagebox.showinfo("Saved", "Tasks saved successfully")


# root = tk.Tk()
# app = TodoGUI(root)
# root.mainloop()