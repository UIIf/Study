import numpy as np
import matplotlib.pyplot as plt


class WIRiv:
    def __init__(self, W, I, R, i, v, g, mu, alpha, beta, h, max_interferon=1000):

        self.ceil_sum = W + I + R

        self.W = W / self.ceil_sum
        self.I = I / self.ceil_sum
        self.R = R / self.ceil_sum

        self.molec = max_interferon
        self.i = i / self.molec
        self.v = v / self.molec

        self.g_i = g["i"]
        self.g_v = g["v"]

        self.m_i = mu["i"]
        self.m_I = mu["I"]
        self.m_v = mu["v"]

        self.a_i = alpha["i"]
        self.a_v = alpha["v"]

        self.b_i = beta["i"]
        self.b_v = beta["v"]

        self.h = h

    def create_time_line(self, max_timer, step=1):

        W_line = []
        I_line = []
        R_line = []

        i_line = []
        v_line = []

        W = self.W
        I = self.I
        R = self.R

        i = self.i
        v = self.v

        for t in range(int(max_timer / self.h) + 1):

            if t % step == 0:
                W_line += [W]
                I_line += [I]
                R_line += [R]

                i_line += [i]
                v_line += [v]

            W, I, R, i, v = (
                W - self.a_i * i * W - self.a_v * v * W,
                I + self.a_v * v * W - self.m_I * I,
                R + self.a_i * i * W,
                i + self.g_i * I - self.b_i * i * W - self.m_i * i,
                v + self.g_v * I - self.b_v * v * W - self.m_v * v,
            )

        return (
            np.array(W_line) * self.ceil_sum,
            np.array(I_line) * self.ceil_sum,
            np.array(R_line) * self.ceil_sum,
            np.array(i_line) * self.molec,
            np.array(v_line) * self.molec,
        )

    def create_plot(self, max_timer, step):
        W_line, I_line, R_line, i_line, v_line = self.create_time_line(max_timer, step)

        steps = W_line.shape[0]
        x = range(steps)

        fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(16, 6))

        ax1.fill_between(x, [0] * steps, W_line, label="Подверженные заражению")
        ax1.fill_between(x, W_line, I_line + W_line, label="Зараженные")
        ax1.fill_between(
            x, W_line + I_line, W_line + I_line + R_line, label="Выздоровевшие"
        )

        ax1.legend()

        ax2.plot(x, i_line, label="Интерферон")
        ax2.plot(x, v_line, label="Вирион")

        ax2.legend()
        plt.show()


alpha = {"i": 0.02, "v": 0.02}

beta = {"i": 0.05, "v": 0.05}

g = {"i": 0.1, "v": 0.1}

mu = {"i": 0.05, "v": 0.05, "I": 0.005}

model = WIRiv(200, 50, 0, 25, 100, g, mu, alpha, beta, 1 / 60)

model.create_plot(24, 60)
