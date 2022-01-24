# Information

Remember that this is just some project I worked on for a while, and it is no longer maintained. Feel free to edit the code, but if you distribute it publicly it'd be nice to reference me as the original creator. I haven't worked much with tkinter before, so the code is messy, but still mostly works. If there's an issue, feel free to report it, but I most likely won't have time to fix it.

## Terminal
The Terminal version should work on any OS, with the module [Colorama](https://pypi.org/project/colorama/) installed via `pip install colorama`.
You can run it with  `python [terminal_analyzer.py file location]`

## GUI
The GUI is MacOS tested only. You can run it by following the steps below:
- `cd [GUI Analyzer folder location]`
- `python3 main.py` (requires tkinter & Python 3 to run)
    - You can install tkinter for python using `brew install python-tk` if necessary
OR if you would like to use the MacOS application in the Releases section, you can just double click that and it will do the work for you

## Themes
When using the GUI version of this Data Analyzer, you can create your own themes. However, this feature has not been implemented yet, so you have to do it yourself. Below are steps on how to create your own themes.
- **WARNING:** *You could break the app if you do not know how to work with JSON files*
- **COLORS:** *You can find the tkinter color chart [here](http://tephra.smith.edu/dftwiki/images/3/3d/TkInterColorCharts.png)* 

- In the file named `data.json`, there is a section named `"themes"`. This is where you will be adding your themes.
    - Sidenote: if you are using the MacOS application, you have to right click it and press "Show Package Contents" and head to `/Contents/Resources/data.json` to find it.
- When creating a new theme, there are 4 things that you need.
    1. You need a name for the theme.
    2. You need `"function colors"`, the colors for the names of each functions (Range, Mean, etc)
    3. You need `"output colors"`, the colors for the output colors. These can be the same or different as `"function colors"`
    4. You need `"return"`, this one is a bit more complicated. This is for when you'd like to have spacing between lines, 1 and 0 only, otherwise the app will glitch.
- You can always use previous themes to get an idea of how it works

## Undeveloped Updates
- Ability to make your own themes using the app
- Cleaner code
