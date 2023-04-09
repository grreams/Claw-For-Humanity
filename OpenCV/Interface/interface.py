import tkinter as tk

def interface():
    window = tk.Tk()
    window.title("Project Claw For Humanity Port Selector")
    window.geometry("600x240")
    window.resizable(True,True)
    ComLable = tk.Label(window, text='Enter com port', font=('Arial', 15))
    ComLable.place(x=30,y=20)
    ComEnt = tk.Entry(window)
    ComEnt.place(x= 30, y= 45)
    
    CamPortLabel = tk.Label(window, text='Enter Camera Port // Default is 0', font=('Arial',15))
    CamPortLabel.place(x=30, y=80)
    btn = tk.Button(window, text='Next')
    btn.config(command=__startPort__(ComEnt))
    
    btn.place(x= 30, y= 100)
    window.mainloop()
    
def colourInterface():
    ColourWindow = tk.Tk()
    ColourWindow.title("Project Claw For Humanity Main")
    ColourWindow.geometry("1000x800")
    ColourWindow.resizable(True,True)
    # colours and buttons
    redBtn = tk.Button(ColourWindow, text='red')
    redBtn.place(x= 100, y= 100)
    bluBtn = tk.Button(ColourWindow, text='blue')
    bluBtn.place(x= 200, y= 100)
    yelBtn = tk.Button(ColourWindow, text = 'green')
    yelBtn.place()
    
    
def __startPort__(what):
    print(str(what))
    
    
interface()