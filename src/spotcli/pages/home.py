from textual.containers import Center
from textual.widgets import Label


class HomePage(Center):
    def compose(self):
        yield Label("🎵 Welcome to SpotCLI")