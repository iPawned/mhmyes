from tkinter import simpledialog, messagebox, Tk

# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
quest1 = simpledialog.askstring(title="Question 1:", prompt="Do you want to go on an adventure?")
if quest1 == "No":
    messagebox.showinfo(title="Well then,")