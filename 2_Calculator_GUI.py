"""
This code creates a calculator GUI with Python programming language using the 'kivy' package. Kivy can run on
multiple platforms and most of the graphics processing runs directly on GPU.

GUI Display: 
Basic Calcular with numbers (0-9),
functions (+, -, /, *),
can perform float, double operations.
"""

#pip install kivy 

# Import the necessary Kivy modules
from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

# Define a Kivy application class
class CalculatorApp(App):
    def build(self):
        # Create the main root widget as a vertical box layout
        root_layout = BoxLayout(orientation='vertical')

        # Create the output label
        output_label = Label(size_hint_y=0.75, font_size=50)

        # Define the symbols for the calculator buttons
        button_symbols = ('1', '2', '3', '+',
                          '4', '5', '6', '-',
                          '7', '8', '9', '.',
                          '0', '*', '/', '=')

        # Create a grid layout for the calculator buttons
        button_grid = GridLayout(cols=4, size_hint_y=2)

        # Add buttons with the specified symbols to the grid
        for symbol in button_symbols:
            button_grid.add_widget(Button(text=symbol))

        # Create a "Clear" button
        clear_button = Button(text='Clear', size_hint_y=None, height=100)

        # Define a function to handle button presses
        def print_button_text(instance):
            output_label.text += instance.text

        # Bind the button press function to all buttons except the first
        for button in button_grid.children[1:]:
            button.bind(on_press=print_button_text)

        # Define a function to resize the label text
        def resize_label_text(label, new_height):
            label.fontsize = 0.5 * label.height

        # Bind the label height change to the label text resizing function
        output_label.bind(height=resize_label_text)

        # Define a function to evaluate the result
        def evaluate_result(instance):
            try:
                output_label.text = str(eval(output_label.text))
            except SyntaxError:
                output_label.text = 'Syntax Error!'

        # Bind the "Evaluate" button to the result evaluation function
        button_grid.children[0].bind(on_press=evaluate_result)

        # Define a function to clear the label
        def clear_label(instance):
            output_label.text = ''

        # Bind the "Clear" button to the label clearing function
        clear_button.bind(on_press=clear_label)

        # Add widgets to the root layout
        root_layout.add_widget(output_label)
        root_layout.add_widget(button_grid)
        root_layout.add_widget(clear_button)

        # Return the main root widget
        return root_layout

# Run the Kivy application
CalculatorApp().run()
