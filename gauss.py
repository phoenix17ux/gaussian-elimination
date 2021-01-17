import os, sys
import tkinter as tk

class Matrix:

    def __init__(self):
        self.matrix = []
        self.rank = 0

    def gauss_method(self):
        for i in range(self.rank):
            a = self.matrix[i]
            
            for j in range(i + 1, self.rank):
                b = self.matrix[j]
                try:
                    m = a[i] / b[i]
                except:
                    pass
                row_list = []
                
                for k in range(len(a)):
                    row_list.append(a[k] - (b[k] * m))
                self.matrix[j] = row_list

    def method_gauss_jordan(self):
        for i in range(self.rank - 1, -1, -1):
            
            row_list = []

            for j in range(self.rank + 1):
                try:
                    row_list.append(self.matrix[i][j] / self.matrix[i][i])
                except:
                    pass
            self.matrix[i] = row_list
            a = self.matrix[i]

            for j in range(i - 1, -1, -1):
                b = self.matrix[j]
                try:
                    m = a[i] / b[i]
                except:
                    pass
                row_list = []

                for s in range(len(a)):
                    row_list.append(round((a[s] - b[s] * m), 1))
                self.matrix[j] = row_list

class GaussApp(tk.Frame):
    def __init__(self, parent):
        tk.Frame.__init__(self, parent)
        self.dict_var = {}
        self.text = ''
        self.matrix = Matrix()
        
        self.butRead = tk.Button(self, text='Прочитать файл', command=self.readFile)
        self.butRead.grid(row=0 , column=2, sticky=tk.E)
        self.insertRank = tk.Entry(self, width=10, font='Arial 16')
        self.insertRank.grid(row=0, column=0, sticky=tk.E)
        self.butRank = tk.Button(self, text='Ввести ранг', command=self.choiceRank)
        self.butRank.grid(row=0, column=1, sticky=tk.E)


    def createMatrix(self):    
        for i in range(self.matrix.rank):
            for j in range(self.matrix.rank + 1):
                index = i, j
                pole = tk.Entry(self, width=10, font='Arial 16')
                pole.grid(row=i, column=j, sticky=tk.W)
                self.dict_var[index] = pole

        
    def getMatrix(self):
        for i in range(self.matrix.rank):
            self.matrix.matrix.append([])
            for j in range(self.matrix.rank + 1):
                index = i,j              
                self.matrix.matrix[i].append(float(self.dict_var[index].get()))


    def insertText(self):
        self.text+="\n" + "Ответ: " + self.answer() + "\n"
        self.text_tk.insert(1.0,self.text)


    def answer(self):
        try:
            s = ''
            for j in range(self.matrix.rank):
                s += str(round(self.matrix.matrix[j][-1],2)) + ' '
            return str(s)

        except IndexError:
            return 'Нет решений!'


    def insertMatrix(self):
         for i in range(self.matrix.rank):
            for j in range(self.matrix.rank + 1):
                index = i,j
                self.dict_var[index].delete(0, tk.END)
                self.dict_var[index].insert(0,str(self.matrix.matrix[i][j]))


    def solve(self):   
        for i in range(self.matrix.rank):
            for j in range(self.matrix.rank+1):
                self.text += str(self.matrix.matrix[i][j]) + " "
            self.text+="\n" 
        self.text += "------------------------------\n"


    def panel(self):
        butOne = tk.Button(self, text='Прямой ход', command=self.method1)
        butOne.grid(row=self.matrix.rank+1 , column=0, sticky=tk.W)

        butTwo = tk.Button(self, text='Обратный ход', command=self.method2)
        butTwo.grid(row=self.matrix.rank+1 , column=1, sticky=tk.W)
        
        self.text_tk = tk.Text(width=50, height=10)
        self.text_tk.pack()
        
        frame = tk.Frame()
        frame.pack()
        b_insert = tk.Button(self, text="Решение", command=self.insertText)
        b_insert.grid(row=self.matrix.rank+1 , column=2, sticky=tk.W)
    

    def method1(self):
        self.getMatrix()
        self.matrix.gauss_method() 
        self.solve()
        self.insertMatrix()


    def method2(self):
        self.getMatrix()
        self.matrix.method_gauss_jordan()
        self.solve()
        self.insertMatrix()


    def choiceRank(self):
        self.matrix.rank = int(self.insertRank.get())
        self.butRead.destroy()
        self.insertRank.destroy()
        self.butRank.destroy()

        self.panel()
        self.createMatrix()


    def readFile(self):
        if sys.platform[:3] == "win":
            file = open(os.getcwd() + "\\file.txt", 'r')
        else:
            file = open(os.getcwd() + "/file.txt", 'r')
        file_list = []
        for i in file.read():
            if i.isdigit():
                file_list.append(int(i)) 
            else:
                self.matrix.rank +=1   

        for i in range(self.matrix.rank):
            self.matrix.matrix.append([])
            for j in range(self.matrix.rank + 1):
                self.matrix.matrix[i].append(file_list[j])
            file_list = file_list[self.matrix.rank+1:]
        self.createMatrix()
        self.insertMatrix()
        self.panel()



if __name__ == "__main__":

    app = tk.Tk()
    app.title("Gaussian-Elimination")
    GaussApp(app).pack()
    app.mainloop()
