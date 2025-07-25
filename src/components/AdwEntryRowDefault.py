from gi.repository import Gtk, GObject, Adw, Gdk, Gio, Pango, GLib

class AdwEntryRowDefault(Adw.EntryRow):
    ACTION_ROW_ICON_SIZE = 34

    def __init__(self, default_text=None, icon_name=None, **kwargs):
        super().__init__(**kwargs)
        self.default_text = default_text
        self.row_btn = None

        if icon_name:
            row_img = Gtk.Image(icon_name=icon_name, pixel_size=self.ACTION_ROW_ICON_SIZE)
            self.add_prefix(row_img)

        self.connect('changed', self.on_changed)

        self.row_btn = Gtk.Button(
            icon_name='gl-undo', 
            valign=Gtk.Align.CENTER,
            visible=False
        )
        
        self.row_btn.connect('clicked', self.on_reset_default_clicked)
        self.row_btn.set_sensitive(self.default_text != self.get_text())

        self.add_suffix(self.row_btn)
        self.set_default_text(default_text)

    def on_reset_default_clicked(self, *args):
        self.set_text(self.default_text)

    def on_changed(self, *args):
        if self.row_btn:
            self.row_btn.set_sensitive(self.default_text != self.get_text())

    def set_default_text(self, text: str | None):
        self.default_text = text
        self.row_btn.set_visible(text != None)
        self.row_btn.set_sensitive(self.default_text != self.get_text())
