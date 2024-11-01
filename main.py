import socket
from kivy.app import App
from kivy.lang import Builder
from kivy.properties import StringProperty
from kivy.uix.gridlayout import GridLayout
ARDUINO_IP = '127.0.0.1'  # Use localhost for the mock server
ARDUINO_PORT = 80  # Port that matches the mock server
# KV content as a string
kv = '''
Widgets:
<Widgets>:
    rows: 13
    Label:
        text: "Twisting Machine"
        size_hint_y: None
        height: "50dp"

    # First row
    GridLayout:
        cols: 9
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25dp"
        Label:
            text: "Core yarn count(Ne):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_a
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_a', 'a')
                background_normal: "right.jpg"

        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "50dp"
        Label:
            text: "TPI:"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_g
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_g', 'g')
                background_normal: "right.jpg"

    # Second row
    GridLayout:
        cols: 11
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25"
        Label:
            text: "Yarn count 1(Ne):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_b
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_b', 'b')
                background_normal: "right.jpg"
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "50dp"
        Label:
            text: "Twist length:"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        Label:
            text: ""  # Placeholder for displaying results
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"
            id: result_label_i  # Unique id for h result

        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "80dp"
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1  # Background color
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                text: "Calculate"
                on_press: root.calculate_i()
                color: 1, 1, 1, 1

    # Third row
    GridLayout:
        cols: 11
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25"
        Label:
            text: "Yarn count 2(Ne):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_c
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_c', 'c')
                background_normal: "right.jpg"
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "50dp"
        Label:
            text: "Resultant count:"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        Label:
            text: ""  # Placeholder for displaying results
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"
            id: result_label_h  # Unique id for i result

        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "80dp"
            canvas.before:
                Color:
                    rgba: 1, 1, 1, 1  # Background color
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                text: "Calculate"
                on_press: root.calculate_h()
                color: 1, 1, 1, 1

    # Fourth row
    GridLayout:
        cols: 5
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25"
        Label:
            text: "Yarn count 3(Ne):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_d
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"

        # Button with border
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_d', 'd')
                background_normal: "right.jpg"

    # Fifth row
    GridLayout:
        cols: 5
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25dp"
        Label:
            text: "Yarn count 4(Ne):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_e
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"

        # Button with border
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_e', 'e')
                background_normal: "right.jpg"
    Label:
        text: ""
        size_hint_x: None
        size_hint_y: None
        height: "50dp"
        width: "25dp"
    GridLayout:
        cols:5
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25dp"
        Label:
            text: "Winding speed(m/min):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_WS
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"

        # Button with border
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_WS', 'WS')
                background_normal: "right.jpg"
    GridLayout:
        cols:5
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25dp"
        Label:
            text: "Angle(θ):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_Angle
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"

        # Button with border
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_Angle', 'Angle')
                background_normal: "right.jpg"
    GridLayout:
        cols:5
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25dp"
        Label:
            text: "Beam length(m):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_Len
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"

        # Button with border
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_Len', 'Len')
                background_normal: "right.jpg"
    GridLayout:
        cols:5
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25dp"
        Label:
            text: "Bobbin dia(m):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_Dia
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"

        # Button with border
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_Dia', 'Dia')
                background_normal: "right.jpg"
    GridLayout:
        cols:5
        Label:
            text: ""
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "25dp"
        Label:
            text: "Twist(s/z):"
            size_hint_x: None
            size_hint_y: None
            height: "25dp"
            width: "150dp"
        TextInput:
            id: input_field_twist
            multiline: False
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "150dp"

        # Button with border
        BoxLayout:
            size_hint_x: None
            size_hint_y: None
            height: "30dp"
            width: "30dp"
            canvas.before:
                Color:
                    rgba: 0, 0, 0, 1  # Border color (black)
                Line:
                    width: 3.5  # Border thickness
                    rectangle: (self.x, self.y, self.width, self.height)

            Button:
                on_press: root.click('input_field_twist', 'twist')
                background_normal: "right.jpg"
    Label:
        text: ""
        size_hint_x: None
        size_hint_y: None
        height: "50dp"
        width: "25dp"

'''
class Widgets(GridLayout):
    # Declare variables for each row
    a = StringProperty("")
    b = StringProperty("")
    c = StringProperty("")
    d = StringProperty("")
    e = StringProperty("")
    g = StringProperty("")
    usage = StringProperty("")
    WS = StringProperty("")
    Angle = StringProperty("")
    Len = StringProperty("")
    Dia = StringProperty("")
    twist = StringProperty("")
    h = StringProperty("")
    f = StringProperty("")# Add h as a property

    def click(self, field_id, variable_name):
        # Set the corresponding variable to the input text
        setattr(self, variable_name, self.ids[field_id].text)
        value = getattr(self, variable_name)
        print(f"Stored in '{variable_name}': {value}")

        # Send the variable and its value over Wi-Fi
        message = f"{variable_name}:{value}"
        self.send_data(message)

    def send_data(self, message):
        """Send data to the Arduino via Wi-Fi."""
        try:
            # Create a socket and connect to the mock Arduino
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.connect((ARDUINO_IP, ARDUINO_PORT))
                s.sendall(message.encode())
                print(f"Sent: {message}")
        except Exception as e:
            print(f"Failed to send data: {e}")

    def get_input_value(self, input_id):
        """Retrieve and convert the input value to float."""
        input_value = self.ids[f'input_field_{input_id}'].text
        if input_value.strip():  # Check if not empty
            try:
                return float(input_value)
            except ValueError:
                return None  # Return None if conversion fails
        return None  # Return None if input is empty

    def calculate_h(self):
        try:
            a = self.get_input_value('a')
            b = self.get_input_value('b')
            c = self.get_input_value('c')
            d = self.get_input_value('d')
            e = self.get_input_value('e')

            # Filter out None and zero values
            values = [x for x in (a, b, c, d, e) if x is not None and x != 0]

            if not values:
                self.ids.result_label_h.text = "Invalid input"
                return

            # Calculate h using the filtered values
            h = 1 / sum(1 / value for value in values)
            self.h = f"{h:.2f}"  # Format to 2 decimal places
            self.ids.result_label_h.text = f"h: {self.h}"  # Display h value

            # Send h value to Arduino
            self.send_data(f"h:{self.h}")

        except ZeroDivisionError:
            self.ids.result_label_h.text = "Undefined (division by zero)"
        except Exception as e:
            self.ids.result_label_h.text = f"Error: {str(e)}"

    def calculate_i(self):
        try:
            g = self.get_input_value('g')
            if g is not None:
                if g != 0:
                    i_value = 1 / g
                    # Update the display label with the calculated value of i
                    self.ids.result_label_i.text = f"{i_value:.2f}"  # Format to 2 decimal places
                else:
                    self.ids.result_label_i.text = "Undefined (g=0)"
            else:
                self.ids.result_label_i.text = "Invalid input"
        except Exception as e:
            self.ids.result_label_i.text = f"Error: {str(e)}"

class TheLabApp(App):
    def build(self):
        Builder.load_string(kv)  # Load the KV layout directly from the string
        return Widgets()

TheLabApp().run()

