import os
import shutil
import datetime
from tkinter import *
from tkinter import ttk, messagebox, filedialog

class Filemover:

    def __init__(self, master):
        
        master.title('File Transfer UI')
        master.resizable(False, False)
        master.configure(background = '#FFFFFF')
        
        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#FFFFFF')
        self.style.configure('TButton', background = '#FFFFFF')
        self.style.configure('TLabel', background = '#FFFFFF', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))      

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()
        
        self.logo = PhotoImage(file = 'filetransfer.png').subsample(2)
        ttk.Label(self.frame_header, image = self.logo).grid(row = 0, column = 0, rowspan = 2)
        ttk.Label(self.frame_header, text = 'Let\'s Transfer Files!', style = 'Header.TLabel').grid(row = 0, column = 1)
        ttk.Label(self.frame_header, wraplength = 300,
                  text = ("Please choose the directory you would like to scan and "
                          "the destination folder. Any files modified in the last "
                          "24 hours will be moved to the new folder.")).grid(row = 1, column = 1)
        
        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

                
        self.source_button = ttk.Button(self.frame_content, text = 'Choose Source', command = self.browseSource)
        self.destination_button = ttk.Button(self.frame_content, text = 'Choose Destination', command = self.browseDestination)

        self.source_entry = ttk.Entry(self.frame_content, width = 40, font = ('Arial', 10))
        self.destination_entry = ttk.Entry(self.frame_content, width = 40, font = ('Arial', 10))
        
        self.source_button.grid(row = 1, column = 0, padx = 5)
        self.destination_button.grid(row = 1, column = 1, padx = 5)
        
        submit = ttk.Button(self.frame_content, text = 'Submit',
                   command = self.submit)

        submit.grid(row = 3, column = 0, padx = 5, pady = 5, columnspan =2)

    def browseSource(self):
        source = filedialog.askdirectory()
        self.source_entry.grid(row = 2, column = 0, padx = 5)
        self.source_entry.insert(0,source)
        return source
        
    def browseDestination(self):
        destination = filedialog.askdirectory()
        self.destination_entry.grid(row = 2, column = 1, padx = 5)
        self.destination_entry.insert(0,destination)
        return destination
        
    def submit(self):
        source = (self.source_entry.get() + "\\")
        destination = (self.destination_entry.get() + "\\")
        print(source)
        print(destination)
        now = datetime.datetime.now()
        last24 = now-datetime.timedelta(hours=24)

        for filename in os.listdir(source):
            stats = os.stat(source+filename)
            lastMod = datetime.datetime.fromtimestamp(stats[8])
            if(lastMod >= last24):
                print(lastMod)
                shutil.move( source + filename, destination)
                print(destination + filename)
        messagebox.showinfo(title = 'File Transfer Complete', message = 'Your files have been transferred.')

def main():            
    
    root = Tk()
    filemover = Filemover(root)
    root.mainloop()
    
if __name__ == "__main__": main()
