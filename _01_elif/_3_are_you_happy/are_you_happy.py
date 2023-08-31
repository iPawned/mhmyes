from tkinter import Tk, simpledialog, messagebox


if __name__ == '__main__':
    window = Tk()
    window.withdraw()
    answer2 = ''
    answer1 = simpledialog.askstring(title='Question 1:', prompt='Are you happy?')
    if answer1 == 'Yes':
        messagebox.showinfo(title='Answer 1', message='Keep doing what you are doing.')
    elif answer1 == 'No':
        answer2 = simpledialog.askstring(title='Question 2', prompt='Do you want to be happy?')
        if answer2 == 'Yes':
            messagebox.showinfo(title='Answer 2', message='Change something.')
        elif answer2 == 'No':
            messagebox.showinfo(title='Answer 3', message='Keep doing what you are doing.')
    # TODO: Look at the AreYouHappy.png image
    #       Use pop-ups to recreate the chart using if and elif statements

    pass
