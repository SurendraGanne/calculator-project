import tkinter as tk
from tkinter import scrolledtext
import math
from history_manager import load_history, add_entry  # ← history import

# ─── Core Logic ───────────────────────────────────────────
def calculate(expression):
    try:
        if expression.startswith("sqrt("):
            num = float(expression[5:-1])
            if num < 0:
                return "Error: sqrt of negative!"
            return round(math.sqrt(num), 10)
        result = eval(expression)
        return round(result, 10)
    except ZeroDivisionError:
        return "Error: Divide by zero!"
    except Exception:
        return "Error: Invalid input!"


# ─── App ──────────────────────────────────────────────────
class CalculatorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🧮 Python Calculator")
        self.root.resizable(False, False)
        self.root.configure(bg="#1e1e2e")

        self.expression = ""
        self.history = load_history()  # ← loads saved history from file

        self.build_ui()

    # ── UI Builder ────────────────────────────────────────
    def build_ui(self):
        # ── Display ──
        self.display_var = tk.StringVar(value="0")

        display_frame = tk.Frame(self.root, bg="#1e1e2e", pady=10)
        display_frame.pack(padx=15, fill="x")

        self.display = tk.Label(
            display_frame,
            textvariable=self.display_var,
            font=("SF Pro Display", 36, "bold"),
            bg="#1e1e2e",
            fg="#cdd6f4",
            anchor="e",
            padx=10,
            wraplength=340,
        )
        self.display.pack(fill="x")

        self.sub_display = tk.Label(
            display_frame,
            text="",
            font=("SF Pro Display", 13),
            bg="#1e1e2e",
            fg="#6c7086",
            anchor="e",
            padx=10,
        )
        self.sub_display.pack(fill="x")

        # ── Buttons ──
        btn_frame = tk.Frame(self.root, bg="#1e1e2e")
        btn_frame.pack(padx=15, pady=(0, 10))

        buttons = [
            ["AC", "+/-", "%",  "÷"],
            ["7",  "8",  "9",  "×"],
            ["4",  "5",  "6",  "−"],
            ["1",  "2",  "3",  "+"],
            ["√",  "0",  "x²", "="],
        ]

        for r, row in enumerate(buttons):
            for c, label in enumerate(row):
                self.make_button(btn_frame, label, r, c)

        # ── History Label ──
        hist_label = tk.Label(
            self.root,
            text="📜  History",
            font=("SF Pro Display", 12, "bold"),
            bg="#1e1e2e",
            fg="#89b4fa",
            anchor="w",
        )
        hist_label.pack(padx=15, fill="x")

        # ── History Box ──
        self.history_box = scrolledtext.ScrolledText(
            self.root,
            height=6,
            font=("Courier New", 11),
            bg="#181825",
            fg="#cdd6f4",
            bd=0,
            relief="flat",
            state="disabled",
            wrap="word",
        )
        self.history_box.pack(padx=15, pady=(4, 15), fill="x")

        # ── Load old history into box on startup ──
        if self.history:
            self.history_box.config(state="normal")
            for entry in self.history:
                self.history_box.insert("end", entry + "\n")
            self.history_box.see("end")
            self.history_box.config(state="disabled")

    # ── Button Factory ────────────────────────────────────
    def make_button(self, parent, label, row, col):
        if label in ["÷", "×", "−", "+", "="]:
            bg, fg, active_bg = "#f38ba8", "#1e1e2e", "#eba0ac"
        elif label in ["AC", "+/-", "%"]:
            bg, fg, active_bg = "#45475a", "#cdd6f4", "#585b70"
        elif label in ["√", "x²"]:
            bg, fg, active_bg = "#89b4fa", "#1e1e2e", "#b4d0ff"
        else:
            bg, fg, active_bg = "#313244", "#cdd6f4", "#45475a"

        btn = tk.Button(
            parent,
            text=label,
            font=("SF Pro Display", 18, "bold"),
            bg=bg,
            fg=fg,
            activebackground=active_bg,
            activeforeground=fg,
            bd=0,
            relief="flat",
            cursor="hand2",
            width=4,
            height=2,
            command=lambda l=label: self.on_press(l),
        )
        btn.grid(row=row, column=col, padx=5, pady=5)

    # ── Button Logic ──────────────────────────────────────
    def on_press(self, label):
        if label == "AC":
            self.expression = ""
            self.display_var.set("0")
            self.sub_display.config(text="")

        elif label == "+/-":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:]
                else:
                    self.expression = "-" + self.expression
                self.display_var.set(self.expression)

        elif label == "%":
            try:
                val = float(self.expression) / 100
                self.expression = str(val)
                self.display_var.set(self.expression)
            except:
                self.display_var.set("Error")

        elif label == "√":
            try:
                val = float(self.expression)
                expr = f"sqrt({val})"
                result = calculate(expr)
                self.record_history(f"√{val}", result)
                self.sub_display.config(text=f"√ {val}")
                self.expression = str(result)
                self.display_var.set(result)
            except:
                self.display_var.set("Error")

        elif label == "x²":
            try:
                val = float(self.expression)
                result = calculate(f"{val}**2")
                self.record_history(f"{val}²", result)
                self.sub_display.config(text=f"{val} ²")
                self.expression = str(result)
                self.display_var.set(result)
            except:
                self.display_var.set("Error")

        elif label == "=":
            if self.expression:
                expr_display = (
                    self.expression
                    .replace("**", "^")
                    .replace("*", "×")
                    .replace("/", "÷")
                    .replace("-", "−")
                )
                result = calculate(self.expression)
                self.record_history(expr_display, result)
                self.sub_display.config(text=expr_display)
                self.expression = str(result)
                self.display_var.set(result)

        else:
            op_map = {"÷": "/", "×": "*", "−": "-"}
            char = op_map.get(label, label)
            self.expression += char
            self.display_var.set(
                self.expression
                .replace("*", "×")
                .replace("/", "÷")
                .replace("-", "−")
            )

    # ── Save to history box AND file ──────────────────────
    def record_history(self, expr, result):
        entry = f"  {expr} = {result}"
        add_entry(self.history, entry)   # ← saves to history.json

        self.history_box.config(state="normal")
        self.history_box.insert("end", entry + "\n")
        self.history_box.see("end")
        self.history_box.config(state="disabled")


# ─── Launch ───────────────────────────────────────────────
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()