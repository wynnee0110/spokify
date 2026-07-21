from textual.widgets import Static


class Content(Static):
    def on_mount(self):
        self.update("Welcome to SpotCLI!")