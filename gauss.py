import tkinter as tk
import os

class GaussApp(tk.Frame):
    def __init__(self, parent, rank):
        tk.Frame.__init__(self, parent)
        self.rank = rank
        self.dict_var = {}
        self.text = ''
        self.matrix = []
        
        for row in range(rank):
            for column in range(rank + 1):
                index = (row, column)
                pole = tk.Entry(self, width=10, font='Arial 16')
                pole.grid(row=row, column=column, sticky=tk.E)
                self.dict_var[index] = pole

        
        butOne = tk.Button(self, text='Прямой ход', command=self.method1)
        butOne.grid(row=rank+2 , column=0, sticky=tk.E)

        butTwo = tk.Button(self, text='Обратный ход', command=self.method2)
        butTwo.grid(row=rank+2 , column=1, sticky=tk.E)
        
        butRead = tk.Button(self, text='Прочитать файл', command=self.readFile)
        butRead.grid(row=rank+2 , column=2, sticky=tk.E)


        self.text_tk = tk.Text(width=50, height=10)
        self.text_tk.pack()
        frame = tk.Frame()
        frame.pack()
        b_insert = tk.Button(frame, text="Решение", command=self.insertText)
        b_insert.pack(side=tk.LEFT)


    def makeMatrix(self):
        for i in range(self.rank):
            self.matrix.append([])
            for j in range(self.rank + 1):
                index = i,j              
                self.matrix[i].append(float(self.dict_var[index].get()))


    def insertText(self):
        self.text+="\n" + "Ответ " + self.answer() + "\n"
        self.text_tk.insert(1.0,self.text)


    def answer(self):
        try:
            s = ''
            for j in range(self.rank):
                s += str(round(self.matrix[j][-1],2)) + ' '
            return str(s)

        except IndexError:
            return 'Нет решений!'


    def insertMatrix(self):
         for i in range(self.rank):
            for j in range(self.rank + 1):
                index = i,j
                self.dict_var[index].delete(0, tk.END)
                self.dict_var[index].insert(0,str(self.matrix[i][j]))


    def solve(self):   
        for i in range(self.rank):
            for j in range(self.rank+1):
                self.text += str(self.matrix[i][j]) + " "
            self.text+="\n" 
        self.text += "------------------------------\n"


    def method1(self):
        self.makeMatrix()
        for i in range(self.rank):
            a = self.matrix[i]
            self.solve()
            
            for j in range(i + 1, self.rank):
                
                b = self.matrix[j]
                try:
                    m = a[i] / b[i]
                except:
                    pass
                line = []
                
                for k in range(len(a)):
                    line.append(a[k] - (b[k] * m))
                self.matrix[j] = line
        self.insertMatrix()


    def method2(self):
        self.makeMatrix()
        for i in range(self.rank - 1, -1, -1):
            self.solve()
            line = []
            for j in range(self.rank + 1):
                try:
                    line.append(self.matrix[i][j] / self.matrix[i][i])
                except:
                    pass
            self.matrix[i] = line
            a = self.matrix[i]

            for j in range(i - 1, -1, -1):
                b = self.matrix[j]
                try:
                    m = a[i] / b[i]
                except:
                    pass
                line = []
                for s in range(len(a)):
                    line.append(round((a[s] - b[s] * m),1))
                self.matrix[j] = line
        self.insertMatrix()


    def readFile(self):
        file = open((os.getcwd() + "/file.txt"), 'r')
        line = []
        for i in file.read():
            if i.isdigit():
                line.append(int(i))    

        self.matrix = []

        for i in range(self.rank):
            self.matrix.append([])
            for j in range(self.rank + 1):
                self.matrix[i].append(line[j])
            line = line[self.rank+1:]
        self.insertMatrix()


if __name__ == "__main__":
    def show_message():
        global rank
        rank = int(x.get())
        rang.destroy()


    rang = tk.Tk()
    rang.title("Ранг матрицы")
    x = tk.Entry(rang, width=10, font='Arial 16')
    x.grid(row=0, column=0, sticky=tk.E)
    xB = tk.Button(rang, text='ввод', command=show_message)
    xB.grid(row=1, column=0, sticky=tk.E)
    rang.mainloop()

    app = tk.Tk()
    app.title("Метод Гаусса")
    GaussApp(app, rank).pack()
    app.mainloop()