import time
import random
import tkinter as tk
from tkinter import messagebox

class TypingTest:
    def __init__(self, master):
        self.master = master
        self.master.title("Typing Test")
        
        self.text = ""
        self.generated_text = ""
        self.start_time = 0
        self.end_time = 0

        self.setup_ui()
        self.generate_text()
        self.timer_running = False

    def setup_ui(self):
        self.paned_window = tk.PanedWindow(self.master, orient=tk.HORIZONTAL)
        self.paned_window.pack(expand=True, fill=tk.BOTH)

        self.text_frame = tk.Frame(self.paned_window)
        self.text_frame.pack(expand=True, fill=tk.BOTH)
        self.text_frame.grid_rowconfigure(0, weight=1)
        self.text_frame.grid_columnconfigure(0, weight=1)

        self.paragraph_label = tk.Label(self.text_frame, text="Paragraph:")
        self.paragraph_label.grid(row=0, column=0, sticky="w")

        self.paragraph_text = tk.Text(self.text_frame, wrap=tk.WORD, height=10)
        self.paragraph_text.grid(row=1, column=0, sticky="nsew")

        self.paned_window.add(self.text_frame)

        self.text_area_frame = tk.Frame(self.paned_window)
        self.text_area_frame.pack(expand=True, fill=tk.BOTH)
        self.text_area_frame.grid_rowconfigure(0, weight=1)
        self.text_area_frame.grid_columnconfigure(0, weight=1)

        self.text_area_label = tk.Label(self.text_area_frame, text="Type here:")
        self.text_area_label.grid(row=0, column=0, sticky="w")

        self.text_box = tk.Text(self.text_area_frame, wrap=tk.WORD, height=10)
        self.text_box.grid(row=1, column=0, sticky="nsew")
        self.text_box.bind("<Return>", self.subtract_line_count)

        self.paned_window.add(self.text_area_frame)

        self.start_button = tk.Button(self.master, text="Start", command=self.start_typing_test)
        self.start_button.pack()

        self.stop_button = tk.Button(self.master, text="Stop", command=self.stop_typing_test, state="disabled")
        self.stop_button.pack()

        self.start_time_label = tk.Label(self.master, text="Start Time: -")
        self.start_time_label.pack()

        self.timer_label = tk.Label(self.master, text="Timer: 0.00 seconds")
        self.timer_label.pack()

        self.line_count_label = tk.Label(self.master, text="")
        self.line_count_label.pack()

    def generate_text(self):
        words = ["The", "quick", "brown", "fox", "jumps", "over", "the", "lazy", "dog."]
        random.shuffle(words)
        self.generated_text = " ".join(words)

    def start_typing_test(self):
        self.text = self.generated_text
        self.start_time = time.time()

        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")

        self.paragraph_text.delete(1.0, tk.END)
        self.paragraph_text.insert(tk.END, self.generated_text)

        self.text_box.delete(1.0, tk.END)

        self.start_time_label.config(text=f"Start Time: {time.strftime('%H:%M:%S')}")

        self.timer_running = True
        self.update_timer()

        self.line_count_label.config(text=f"Lines to type: {len(self.generated_text.splitlines())}")

    def stop_typing_test(self):
        self.end_time = time.time()
        elapsed_time = self.end_time - self.start_time

        typed_text = self.text_box.get(1.0, tk.END).strip()
        typed_lines = len(typed_text.split('\n'))

        if typed_text == self.text:
            messagebox.showinfo("Congratulations!", f"You typed it correctly in {elapsed_time:.2f} seconds.")
        else:
            messagebox.showerror("Oops!", f"Looks like there was a mistake. You typed {typed_lines} lines, but {len(self.generated_text.splitlines())} were required.")

        self.start_button.config(state="normal")
        self.stop_button.config(state="disabled")
        self.generate_text()
        self.text_box.delete(1.0, tk.END)

        self.timer_running = False

    def update_timer(self):
        if self.timer_running:
            elapsed_time = time.time() - self.start_time
            self.timer_label.config(text=f"Timer: {elapsed_time:.2f} seconds")
            self.master.after(100, self.update_timer)

    def subtract_line_count(self, event):
        self.line_count_label.config(text=f"Lines to type: {len(self.generated_text.splitlines()) - 1}")

def main():
    root = tk.Tk()
    typing_test_app = TypingTest(root)
    root.mainloop()

if __name__ == "__main__":
    main()
