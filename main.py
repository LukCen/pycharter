import matplotlib.pyplot as mpl
import tkinter
import tkinter.ttk as ttk

# class for creating the top frame for data inputs

class DataRow():
  def __init__(self, master,  frame_col, frame_row):
    

    self.master = master
    self.frame_col= frame_col
    self.frame_row = frame_row

    # ogranizational container
    self.frame = ttk.Frame(master)


    # labels for inputs plus inputs

    self.new_label_x = ttk.Label(self.frame, text="X axis (string)")
    self.new_label_x.configure(padding=10)

    self.new_label_y = ttk.Label(self.frame, text="Y axis (number)")
    self.new_label_y.configure(padding=10)

    self.new_entry_x = ttk.Entry(self.frame, width=60)
    self.new_entry_y = ttk.Entry(self.frame, width=60)

    # add to list button

    self.new_button = ttk.Button(self.frame, text="Add to list", command=self.add_to_list)

    self.new_entry_x.grid(row=0, column=1, sticky='ew')
    self.new_entry_y.grid(row=1, column=1, sticky='ew')

    self.new_label_x.grid(row=0, column=0)
    self.new_label_y.grid(row=1, column=0)

    self.new_button.grid(row=0, column=2, sticky='nse')

    self.new_button.rowconfigure(0, weight=2)

    self.new_entry_x.columnconfigure(1, weight=1)

    self.frame.grid(row=self.frame_row, column=self.frame_col, padx=20, pady=5, sticky='ew')
    
  def add_to_list(self):
    text_x = self.new_entry_x.get()
    text_y = self.new_entry_y.get()
    if text_x and text_y:
      # text_list.insert('', 'end',None, text=f'{text_x } : { text_y}')
      items.update({text_x: text_y})

      list_item_frame = ttk.Frame(self.frame)

      list_item_key = ttk.Label(list_item_frame, text=text_x)
      list_item_value = ttk.Label(list_item_frame, text=text_y)

      list_item_key.pack(anchor="w")
      list_item_value.pack(anchor="e")
      list_item_frame.grid(row=2,column=0, sticky='ew')
      list_item_frame.rowconfigure(2, weight=2)

        
# key/value pairs to use for the chart making
items = {}

def plotLineChart(title = "My Chart"):
    
    sorted_items = sorted(items.items(), key=lambda x: int(x[1]))
    names = [item[0] for item in sorted_items]
    values = [int(item[1]) for item in sorted_items]


    mpl.bar(names, values)
    mpl.title(title)
    mpl.show()


root = tkinter.Tk()
root.configure(bg="#999999")

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=0)
root.rowconfigure(1, weight=1)

root.minsize(800,600)
root.title("PyCharter")

# frame containing the inputs
frame1 = ttk.Frame(root)
frame1.grid(row=0,column=0,sticky="nsew")
frame1.columnconfigure(0, weight=1)

# textlist - displays added k/v pairs
# text_list = ttk.Treeview(root)
# text_list.grid(rows=1,column=0,sticky='nsew')


chart_button = tkinter.Button(root,text="Chart", command=plotLineChart, background="#333333", foreground="#f5f5f5", font="25", padx=20, pady=10)
chart_button.grid(row=3, columnspan=3, sticky='nsew')
x_row = DataRow(frame1,0,0)


root.mainloop()

