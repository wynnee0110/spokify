from textual.widgets import Static


class PlayerBar(Static):
    def on_mount(self):
        self.update("▶ Nothing Playing                              🔊 70%")