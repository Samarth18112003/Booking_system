from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.clock import Clock
from datetime import datetime, timedelta

class ClockApp(BoxLayout):
    def _init_(self, **kwargs):
        super(ClockApp, self)._init_(**kwargs)
        self.orientation = 'vertical'

        # Create the main content area
        self.main_content = BoxLayout(orientation='horizontal', spacing=5)
        self.add_widget(self.main_content)

        self.start_time = datetime.now()

        # Create the swipe windows
        self.swipe_windows = {
            'Alarms': BoxLayout(orientation='vertical', spacing=5),
            'World Clocks': BoxLayout(orientation='vertical', spacing=5),
            'Stopwatch': BoxLayout(orientation='vertical', spacing=5),
            'Timer': BoxLayout(orientation='vertical', spacing=5)
        }

        # Create buttons for each swipe window
        for window_name, window_content in self.swipe_windows.items():
            self.main_content.add_widget(Button(text=window_name, on_press=self.show_swipe_window(window_name)))
            window_content.add_widget(Label(text=f"Content for {window_name}"))

        # Inside the 'World Clocks' section
        world_clock_content = self.swipe_windows['World Clocks']
        world_clock_content.add_widget(Label(text="World Clocks:"))

        # Add world clocks here (a dictionary of city names and offsets)
        world_clocks = {
            'New York': -5,
            'London': 0,
            'Tokyo': 9
        }

        for city, offset in world_clocks.items():
            world_time = "City: {} - Time: {}{}".format(city, self.get_world_time(offset),
                                                        self.get_offset_string(offset))
            world_clock_content.add_widget(Label(text=world_time))

        # Inside the 'Alarms' section
        self.alarm_content = self.swipe_windows['Alarms']
        self.alarm_content.add_widget(Label(text="Alarms:"))

        # Text input for setting alarm time
        self.alarm_time_input = TextInput(hint_text="Enter alarm time (HH:MM)")

        # Function to add an alarm
        def add_alarm(instance):
            alarm_time = self.alarm_time_input.text
            if self.validate_alarm_time(alarm_time):
                alarm_label = Label(text=f"Alarm set for {alarm_time}")
                self.alarm_content.add_widget(alarm_label)
                Clock.schedule_once(lambda dt, label=alarm_label: self.remove_alarm(label), self.calculate_time_to_alarm(alarm_time))

        add_alarm_button = Button(text="Add Alarm")
        add_alarm_button.bind(on_press=add_alarm)
        self.alarm_content.add_widget(self.alarm_time_input)
        self.alarm_content.add_widget(add_alarm_button)

        # Inside the 'Stopwatch' section
        stopwatch_content = self.swipe_windows['Stopwatch']
        stopwatch_content.add_widget(Label(text="Stopwatch:"))

        # Create buttons for start and stop
        is_running = False

        def start_stopwatch(instance):
            nonlocal is_running
            is_running = True

        start_button = Button(text="Start")
        start_button.bind(on_press=start_stopwatch)
        stopwatch_content.add_widget(start_button)

        def stop_stopwatch(instance):
            nonlocal is_running
            is_running = False

        stop_button = Button(text="Stop")
        stop_button.bind(on_press=stop_stopwatch)
        stopwatch_content.add_widget(stop_button)

        # Create a label to display the stopwatch time
        self.stopwatch_label = Label(text="00:00:00")
        stopwatch_content.add_widget(self.stopwatch_label)

        # Function to update the stopwatch time
        def update_stopwatch_time(dt):
            if is_running:
                self.update_stopwatch_label()  # Call the function to update the label

        Clock.schedule_interval(update_stopwatch_time, 1)

        def update_stopwatch_label(self):
            # Update the stopwatch label with the elapsed time
            if hasattr(self, 'start_time'):
                now = datetime.now()
                elapsed_time = now - self.start_time
                hours, remainder = divmod(elapsed_time.total_seconds(), 3600)
                minutes, seconds = divmod(remainder, 60)
                self.stopwatch_label.text = f"{int(hours):02d}:{int(minutes):02d}:{int(seconds):02d}"

        def show_swipe_window(self, window_name):
            def show_window(instance):
                self.main_content.clear_widgets()
                self.main_content.add_widget(Button(text="Back to Main", on_press=self.show_main_window))
                self.main_content.add_widget(self.swipe_windows[window_name])

            return show_window

        def show_main_window(self, instance):
            self.main_content.clear_widgets()
            for window_name, _ in self.swipe_windows.items():
                self.main_content.add_widget(Button(text=window_name, on_press=self.show_swipe_window(window_name)))

        def validate_alarm_time(self, time_str):
            # You can implement time validation logic here
            # For example, check if the input is in HH:MM format
            return True  # Add your validation criteria

        def calculate_time_to_alarm(self, alarm_time):
            # You can calculate the time remaining until the alarm and return it in seconds
            # Here, we assume a simple implementation for demonstration
            return 5  # 5 seconds for demonstration

        def remove_alarm(self, alarm_label):
            self.alarm_content.remove_widget(alarm_label)

        def get_world_time(self, offset):
            # Get the current device time
            current_time = datetime.now()

            # Calculate the world time based on the offset
            world_time = current_time + timedelta(hours=offset)

            # Format the world time as a string
            world_time_str = world_time.strftime('%Y-%m-%d %H:%M:%S')  # Customize the format as needed

            return world_time_str

        def get_offset_string(self, offset):
            if offset > 0:
                return f" (UTC+{offset})"
            elif offset < 0:
                return f" (UTC{offset})"
            else:
                return " (UTC)"

        # Inside the 'Timer' section
        timer_content = self.swipe_windows['Timer']
        timer_content.add_widget(Label(text="Timer:"))
    
        # Text input for setting timer duration
        timer_duration_input = TextInput(hint_text="Enter timer duration (seconds)")
    
        # Initialize timer_duration
        timer_duration = 0
    
        # Function to update the timer label with the remaining time
        def update_timer_label(dt):
            nonlocal timer_duration
            if timer_duration > 0:
                timer_duration -= 1
                minutes, seconds = divmod(timer_duration, 60)
                timer_label.text = f"Timer: {minutes:02d}:{seconds:02d}"
            else:
                timer_label.text = "Timer: 00:00"
                Clock.unschedule(update_timer_label)  # Stop the timer when it reaches 0
    
        # Function to start the timer
        def start_timer(instance):
            nonlocal timer_duration
            if not timer_duration_input.text.isdigit():
                return  # Invalid input, do nothing
            timer_duration = int(timer_duration_input.text)
            minutes, seconds = divmod(timer_duration, 60)
            timer_label.text = f"Timer: {minutes:02d}:{seconds:02d}"
            Clock.schedule_interval(update_timer_label, 1)  # Update the timer label every second
    
        start_timer_button = Button(text="Start Timer")
        start_timer_button.bind(on_press=start_timer)
        timer_content.add_widget(timer_duration_input)
        timer_content.add_widget(start_timer_button)
    
        # Create a label to display the timer countdown
        timer_label = Label(text="Timer: 00:00")
        timer_content.add_widget(timer_label)



class ClockAppMain(App):
    def build(self):
        return ClockApp()

if _name_ == '_main_':
    ClockAppMain().run()





"""
# Inside the 'Alarms' section in ClockApp class
alarm_content = self.swipe_windows['Alarms']
alarm_content.add_widget(Label(text="Alarms:"))

# Function to add an alarm
def add_alarm(instance):
    alarm_time = "Set your alarm time here"  # You can use text inputs to set the time
    alarm_content.add_widget(Label(text=alarm_time))

add_alarm_button = Button(text="Add Alarm")
add_alarm_button.bind(on_press=add_alarm)
alarm_content.add_widget(add_alarm_button)
"""


"""
# Inside the 'World Clocks' section in ClockApp class
world_clock_content = self.swipe_windows['World Clocks']
world_clock_content.add_widget(Label(text="World Clocks:"))

# Add world clocks here
for city, offset in world_clocks.items():
    world_time = "City: {} - Time: {}".format(city, "Set the time here")
    world_clock_content.add_widget(Label(text=world_time))
"""


"""
# Inside the 'Stopwatch' section in ClockApp class
stopwatch_content = self.swipe_windows['Stopwatch']
stopwatch_content.add_widget(Label(text="Stopwatch:"))

# Create buttons for start and stop
is_running = False

def start_stopwatch(instance):
    nonlocal is_running
    is_running = True

start_button = Button(text="Start")
start_button.bind(on_press=start_stopwatch)
stopwatch_content.add_widget(start_button)

def stop_stopwatch(instance):
    nonlocal is_running
    is_running = False

stop_button = Button(text="Stop")
stop_button.bind(on_press=stop_stopwatch)
stopwatch_content.add_widget(stop_button)

# Create a label to display the stopwatch time
stopwatch_label = Label(text="00:00:00")
stopwatch_content.add_widget(stopwatch_label)

# Function to update the stopwatch time
from kivy.clock import Clock

def update_stopwatch_time(dt):
    if is_running:
        # Update the stopwatch time here
        # Use the Clock.schedule_interval to call this function periodically

Clock.schedule_interval(update_stopwatch_time, 1)
"""


"""
# Inside the 'Timer' section in ClockApp class
timer_content = self.swipe_windows['Timer']
timer_content.add_widget(Label(text="Timer:"))

# Create an input field for timer duration
timer_duration_input = TextInput(hint_text="Enter timer duration (seconds)")

# Function to start the timer
def start_timer(instance):
    timer_duration = int(timer_duration_input.text)
    # Implement timer functionality here

start_timer_button = Button(text="Start Timer")
start_timer_button.bind(on_press=start_timer)
timer_content.add_widget(timer_duration_input)
timer_content.add_widget(start_timer_button)

# Create a label to display the timer countdown
timer_label = Label(text="Timer: 00:00")
timer_content.add_widget(timer_label)
"""