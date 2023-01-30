import numpy as np
import matplotlib.pyplot as plt


class SIR:
    def __init__(self, S, I, R, c, w, h):
        self.sum = S + I + R
        self.S, self.I, self.R = S/self.sum, I/self.sum, R/self.sum

        self.c, self.w = c/self.sum, w/self.sum

        self.h = h

    def create_time_line(self, max_timer, step = 1):

        S_line = []
        I_line = []
        R_line = []

        S, I, R = self.S, self.I, self.R

        for t in range(int(max_timer/self.h) + 1):
            
            if(t%step == 0):
                S_line += [S]
                I_line += [I]
                R_line += [R]


            S, I, R = (
                S - self.c * self.h * I * S,
                I + self.c * self.h * I * S - self.w*self.h*I,
                R + self.w*self.h*I
            )
            
        return (np.array(S_line) * self.sum, np.array(I_line)* self.sum, np.array(R_line)* self.sum)
            

    def create_plot(self, max_timer, step):
        S_list, I_list, R_list = self.create_time_line(max_timer, step)

        steps = S_list.shape[0]
        x = range(steps)

        plt.fill_between(x, [0]*steps, S_list, label = 'Подверженные заражению')
        plt.fill_between(x, S_list, I_list + S_list, label = 'Зараженные')
        plt.fill_between(x, S_list + I_list, S_list + I_list + R_list, label = 'Выздоровевшие')

        plt.xlabel('Часы')
        plt.ylabel('Особи')

        plt.legend()
        plt.show()
    

# SIR_100 = SIR(100, 100, 0, 40, 8, 1/60) # 1
SIR_100 = SIR(100, 100, 0, 15, 10, 1/60)
SIR_100.create_plot(24*7, 60)