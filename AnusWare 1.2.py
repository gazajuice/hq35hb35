from tkinter import *
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import subprocess
class Setpath():
    def __init__(self, filepath, url, opid):
        self.filepath = filepath
        self.url = url
        self.opid = opid
    def set1(self):
        global i
        i = 0
        self.window = Tk()
        self.window.title("AnusWare")
        self.window.geometry("500x700")
        def poop():
            global i
            self.filepath = self.textvar.get()
            i += 1
            self.label1 = Label(self.window, text=("File path Set: " + self.filepath), font=("Arial", 15))
            self.label1.pack()
            if i == 3:
                self.button3 = Button(self.window, text="GO", command=poop3, font=("Arial", 20))
                self.button3.pack()
            elif i > 3:
                i = 1
        def poop2():
            global i
            self.url = self.textvar2.get()
            i += 1
            self.label2 = Label(self.window, text=("URL Set: " + self.url), font=("Arial", 15))
            self.label2.pack()
            if i == 3:
                self.button3 = Button(self.window, text="GO", command=poop3, font=("Arial", 20))
                self.button3.pack()
            elif i > 3:
                i = 1
        def poop4():
            global i
            self.opid = self.textvar4.get()
            i += 1
            self.label3 = Label(self.window, text=("Option ID Set: " + self.opid), font=("Arial", 15))
            self.label3.pack()
            if i == 3:
                self.button3 = Button(self.window, text="GO", command=poop3, font=("Arial", 20))
                self.button3.pack()
            elif i > 3:
                i = 1
        def poop5():
            self.window.destroy()
            exit()
        def poop3():
            while True:
                self.p3 = subprocess.Popen(self.filepath)
                self.driver = Driver(uc=True)
                self.driver.get(self.url)
                self.p1 = self.driver.find_element(By.ID, self.opid)
                self.p1.click()
                self.p2 = WebDriverWait(self.driver, 100).until(
                    ec.presence_of_element_located(
                        (By.XPATH,
                         '//div[@class="strawpoll-vote-success-modal px-4 pt-5 pb-4 sm:p-6 rounded-md custom-box"]'))
                )
                self.p3.terminate()
                self.driver.quit()

        self.textvar = StringVar()
        self.text = Entry(self.window, textvariable=self.textvar, font=("Arial", 40))
        self.text.pack()
        self.button = Button(self.window, text="Set Path", command=poop, font=("Arial", 20))
        self.button.pack()
        self.textvar2 = StringVar()
        self.text2 = Entry(self.window, textvariable=self.textvar2, font=("Arial", 40))
        self.text2.pack()
        self.button2 = Button(self.window, text="Set URL", command=poop2, font=("Arial", 20))
        self.button2.pack()
        self.textvar4 = StringVar()
        self.text4 = Entry(self.window, textvariable=self.textvar4, font=("Arial", 40))
        self.text4.pack()
        self.button4 = Button(self.window, text="Set Option ID", command=poop4, font=("Arial", 20))
        self.button4.pack()
        self.button5 = Button(self.window, text="Quit", command=poop5, font=("Arial", 20))
        self.button5.pack()

        self.window.mainloop()
p = Setpath("", "", "")
p2 = p.set1()
