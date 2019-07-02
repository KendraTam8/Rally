#importing 
from Tkinter import *
import random

###CHECKKKKK NUMBERRRRR
check = 1

distance = []
speed = 0
startTime = ""
calcDistArr = []
actDistArr = []
calbArr = []
gapArr = []
durationArr = []
timeArr = []
totalArr = []
entryArr = []

class MainGUI():
    def __init__(self, master):
        global distance
        global speed
        global check
        global startTime
        global calcDistArr
        global calbArr
        global actDistArr
        global gapArr
        global durationArr
        global totalArr
        global timeArr
        global entryArr
        
        self.master = master;
        self.master.title("Rally")
        self.master.geometry("1200x550")
        
        #Update BTN
        self.updateBTN = Button(self.master, text = "Update", font = ("Helvetica",15), command = lambda: self.update())
        self.updateBTN.pack()#place(x = 1125, y = 510)
        
        #Checkpoint LBL
        self.checkLBL = Label(master, text = "Going to Checkpoint " + str(check), font = ("Helvetica",12))
        self.checkLBL.place(x = 0, y = 10)
        
        #Speed
        self.speedLBL = Label(master, text = str(int(speed)) + " kph", font = ("Helvetica",12))
        self.speedLBL.place(x = 400, y = 10)
        
        #Start Time
        self.startTimeLBL = Label(self.master, text = "Start Time: " + startTime, font = ("Helvetica",13))
        self.startTimeLBL.place(x = 700, y = 10)
        
        self.startTimeEntry = Entry(self.master, font = ("Helvetica",12))
        self.startTimeEntry.place(x = 900, y = 10)
        
        #Distance LBL
        self.distHead = Label(master, text = "Dist", font = ("Helvetica",12))
        self.distHead.place(x = 0, y = 50)
        for i in range(0,len(distance)):
            self.distLBL = Label(master, text = distance[i], font = ("Helvetica",12))
            self.distLBL.place(x = 0, y = 75 + i* 25)
        
        #Supposed Car Distance LBL
        self.carDistHead = Label(master, text = "Calc Dist", font = ("Helvetica",12))
        self.carDistHead.place(x = 70, y = 50)
        
        for i in range(0,len(calcDistArr)):
            self.calcLBL = Label(master, text = calcDistArr[i], font = ("Helvetica",12))
            self.calcLBL.place(x = 70, y = 75 + i* 25)
        
        
        #Calibrated
        self.calibrateHead = Label(master, text = "Calibrated", font = ("Helvetica",12))
        self.calibrateHead.place(x = 200, y = 50)
        
        for i in range(0,len(calcDistArr)):
            self.calbLBL = Label(master, text = calbArr[i], font = ("Helvetica",12))
            self.calbLBL.place(x = 200, y = 75 + i* 25)
        
        
        
        
        #Actual Distance INPUT
        self.ActDistHead = Label(master, text = "Actual Dist", font = ("Helvetica",12))
        self.ActDistHead.place(x = 400, y = 50)
        #LBL
        for i in range(0,len(actDistArr)):
            self.durLBL = Label(master, text = actDistArr[i], font = ("Helvetica",12))
            self.durLBL.place(x = 400, y = 75 + i* 25)
        #ENTRY
        entryArr = []
        for i in range(0,len(actDistArr)):
            self.durLBL = Entry(master, font = ("Helvetica",12), width = 8)
            self.durLBL.place(x = 470, y = 75 + i* 25)
            entryArr.append(self.durLBL)
        
        #Gap LBL
        self.gapHead = Label(master, text = "Gap", font = ("Helvetica",12))
        self.gapHead.place(x = 600, y = 50)
        
        for i in range(0,len(gapArr)):
            self.durLBL = Label(master, text = gapArr[i], font = ("Helvetica",12))
            self.durLBL.place(x = 600, y = 75 + i* 25)
        
        #Duration LBL
        self.durationHead = Label(master, text = "Duration", font = ("Helvetica",12))
        self.durationHead.place(x = 740, y = 50)
        
        for i in range(0,len(durationArr)):
            self.durLBL = Label(master, text = durationArr[i], font = ("Helvetica",12))
            self.durLBL.place(x = 740, y = 75 + i* 25)
            
    
        #Total Time LBL
        self.totalHead = Label(master, text = "Total Duration", font = ("Helvetica",12))
        self.totalHead.place(x = 950, y = 50)
        
        for i in range(0,len(totalArr)):
            self.totalLBL = Label(master, text = totalArr[i], font = ("Helvetica",12))
            self.totalLBL.place(x = 950, y = 75 + i* 25)
        
        #Time LBL
        self.timeHead = Label(master, text = "Time", font = ("Helvetica",12))
        self.timeHead.place(x = 1140, y = 50)
        
        for i in range(0,len(timeArr)):
            self.timeLBL = Label(master, text = timeArr[i], font = ("Helvetica",12))
            self.timeLBL.place(x = 1140, y = 75 + i* 25)
        
        
        
    def update(self):
        global distance
        global speed
        global check
        global startTime
        global calcDistArr
        global calbArr
        global actDistArr
        global gapArr
        global durationArr
        global totalArr
        global timeArr
        global entryArr
        
        #calc distance
        prevGap = 0
        for i in range(0,len(distance)):
            if prevGap != 0:
                calcDistArr[i] = round(distance[i] + prevGap,4)
            prevGap = gapArr[i]
        
        
        #calbrated
        for i in range(0,len(distance)-1):
            if gapArr[i] != 0 and distance[i] != 0:
                calbArr[i+1] = round(actDistArr[i] / distance[i] * distance[i+1],4)
            prevDist = distance[i]
        
        
        
        #acutal distance
        for i in range(0,len(distance)):
            if entryArr[i].get() != "":
                actDistArr[i] = float(entryArr[i].get())
        
        #gap
        for i in range(0,len(gapArr)):
            if actDistArr[i] != 0:
                gapArr[i] = round(actDistArr[i] - distance[i],4)
        
        
        #duration + total
        getTime = self.startTimeEntry.get()
        if getTime != "":
            prevDist = 0
            for i in range(0,len(distance)):
                #each
                duration = (distance[i] - prevDist) / float(speed) * 60
                minute = int(duration)
                sec = int((duration - minute) * 60)
                
                durationStr = str(minute) + " mins " + str(sec) + " secs"
                durationArr.append(durationStr)
                prevDist = distance[i]
                
                #total
                durationT = distance[i]/ float(speed) * 60
                minuteT = int(durationT)
                secT = int((durationT - minuteT) * 60)
                
                totalStr = str(minuteT) + " mins " + str(secT) + " secs"
                totalArr.append(totalStr)
      
        
            #time
            startTime = getTime
            
            splitTime = startTime.split(':')
            hour = int(splitTime[0])
            mins = int(splitTime[1])
            
            for i in range(0,len(distance)):
                hour = int(splitTime[0])
                mins = int(splitTime[1])
                
                time = int(distance[i] / float(speed) * 60)
                mins += time
                
                if mins >= 60:
                    hour += 1
                    mins = mins-60
                
                minss = mins
                
                if mins < 10:
                    minss = "0" + str(mins)
                
                
                
                timeStr = str(hour) + ":" + str(minss)
                timeArr.append(timeStr)
        
        #write files
        writeFile = "Check Data " + str(check) + ".txt"
        w = open(writeFile,'w')
        
        for i in range(0,len(actDistArr)):
            w.writelines(str(actDistArr[i])+"\n")
        
        w.close()
        
        #removing the current screen
        self.master.withdraw()
        
        #the new window is the "first priority"
        newWindow = Toplevel(self.master)
        #set the new window to the score page
        root = MainGUI(newWindow)

        
def main():
    global distance
    global speed
    global check
    global startTime
    global calcDistArr
    global actDistArr
    global durationArr
    global gapArr
    global totalArr
    global timeArr
    global entryArr
        
    #open file
    filename = "data.txt"
    f = open(filename)
    
    speed = f.readline()
    line = f.readline()
    
    #find number of checkpoints
    while line != "end\n":
        distance.append(float(line))
        actDistArr.append(0)
        gapArr.append(0)
        calcDistArr.append(0)
        calbArr.append(0)
        line = f.readline()
        if line == "\n" or line == "":
            break
        
        
    f.close()
    #runner
    #creates root object
    root = Tk()
    #makes the window
    my_gui = MainGUI(root)
    #creates the window on the screen
    root.mainloop()
    
main()