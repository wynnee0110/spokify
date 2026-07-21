from textual.widgets import Static


class Content(Static):

    def show_page(self, name: str):
        self.update(f"[b]{name}[/b]")