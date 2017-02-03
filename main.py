import G213Colors
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk, Gio
NAME = "G213Colors"



class Window(Gtk.Window):

    hexColor = "000000"
    ctime = "500"
    btime = "500"

    def sendStatic(self):
        global hexColor
        myG = G213Colors
        myG.connectG()
        myG.sendColorCommand(hexColor)
        myG.disconnectG()

    def sendBreathe(self):
        global hexColor
        myG = G213Colors
        myG.connectG()
        myG.sendBreatheCommand(hexColor, btime)
        myG.disconnectG()

    def sendCycle(self):
        global time
        myG = G213Colors
        myG.connectG()
        myG.sendCycleCommand(ctime)
        myG.disconnectG()

    def color_set(self, colorbutton):
        global hexColor
        color = colorbutton.get_rgba()
        red = int(color.red * 255)
        green = int(color.green * 255)
        blue = int(color.blue * 255)
        hexColor = "%02x%02x%02x" % (red, green, blue)
        print(hexColor)

    def sendManager(self):
        self.stackName = self.stack.get_visible_child_name()
        if self.stackName == "static":
            self.sendStatic()
        elif self.stackName == "cycle":
            self.sendCycle()
        elif self.stackName == "breathe":
            self.sendBreathe()
            
    def on_ok_button_clicked(self, button):
        global hexColor
        global ctime
        global btime
        ctime = self.sbCycle.get_value_as_int()
        btime = self.sbBCycle.get_value_as_int()
        print(ctime)
        print(self.stack.get_visible_child_name())
        self.sendManager()

    def __init__(self):

        Gtk.Window.__init__(self, title=NAME)
        self.set_border_width(10)

        vBoxMain = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.add(vBoxMain)

        ###STACK
        self.stack = Gtk.Stack()
        self.stack.set_transition_type(Gtk.StackTransitionType.SLIDE_LEFT_RIGHT)
        self.stack.set_transition_duration(1000)

        ###STATIC TAB
        vBoxStatic = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        staticColorButton = Gtk.ColorButton()
        staticColorButton.connect("color-set", self.color_set)
        vBoxStatic.add(staticColorButton)

        self.stack.add_titled(vBoxStatic, "static", "Static")

        ###CYCLE TAB
        vBoxCycle = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        self.adjCycle = Gtk.Adjustment(5000, 500, 65535, 100, 100, 0)
        self.sbCycle = Gtk.SpinButton()
        self.sbCycle.set_adjustment(self.adjCycle)
        vBoxCycle.add(self.sbCycle)
        self.stack.add_titled(vBoxCycle, "cycle", "Cycle")

        ###BREATHE TAB

        vBoxBreathe = Gtk.Box(orientation=Gtk.Orientation.VERTICAL, spacing=5)
        breatheColorButton = Gtk.ColorButton()
        breatheColorButton.connect("color-set", self.color_set)
        vBoxBreathe.add(breatheColorButton)
        vBoxBreathe.add(self.sbCycle)
        self.adjBCycle = Gtk.Adjustment(5000, 500, 65535, 100, 100, 0)
        self.sbBCycle = Gtk.SpinButton()
        self.sbBCycle.set_adjustment(self.adjBCycle)
        vBoxBreathe.add(self.sbBCycle)
        self.stack.add_titled(vBoxBreathe, "breathe", "Breathe")

        ###STACK
        self.stack_switcher = Gtk.StackSwitcher()
        self.stack_switcher.set_stack(self.stack)
        vBoxMain.pack_start(self.stack_switcher, True, True, 0)
        vBoxMain.pack_start(self.stack, True, True, 0)

        ###OK BUTTON
        btnOk = Gtk.Button.new_with_label("OK")
        btnOk.connect("clicked", self.on_ok_button_clicked)
        vBoxMain.pack_start(btnOk, True, True, 0)

win = Window()
win.connect("delete-event", Gtk.main_quit)
win.show_all()
Gtk.main()
