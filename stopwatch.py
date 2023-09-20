from textual.app import App
from textual.containers import ScrollableContainer
from textual.widgets import Footer, Header, Button, Static 

class TimeDisplay(Static):
    pass

class Rando(Static):
    pass

class Thing(Static):
    pass

class stopwatch(Static):
    def compose(self):
        #Valid button variants are 'default'(black), 'error'(red), 'primary'(blue), 'success'(green), or 'warning'(yellow)
        yield Button("Start",variant='success')
        yield Button("Stop",variant='error')
        yield Button("Reset",variant='primary')
        #yield Rando("I'm just a random thing😀")
        with Rando():
            yield Thing("I'm just a random thing😀")
        yield TimeDisplay("00:00:00.00")

class StopwatchApp(App):
    font_size = 40
    BINDINGS = [
            ('d','toggle_dark_mode','Toggle light/dark mode'),
            #("right", "scroll_right", "Scroll Right"),
        ]
    
    CSS_PATH = "stopwatch.css"
    
    def compose(self):
        """What widgets is the app composed of?"""
        
        yield Header(show_clock=True)
        yield Footer()
        with ScrollableContainer(id='stopwatches'):
            yield stopwatch()
            yield stopwatch()
            yield stopwatch()       
    
    #EXTREMELY IMPORTANT TO PUT 'action_' before method/function
    def action_toggle_dark_mode(self):
        self.dark = not self.dark


if __name__ == "__main__":
    StopwatchApp().run()
