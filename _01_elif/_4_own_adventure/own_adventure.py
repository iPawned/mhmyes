from tkinter import simpledialog, messagebox, Tk
if __name__ == '__main__':
    window = Tk()
    window.withdraw()
# TODO Tell the user a story, but give them options so they can decide the
#  path of the plot.
#  Use pop-ups, if statements, and your imagination to make an interesting
#  story
    quest1 = simpledialog.askstring(title="Question 1:", prompt="Do you want to go on an adventure?")
    if quest1 == "No":
        messagebox.showinfo(title="Failed", message="Well then, I will be on my way")
    elif quest1 == "Yes":
        messagebox.showinfo(title="Passed", message="Well then, let's go!")
        messagebox.showinfo(title="River", message="Oh no, there is a river in the middle of the trail!")
        quest2 = simpledialog.askstring(title="Question 2:", prompt="Type Bridge or Swim")
        if quest2 == "Swim":
            messagebox.showinfo(title="Failed", message="Everything seems to be fine, until you realise that you swum into a lake of piranahs!")
        if quest2 == "Bridge":
            messagebox.showinfo(title="Passed", message="You walk on the stable wooden bridge and get to the other side.")
            messagebox.showinfo(title="Pond", message="You see a big pond to refill your water with")
            quest3 = simpledialog.askstring(title="Question 3:", prompt="Type Refill to refill your water or type Ignore to walk past it")
            if quest3 == "Refill":
                messagebox.showinfo(title="Failed", message="You take a sip of your water. Within a few minutes, you start to feel sick, and collapse on the ground.")
            elif quest3 == "Ignore":
                messagebox.showinfo(title="Passed", message="A man walks up to you and asks you if you drank water from the pond. You tell him no, and he sighs with relief and tells you that a large amount of deadly chemicals fell into the water!")
                messagebox.showinfo(title="Bandits", message="You see a group of bandits hoping for a easy score.")
                quest4 = simpledialog.askstring(title="Question 4", prompt="Type Fight to fight the bandits or Run to run away")
                if quest3 == "Run":
                    messagebox.showinfo(title="Failed", message="You try running as fast as you can the other way, but get cornered by even more bandits. It was a trap!")
                elif quest4 == "Fight":
                    messagebox.showinfo(title="Passed", message="As you start to pull out your weapons, the bandits run away. They must have thought that you were unarmed!")
                    messagebox.showinfo(title="Winner!", message="You contine to walk down the path when you see a golden chest, you open it, and are almost blinded by the golden light...")
