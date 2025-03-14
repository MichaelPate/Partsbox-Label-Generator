# Use python virtual environment:
# partsbox_labelgen_env
# partsbox_labelgen_env\Scripts\activate

import tkinter as tk
from tkinter import filedialog
import webbrowser
import os

class HTMLEditor:
    def __init__(self, root):
        self.root = root
        self.root.title("HTML Editor")

        # Create the text widget for editing HTML
        self.text = tk.Text(self.root, wrap="word", width=80, height=20)
        self.text.pack(padx=10, pady=10)

        # Create buttons
        self.save_button = tk.Button(self.root, text="Save", command=self.save_file)
        self.save_button.pack(side="left", padx=10, pady=10)

        self.preview_button = tk.Button(self.root, text="Preview", command=self.preview_file)
        self.preview_button.pack(side="left", padx=10, pady=10)

        self.print_button = tk.Button(self.root, text="Print", command=self.print_file)
        self.print_button.pack(side="left", padx=10, pady=10)

        self.load_file()  # Load the file if it exists

    def load_file(self):
        """Prompt the user to load an existing HTML file."""
        file_path = filedialog.askopenfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html"), ("All Files", "*.*")])
        if file_path:
            with open(file_path, "r") as file:
                self.text.delete(1.0, tk.END)  # Clear current content
                self.text.insert(tk.END, file.read())  # Load file content into the text widget
            self.current_file = file_path  # Store the current file path

    def save_file(self):
        """Save the current content to a file."""
        if not hasattr(self, "current_file") or not self.current_file:
            # Ask the user for the filename if it's a new file
            self.current_file = filedialog.asksaveasfilename(defaultextension=".html", filetypes=[("HTML Files", "*.html"), ("All Files", "*.*")])

        if self.current_file:
            with open(self.current_file, "w") as file:
                file.write(self.text.get(1.0, tk.END))  # Write the content to the file
            print(f"File saved to {self.current_file}")

    def preview_file(self):
        """Open the HTML file in a browser for preview."""
        if hasattr(self, "current_file") and self.current_file:
            webbrowser.open(f"file:///{self.current_file}")
        else:
            print("No file loaded or saved yet.")

    def print_file(self):
        """Print the HTML file."""
        if hasattr(self, "current_file") and self.current_file:
            # This will try to print the HTML file using the default printing service on your system.
            # For Windows, it will use the default system printing method.
            if os.name == "nt":  # For Windows
                os.startfile(self.current_file, "print")
            else:  # For macOS or Linux (requires the user to have lp or another printing command)
                os.system(f"lp {self.current_file}")
            print(f"Printing {self.current_file}")
        else:
            print("No file loaded or saved yet.")

if __name__ == "__main__":
    root = tk.Tk()
    editor = HTMLEditor(root)
    root.mainloop()
