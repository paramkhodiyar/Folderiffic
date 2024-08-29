import os
import shutil
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def sort_files():
    downloads_path = os.path.expanduser("/Users/paramkhodiyar/Downloads")
    destination_path = filedialog.askdirectory(title="Select destination folder")
    if not destination_path:
        status_label.config(text="Destination folder not selected. Aborting.")
        return
    
    keyword = keyword_entry.get().strip()
    if not keyword:
        status_label.config(text="Please enter a keyword.")
        return
    
    
    files = os.listdir(downloads_path)
    
    
    matching_files = [f for f in files if keyword.lower() in f.lower()]
    
    
    progress['maximum'] = len(matching_files)
    
    moved_count = 0
    skipped_count = 0
    for i, file in enumerate(matching_files):
        source = os.path.join(downloads_path, file)
        destination = os.path.join(destination_path, file)
        
        
        if not os.path.exists(destination):
            shutil.move(source, destination)
            moved_count += 1
        else:
            skipped_count += 1
        
        
        progress['value'] = i + 1
        status_label.config(text=f"Processing: {file}")
        root.update_idletasks()
    
    
    status_label.config(text=f"Done! Moved {moved_count} files, Skipped {skipped_count} files.")


root = tk.Tk()
root.title("File Sorter")
root.geometry("400x200")


keyword_label = ttk.Label(root, text="Enter keyword:")
keyword_label.pack(pady=(10, 0))
keyword_entry = ttk.Entry(root, width=30)
keyword_entry.pack(pady=(0, 10))


sort_button = ttk.Button(root, text="Choose the destination Folder", command=sort_files)
sort_button.pack(pady=10)


progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
progress.pack(pady=10)


status_label = ttk.Label(root, text="Enter a keyword and click 'Sort Files' to begin")
status_label.pack(pady=10)


root.mainloop()


   
    
