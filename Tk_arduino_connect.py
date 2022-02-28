from tkinter import Tk, Button, Label, BOTH, END, HORIZONTAL, Text
from tkinter.ttk import Combobox
from sys import platform
from glob import glob
from serial import Serial, SerialException

class Window(Tk):

    def __init__(self):
        Tk.__init__(self)
        self.title('Arduino')
        self.geometry(self.windows())

        self.speeds = ['1200', '2400', '4800', '9600', '19200', '38400', '57600', '115200']

        self.TextField = Text(self, width=15, height=1, state='disable')

        self.Read = Button(self, text='Прочитать', width=15, height=1, bg='lightgrey')
        self.Read.config(command=self.read)

        self.Blink = Button(self, text='Мигать', width=15, height=1, bg='lightgrey')
        self.Blink.config(command=self.blink)

        self.Light = Button(self, text="Гореть", width=15, height=1, bg='lightgrey')
        self.Light.config(command=self.light)

        self.Off = Button(self, text='Погасить', width=15, height=1, bg='lightgrey')
        self.Off.config(command=self.off)

        self.Conn = Button(self, text='Подключить', width=15, height=1, bg='lightgrey')
        self.Conn.config(command=self.connect)

        self.PortCmb = Combobox(self, width=20, values=self.serial_ports())

        self.PortLbl = Label(self, text="Порт")

        self.SpeedCmb = Combobox(self, width=20, values=self.speeds)
        self.SpeedLbl = Label(self, text="Скорость")

        self.PortLbl.pack()
        self.PortCmb.pack(pady=10)

        self.SpeedLbl.pack()
        self.SpeedCmb.pack(pady=10)

        self.TextField.pack(pady=5)
        self.Conn.pack(pady=5)
        self.Read.pack(pady=5)
        self.Blink.pack(pady=5)
        self.Light.pack(pady=5)
        self.Off.pack(pady=5)

        self.ser = None

    def windows(self):
        w = 300
        h = 350
        sw = self.winfo_screenwidth()
        sh = self.winfo_screenheight()
        x = (sw - w) / 2
        y = (sh - h) / 2
        return '%dx%d+%d+%d' % (w, h, x, y)


    def open_port(self, port, speed):
        self.ser = Serial(port, speed)
        print(self.ser)

    def blink(self):
       if self.ser is not None and self.ser.is_open:
            print(self.ser.write(100))
            self.Blink['relief'] = 'sunken'
            self.Blink['relief'] = 'raised'


    def light(self):
        if self.ser is not None and self.ser.is_open:
            print(self.ser.write(101))
            self.Light['relief'] = 'sunken'
            self.Light['relief'] = 'raised'


    def off(self):
        if self.ser is not None and self.ser.is_open:
            print(self.ser.write(102))
            self.Off['relief'] = 'sunken'
            self.Off['relief'] = 'raised'


    def connect(self):
        if self.Conn['text'] == 'Подключить' and self.PortCmb.get() and self.SpeedCmb.get():
            self.open_port(self.PortCmb.get(), self.SpeedCmb.get())
            self.Conn['text'] = 'Подключено'
            self.Conn['relief'] = 'sunken'
            self.Conn['bg'] = 'green'
        elif self.Conn['text'] == 'Подключено':
            self.ser.close()
            print(self.ser)
            self.Conn['text'] = 'Подключить'
            self.Conn['relief'] = 'raised'
            self.Conn['bg'] = 'lightgrey'


    def read(self):
        if self.ser is not None and self.ser.is_open:
            # self.text = self.ser.read()
            self.text = 'hello!'
            self.textfield(self.text)
            print(self.text)

    def textfield(self, text):
        self.TextField.configure(state='normal')
        self.TextField.insert(END, text)
        self.TextField.configure(state='disable')


    def serial_ports(self):
        """ Lists serial port names
            :raises EnvironmentError:
                On unsupported or unknown platforms
            :returns:
                A list of the serial ports available on the system
        """
        if platform.startswith('win'):
            ports = ['COM%s' % (i + 1) for i in range(256)]
        elif platform.startswith('linux') or platform.startswith('cygwin'):
            # this excludes your current terminal "/dev/tty"
            ports = glob('/dev/tty[A-Za-z]*')
        elif platform.startswith('darwin'):
            ports = glob('/dev/tty.*')
        else:
            raise EnvironmentError('Unsupported platform')

        result = []
        for port in ports:
            try:
                s = Serial(port)
                s.close()
                result.append(port)
            except (OSError, SerialException):
                pass
        return result

w = Window()
w.mainloop()



