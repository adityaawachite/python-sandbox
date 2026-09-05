
# First, we need to import the necessary tools (libraries) for our calculator.
# 'tkinter' is used to create the visual interface (the buttons, screen, window).
import tkinter as tk
from tkinter import messagebox

# We need 'math' for standard scientific calculations like sin, cos, square roots.
import math

# We need 'numpy' (your "bumpy"!) to analyze sequences and predict patterns.
import numpy as np

class ScientificCalculator:
    def __init__(self, root):
        # We start by setting up the main window of our application.
        self.root = root
        self.root.title("Scientific Calculator")
        
        # Let's give it a nice vertical rectangular shape, like a real calculator.
        self.root.geometry("400x600")
        
        # We lock the window size so the layout doesn't get messed up if the user drags the corners.
        self.root.resizable(False, False)
        
        # Adding a cool dark-blue background color to make it look premium.
        self.root.configure(bg="#2c3e50")

        # This string will keep track of whatever the user types on the screen.
        self.equation = ""
        
        # --- Setting up the Display Screen ---
        # StringVar is a special Tkinter variable that updates the screen automatically when its value changes.
        self.display_var = tk.StringVar()
        
        # This is the actual text box at the top of the calculator.
        # We make the font big and bold, align the text to the right, and give it a slight border.
        self.display = tk.Entry(self.root, textvariable=self.display_var, font=('Arial', 20, 'bold'), 
                                bg="#ecf0f1", fg="#2c3e50", bd=10, justify="right")
        
        # We place the screen at the very top (row 0) and make it span across all 4 columns.
        self.display.grid(row=0, column=0, columnspan=4, ipadx=8, ipady=20, pady=10)

        # Now, let's call the function that draws all the buttons on the screen.
        self.create_buttons()

    def create_buttons(self):
        # Here is our blueprint for the buttons. 
        # Each item is a tuple containing: (Button Text, Row Number, Column Number)
        buttons = [
            ('C', 1, 0), ('(', 1, 1), (')', 1, 2), ('/', 1, 3),
            ('7', 2, 0), ('8', 2, 1), ('9', 2, 2), ('*', 2, 3),
            ('4', 3, 0), ('5', 3, 1), ('6', 3, 2), ('-', 3, 3),
            ('1', 4, 0), ('2', 4, 1), ('3', 4, 2), ('+', 4, 3),
            ('0', 5, 0), ('.', 5, 1), ('^2', 5, 2), ('=', 5, 3),
            ('sin', 6, 0), ('cos', 6, 1), ('tan', 6, 2), ('sqrt', 6, 3),
            ('log', 7, 0), ('ln', 7, 1), ('DEL', 7, 2), ('LogPattern', 7, 3)
        ]

        # We loop through our blueprint and create a button for each item.
        for (text, row, col) in buttons:
            # The lambda function here is a neat trick. It ensures that when a button is clicked,
            # it passes its specific text (like '7' or '+') to our click handler function.
            action = lambda x=text: self.on_button_click(x)
            
            # Creating the actual button widget with some styling (fonts, colors, hover effects).
            btn = tk.Button(self.root, text=text, font=('Arial', 14, 'bold'), bg="#34495e", fg="white",
                            activebackground="#1abc9c", activeforeground="white", relief="ridge", bd=3, command=action)
            
            # Placing the button exactly where our blueprint says it should go.
            btn.grid(row=row, column=col, sticky="nsew", padx=5, pady=5, ipadx=10, ipady=10)

        # To make sure the buttons stretch and look proportional, we configure the grid weights.
        # This tells the window to share the extra space equally among columns and rows.
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
        for i in range(1, 8):
            self.root.grid_rowconfigure(i, weight=1)

    def on_button_click(self, char):
        # This function acts like a traffic cop, directing what to do based on which button was clicked.
        
        if char == 'C':
            # 'C' means Clear. We wipe the equation memory and the screen.
            self.equation = ""
            self.display_var.set(self.equation)
            
        elif char == 'DEL':
            # 'DEL' means Delete. We slice off the very last character from our equation string.
            self.equation = self.equation[:-1]
            self.display_var.set(self.equation)
            
        elif char == '=':
            # Time to do the math! We hand this off to our basic evaluation function.
            self.evaluate_equation()
            
        elif char in ('sin', 'cos', 'tan', 'sqrt', 'log', 'ln', '^2'):
            # These are special scientific functions. We have a separate function to handle them safely.
            self.evaluate_scientific(char)
            
        elif char == 'LogPattern':
            # Ah, your special feature! Time to wake up NumPy and predict the log pattern.
            self.predict_log_pattern()
            
        else:
            # If it's just a regular number or symbol (like 7 or +), just add it to our equation string.
            self.equation += str(char)
            self.display_var.set(self.equation)

    def evaluate_equation(self):
        # This try-except block is what makes the program "foolproof". 
        # If the user types something crazy like "5++*6", the program won't crash; it will just show an error.
        try:
            # Python's eval() function calculates math automatically, but it uses '**' for powers.
            # So, we gently replace the '^' symbol with '**' before doing the math.
            eval_string = self.equation.replace('^', '**')
            
            # Calculate the result and turn it back into a string.
            result = str(eval(eval_string))
            
            # Show the result on the screen and update our memory so the user can keep calculating.
            self.display_var.set(result)
            self.equation = result
            
        except ZeroDivisionError:
            # Catching the classic "dividing by zero" mistake.
            self.display_var.set("Error: Div by Zero")
            self.equation = ""
        except Exception:
            # Catching any other typos or syntax errors.
            self.display_var.set("Syntax Error")
            self.equation = ""

    def evaluate_scientific(self, func):
        # This handles functions that act on a single number (e.g., typing '90' and pressing 'sin').
        try:
            # First, we evaluate whatever is currently on the screen to get a single number.
            val = float(eval(self.equation) if self.equation else 0)
            
            # Now we figure out which math function to apply.
            if func == 'sin':
                result = math.sin(math.radians(val)) # Converting to radians because math.sin expects it!
            elif func == 'cos':
                result = math.cos(math.radians(val))
            elif func == 'tan':
                result = math.tan(math.radians(val))
            elif func == 'sqrt':
                result = math.sqrt(val)
            elif func == 'log':
                result = math.log10(val) # Base-10 logarithm
            elif func == 'ln':
                result = math.log(val)   # Natural logarithm (Base-e)
            elif func == '^2':
                result = val ** 2
            
            # Sometimes math gives us ugly long decimals like 0.99999999999. 
            # We round it to 8 decimal places to keep the screen clean.
            result = round(result, 8)
            
            # Display it!
            self.display_var.set(str(result))
            self.equation = str(result)
            
        except ValueError:
            # Trying to find the square root of a negative number, for example.
            self.display_var.set("Math Error")
            self.equation = ""
        except Exception:
            self.display_var.set("Error")
            self.equation = ""

    def predict_log_pattern(self):
        """
        This is the special requested feature. It uses NumPy to find a pattern in 
        a comma-separated sequence and predicts the next logarithmic value.
        """
        try:
            # We expect the user to type something like: "10,100,1000"
            # First, we split this string into a list of individual items based on the commas.
            input_data = self.equation.split(',')
            
            # We need at least two numbers to find a pattern.
            if len(input_data) < 2:
                messagebox.showinfo("Pattern Info", "Please enter at least 2 values separated by commas. Example: 10,100,1000")
                return

            # We convert our list of strings into a NumPy array of floating-point numbers.
            # We use 'strip()' to remove any accidental spaces the user might have typed.
            values = np.array([float(x.strip()) for x in input_data])
            
            # Let's calculate the log10 for the entire sequence at once (NumPy is fast at this!).
            logs = np.log10(values)
            
            # To find the pattern, we map out the data points (0, 1, 2...) on an X-axis.
            x_indices = np.arange(len(values))
            
            # We use 'polyfit' to draw the best straight line (Degree 1) through our log values.
            # This gives us the mathematical formula for the trend.
            poly_coefficients = np.polyfit(x_indices, logs, 1) 
            
            # Now, what is the next step in the sequence? It's the length of our current array.
            next_index = len(values)
            
            # We ask NumPy to predict the log value for this next step using our trend formula.
            next_log = np.polyval(poly_coefficients, next_index)
            
            # We reverse the log (10 to the power of the log) to find what the actual next number is.
            next_value = 10 ** next_log

            # We format this nicely and show it in a pop-up alert box.
            pattern_result = f"Predicted Next Log10: {next_log:.4f}\nPredicted Next Value: {next_value:.4f}"
            messagebox.showinfo("Log Pattern Prediction", pattern_result)
            
            # Finally, we put the predicted next value onto the calculator screen so the user can use it.
            self.equation = str(round(next_value, 4))
            self.display_var.set(self.equation)

        except Exception as e:
            # If the user typed letters or messed up the format, we catch it gracefully here.
            messagebox.showerror("Pattern Error", "Invalid format! Please use only numbers and commas.")
            self.equation = ""
            self.display_var.set("")

# This is the starting point of our application.
if __name__ == "__main__":
    # We create the main Tkinter engine.
    root = tk.Tk()
    
    # We pass that engine to our ScientificCalculator class to build the UI.
    app = ScientificCalculator(root)
    
    # We start the infinite loop that keeps the window open and waits for user clicks!
    root.mainloop()
