from tkinter import *
from seleniumbase import Driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
import time
import os
import signal
import subprocess

class Setpath():
    def __init__(self, filepath, url, opid):
        self.filepath = filepath
        self.url = url
        self.opid = opid
    def set1(self):
        self.window = Tk()
        def poop():
            self.filepath = self.textvar.get()
            print(self.filepath)
        def poop2():
            self.url = self.textvar2.get()
            print(self.url)
        def poop4():
            self.opid = self.textvar4.get()
            print(self.opid)
        def poop3():
            self.window.destroy()
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
        self.text = Entry(self.window, textvariable=self.textvar, font=("Arial", 20))
        self.text.pack()
        self.button = Button(self.window, text="Set Path", command=poop)
        self.button.pack()
        self.textvar2 = StringVar()
        self.text2 = Entry(self.window, textvariable=self.textvar2, font=("Arial", 20))
        self.text2.pack()
        self.button2 = Button(self.window, text="Set URL", command=poop2)
        self.button2.pack()
        self.textvar4 = StringVar()
        self.text4 = Entry(self.window, textvariable=self.textvar4, font=("Arial", 20))
        self.text4.pack()
        self.button4 = Button(self.window, text="Set Option ID", command=poop4)
        self.button4.pack()
        self.button3 = Button(self.window, text="GO", command=poop3)
        self.button3.pack()

        self.window.mainloop()
p = Setpath("", "", "")
p2 = p.set1()
