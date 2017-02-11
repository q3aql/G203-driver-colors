#!/usr/bin/env python

import G213Colors
import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk
from time import sleep
NAME = "G213 Colors"


class Window(Gtk.Window):

    def btnGetHex(self, btn):
        color = btn.get_rgba()
        red = int(color.red * 255)
        green = int(color.green * 255)
        blue = int(color.blue * 255)
        hexColor = "%02x%02x%02x" % (red, green, blue)
        return hexColor

    def sbGetValue(self, sb):
        return sb.get_value_as_int()

    def sendStatic(self):
        myG = G213Colors
        myG.connectG()
        myG.sendColorCommand(self.btnGetHex(self.staticColorButton))
        myG.disconnectG()

    def sendBreathe(self):
        myG = G213Colors
        myG.connectG()
        myG.sendBreatheCommand(self.btnGetHex(self.breatheColorButton), self.sbGetValue(self.sbBCycle))
        myG.disconnectG()

    def sendCycle(self):
        myG = G213Colors
        myG.connectG()
        myG.sendCycleCommand(self.sbGetValue(self.sbCycle))
        myG.disconnectG()

    def sendSegments(self):
        myG = G213Colors
        myG.connectG()
        for i in range(1, 6):
            print(i)
            print(self.btnGetHex(self.segmentColorBtns[i-1]))
            myG.sendColorCommand(self.btnGetHex(self.segmentColorBtns[i -1]), i)
            sleep(0.01)
        myG.disconnectG()

    def color_set_segments(self, colorbutton):
        global hexColorSegments
        i = 0
        for btn in self.segmentColorButtons:
            colors = btn.get_rgba()
            red = int(color.red * 255)
            green = int(color.green * 255)
            blue = int(color.blue * 255)
            hexColorSegments[i] = "%02x%02x%02x" % (red, green, blue)

    def sendManager(self):
        self.stackName = self.stack.get_visible_child_name()
        if self.stackName == "static":
            self.sendStatic()
        elif self.stackName == "cycle":
            self.sendCycle()
        elif self.stackName == "breathe":
            self.sendBreathe()
        elif self.stackName == "segments":
            self.sendSegments()

    def on_ok_button_clicked(self, button):
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
        self.staticColorButton = Gtk.ColorButton()
        vBoxStatic.add(self.staticColorButton)

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
        self.breatheColorButton = Gtk.ColorButton()
        vBoxBreathe.add(self.breatheColorButton)
        self.adjBCycle = Gtk.Adjustment(5000, 500, 65535, 100, 100, 0)
        self.sbBCycle = Gtk.SpinButton()
        self.sbBCycle.set_adjustment(self.adjBCycle)
        vBoxBreathe.add(self.sbBCycle)
        self.stack.add_titled(vBoxBreathe, "breathe", "Breathe")

        ###SEGMENTS TAB
        hBoxSegments = Gtk.Box(spacing=5)
        self.segmentColorBtns = [Gtk.ColorButton() for _ in range(5)]
        for btn in self.segmentColorBtns:
            hBoxSegments.pack_start(btn, True, True, 0)
        self.stack.add_titled(hBoxSegments, "segments", "Segments")

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
