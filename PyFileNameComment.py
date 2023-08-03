import tkinter as tk
from tkinter import filedialog
import os

def add_file_name_to_files(directory_path, output_text):
    if not os.path.isdir(directory_path):
        output_text.set("指定されたディレクトリが存在しません。")
        return

    for filename in os.listdir(directory_path):
        if filename.endswith(".py"):
            file_path = os.path.join(directory_path, filename)
            with open(file_path, "r+", encoding="utf-8") as file:
                lines = file.readlines()
                first_line = lines[0].strip() if len(lines) > 0 else ""
                if not first_line.startswith("#") or f"# {filename}" not in first_line:
                    file.seek(0, 0)
                    file.write(f"# {filename}\n")
                    file.write("".join(lines))
                file.close()

    output_text.set("ファイル名をファイルに追加しました。")

def browse_directory(output_text):
    directory_path = filedialog.askdirectory()
    selected_directory.set(directory_path)
    output_text.set("")

def execute_add_file_name(output_text):
    directory_path = selected_directory.get()
    if directory_path:
        add_file_name_to_files(directory_path, output_text)

app = tk.Tk()
app.title("Pythonファイル名をファイルに追加")

output_text = tk.StringVar()
output_label = tk.Label(app, textvariable=output_text)
output_label.pack(pady=10)

browse_button = tk.Button(app, text="ディレクトリを選択", command=lambda: browse_directory(output_text))
browse_button.pack(pady=5)

execute_button = tk.Button(app, text="実行", command=lambda: execute_add_file_name(output_text))
execute_button.pack(pady=5)

selected_directory = tk.StringVar()
selected_directory_entry = tk.Entry(app, textvariable=selected_directory, width=50)
selected_directory_entry.pack(pady=5)

app.mainloop()
