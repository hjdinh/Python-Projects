import socket
import threading
import tkinter
import tkinter.scrolledtext
from tkinter import simpledialog

host = socket.gethostbyname(socket.gethostname())
port = 9090

class Client:
    def __init__(self, host, port):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)   # define socket
        self.sock.connect((host, port))     # connect to socket

        msg = tkinter.Tk()      # define message window to enter username
        msg.withdraw()      # hide window without destroying it internally

        self.username = simpledialog.askstring("Username", "Please choose a username", parent=msg)  # take username

        self.gui_done = False
        self.running = True

        gui_thread = threading.Thread(target=self.gui_loop)
        receive_thread = threading.Thread(target=self.receive)

        gui_thread.start()
        receive_thread.start()

    def gui_loop(self):     # define gui
        self.win = tkinter.Tk()
        self.win.configure(bg="lightgray")
        
        self.chat_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
        self.chat_label.config(font=("Arial", 12))
        self.chat_label.pack(padx=20, pady=5)

        self.text_area = tkinter.scrolledtext.ScrolledText(self.win)
        self.text_area.pack(padx=20, pady=5)
        self.text_area.config(state="disabled")

        self.msg_label = tkinter.Label(self.win, text="Chat:", bg="lightgray")
        self.msg_label.config(font=("Arial", 12))
        self.msg_label.pack(padx=20, pady=5)

        self.input_area = tkinter.Text(self.win, height=3)
        self.input_area.pack(padx=20, pady=5)
        self.input_area.focus()
        
        self.send_button = tkinter.Button(self.win, text="Send", command=self.write)
        self.send_button.config(font=("Arial", 12))
        self.send_button.pack(padx=20, pady=5)

        self.gui_done = True

        self.win.protocol("WM_DELETE_WINDOW", self.stop)    # call stop function when window is closed

        self.win.mainloop()

    def write(self):
        message = f"{self.username}: {self.input_area.get('1.0', 'end')}"       # retrieve message from input
        self.sock.send(message.encode("utf-8"))     # send message to server
        self.input_area.delete("1.0", "end")    # clear message field

    def stop(self):
        self.running = False
        self.win.destroy()      # destroy widget
        self.sock.close()       # close connection
        exit(0)

    def receive(self):
        while self.running:
            try:
                message = self.sock.recv(1024).decode("utf-8")
                if message == "USER":
                    self.sock.send(self.username.encode("utf-8"))   # send username to server
                else:
                    if self.gui_done:
                        self.text_area.config(state="normal")   # make text area editable
                        self.text_area.insert("end", message)   # insert message to text area
                        self.text_area.yview("end")             # always view end of text area
                        self.text_area.config(state="disabled")     # make text area uneditable
            except ConnectionAbortedError:
                break
            except:
                print("Error")
                self.sock.close()
                break

client = Client(host, port)