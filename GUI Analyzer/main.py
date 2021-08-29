#!usr/bin/env python

from Foundation import NSUserDefaults, NSURL
from AppKit import NSWorkspace
from functions import *
import tkinter.messagebox as msg
import tkinter as tk
from copy import deepcopy

root = tk.Tk()
root.title('Data Analyzer')
root.geometry('570x497')
root.resizable(False, False)
root.iconphoto(False, tk.PhotoImage(file = "icon.png"))

def themeList():
    with open("data.json", "r") as data_file:
        themes = deepcopy(json.load(data_file)["themes"])
        theme_list = []
        for i in themes:
            theme_list.append(i)
    return theme_list
theme_list = themeList()
is_help = False

def example():
    entry_input.delete("0", tk.END)
    entry_input.insert(tk.END, '10 17,34, 19, 98 01 3.55, 9,9.0, 88.12, 1394224, 1938 48.0112 asd .;, []')
    analize_data()
    text_output.insert('1.0', """You can split your input with either spaces, commas, or both as you prefer. Negative,
positive, and decimal numbers are accepted, and any NaNs (Not a Number) will be
removed before the calculations and listed for you if needed, and you can always put
more than the size of the input box. You can also edit colored themes for the output by
pressing the \"Themes\" button. You can switch themes with the drop-down menu.
\nHere's an example with the above input:\n\n""")
    text_output.tag_add("Example", "1.0", "9.0")
    text_output.tag_config("Example", font=('Helvetica', 14))
    global is_help
    is_help = True

def analize_data(event=None):
    nums = organiseList(" ".join(entry_input.get().split(",")).split())
    if len(nums[0])<2:
        MsgBox = msg.askquestion("Error", 'You need at least two numbers, would you like to see an example?', icon='warning')
        if MsgBox == 'yes':
            example()
    else:
        text_output.delete('1.0', tk.END)
        outputs = allOutputs(nums[0], nums[1])
        for i in range(1, 13):
            if i == 1: o = i
            elif i == 2: o = i + outputs[1]
            elif i == 3: o = i + outputs[1] + outputs[2]
            elif i < 7: o = i + outputs[1] + outputs[2]
            elif i < 11: o = i + outputs[1] + outputs[2]
            elif i == 11: o = i + outputs[1] + outputs[2]
            elif i == 12: o = i + outputs[1] + outputs[2]
            new_lines[i-1]+=float(o)
        o = 0
        for i in range(0, 12):
            if current_theme["theme data"]["return"][i]==1:
                o += 1
            new_lines[i]+=float(o)
        
        # Debugging
        # print(new_lines)  
        
        for i in range(0, 12):
            if i>0 and i<12:
                if current_theme["theme data"]["return"][i]==1:
                    text_output.insert(tk.END, '\n\n')
                else:
                    text_output.insert(tk.END, '\n')
            text_output.insert(tk.END, f'{function_names[i]}: {outputs[0][i]}')
            text_output.tag_add(f"{i}", f"{new_lines[i]}", correctSpacing(new_lines[i], len(function_names[i])))
            text_output.tag_config(f"{i}", foreground=f"{current_theme['theme data']['function colors'][i]}", font=('Menlo', 14, 'bold'))
            text_output.tag_add(f"{-1-i}", correctSpacing(new_lines[i], len(function_names[i])), tk.END)
            text_output.tag_config(f"{-1-i}", foreground=f"{current_theme['theme data']['output colors'][i]}", font=('Menlo', 14, 'normal'))
        for i in range(0, 12): new_lines[i]=0
        global is_help
        is_help = False

label_title = tk.Label(
    master=root,
    text="Press help for an example",
    font=('Helvetica', 14, "bold"),
    height=2
)
label_title.place(x=200, y=35)

label_data = tk.Label(
    master=root,
    text='Data:',
    font=('Helvetica', 14, 'normal')
)
label_data.place(x=8, y=72)

entry_input = tk.Entry(
    master=root,
    width=50
)
entry_input.bind('<Return>', analize_data)
entry_input.bind('<KP_Enter>', analize_data)
entry_input.place(x=47, y=70)

button_ok = tk.Button(
    master=root,
    text='Go',
    command=analize_data,
    font=('Helvetica', 14, 'normal')
)
button_ok.place(x=507.5, y=68)

text_output = tk.Text(
    master=root,
    font=('Menlo', 14, 'bold'),
    width=69
)
text_output.place(x=4.5, y=100)

def close():
    MsgBox = msg.askquestion("Error", 'Are you sure you want to close the app?', icon='warning')
    if MsgBox == 'yes':
        root.destroy()

button_exit = tk.Button(
    master=root,
    text=' Exit ',
    command=close,
    font=('Helvetica', 14, "normal")
)
button_exit.place(x=494.5, y=3)

button_example = tk.Button(
    master=root,
    text='Help',
    command=example,
    font=('Helvetica', 14, "normal")
)
button_example.place(x=497, y=35)

def changeTheme(choice, custom_choice=None):
    global current_theme
    global is_help
    if custom_choice==True:
        choice = choice
    else:
        choice = theme_drop_var.get()
        if choice == 'Dark Mode' and NSUserDefaults.standardUserDefaults().stringForKey_('AppleInterfaceStyle') !='Dark':
            MsgBox = msg.askquestion("Warning", 'The Dark Mode theme may be illegible when your computer is on light mode. Would you like to open System Preferences and change the Appearance of your computer?', icon="warning")
            if MsgBox == 'yes':
                workspace = NSWorkspace.sharedWorkspace()
                workspace.openURL_(NSURL.URLWithString_('x-apple.systempreferences::com.apple.preference.general'))
            else:
                pass
        elif choice == 'Light Mode' and NSUserDefaults.standardUserDefaults().stringForKey_('AppleInterfaceStyle') =='Dark':
            MsgBox = msg.askquestion("Warning", 'The Light Mode theme may be illegible when your computer is on dark mode. Would you like to open System Preferences and change the Appearance of your computer?', icon="warning")
            if MsgBox == 'yes':
                workspace = NSWorkspace.sharedWorkspace()
                workspace.openURL_(NSURL.URLWithString_('x-apple.systempreferences::com.apple.preference.general'))
            else:
                pass
    #################################################
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
    #################################################
    data["theme"] = choice
    #################################################
    with open("data.json", "w") as data_file:
        json.dump(data, data_file, indent=4)
    #################################################
    current_theme = currentTheme()
    if len(organiseList(" ".join(entry_input.get().split(",")).split())[0])>=2 and is_help==False:
        analize_data()
    elif is_help==True:
        example()

def currentTheme():
    with open("data.json", "r") as data_file:
        data = json.load(data_file)
        currenttheme = {"theme name": data["theme"], "theme data": data["themes"][data["theme"]]}
    return currenttheme
current_theme = currentTheme()

if current_theme["theme name"] == 'Dark Mode' and NSUserDefaults.standardUserDefaults().stringForKey_('AppleInterfaceStyle') !='Dark':
    changeTheme('Light Mode', True)
elif current_theme["theme name"] == 'Light Mode' and NSUserDefaults.standardUserDefaults().stringForKey_('AppleInterfaceStyle') =='Dark':
    changeTheme('Dark Mode', True)

theme_drop_var = tk.StringVar()
theme_drop_var.set(current_theme["theme name"])
theme_dropdown = tk.OptionMenu(
    root,
    theme_drop_var,
    *theme_list,
    command=changeTheme
)
theme_dropdown.place(x=8, y=35)

def switchThemeButton(editing):
    if editing == True:
        label_title.place_forget()
        label_data.place_forget()
        entry_input.place_forget()
        button_ok.place_forget()
        text_output.place_forget()
        button_exit.place_forget()
        button_example.place_forget()
        button_edit_theme.place_forget()

        theme_dropdown.place(x=263, y=7)
        
        button_go_back.place(x=5, y=3)
        button_update_theme_list.place(x=100, y=3)
        msg.showinfo("Information", """This feature has not been implemented yet, since I've been busy with other stuff.

You can check out the readMe.md to create your own themes manually.""")

    elif editing == False:
        label_title.place(x=200, y=35)
        label_data.place(x=8, y=72)
        entry_input.place(x=47, y=70)
        button_ok.place(x=507.5, y=68)
        text_output.place(x=4.5, y=100)
        button_exit.place(x=494.5, y=3)
        button_example.place(x=497, y=35)
        button_edit_theme.place(x=5, y=3)

        theme_dropdown.place(x=8, y=35)
        
        button_go_back.place_forget()
        button_update_theme_list.place_forget()
        
        

def editThemes():
    pass



button_edit_theme = tk.Button(
    master=root,
    text='Themes',
    command=lambda: [switchThemeButton(True), editThemes()],
    font=('Helvetica', 14, "normal")
)
button_edit_theme.place(x=5, y=3)

button_go_back = tk.Button(
    master=root,
    text='Go Back',
    command=lambda: switchThemeButton(False),
    font=('Helvetica', 14, "normal")
)
#need to config theme list
def updateThemeList():
    global theme_list
    global theme_drop_var
    global theme_dropdown
    theme_list = themeList()
    theme_drop_var = tk.StringVar()
    theme_drop_var.set(current_theme["theme name"])
    theme_dropdown.destroy()
    theme_dropdown = tk.OptionMenu(
        root,
        theme_drop_var,
        *theme_list,
        command=changeTheme
        )
    theme_dropdown.place(x=263, y=7)

button_update_theme_list = tk.Button(
    master=root,
    text='Update Theme List',
    command=updateThemeList,
    font=('Helvetica', 14, "normal")
)

root.mainloop()