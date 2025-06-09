import reflex as rx

class ThemeState(rx.State):
    dark_mode: bool = False

    def toggle_dark_mode(self):
        self.dark_mode = not self.dark_mode


class colors:
    primary = "#b8860b"
    secondary = "#222"
    white = "#fff"
    background = "#fafafa"