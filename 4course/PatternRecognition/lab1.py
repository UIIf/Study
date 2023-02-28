#VAR 5
# M1 = [0, 0]
# M2 = [1, 1]
# M3 = [-1, 1]

# X = A*eps + M

import numpy as np
import matplotlib.pyplot as plt

N = 200
dims = 2

M1 = np.array([0, 0])
M2 = np.array([1, 1])
M3 = np.array([-1, 1])

B_diag_symm = np.array([
        [0.1, 0],
        [0, 0.1]
    ])

B_diag_asymm = np.array([
    [0.01, 0],
    [0, 0.06]
])

def diag_flip(matrix):
    m = matrix.copy()
    m[0][0], m[1][1] = m[1][1], m[0][0]
    return m

eps = np.random.randn(N, dims)

def create_a(B):
    a = np.zeros([dims, dims])
    a[0][0] = np.sqrt(B[0][0])
    
    a[1][0] = B[0][1]/np.sqrt(B[0][0])

    a[1][1] = np.sqrt(B[1][1] - a[1][0]**2)
    return a

def calc_p_b(M1, M2, B1, B2):
    b_sum = (B2 + B1)/2
    inv_b_sum = np.linalg.inv(b_sum)
    m_diff = (M2 - M1)
    return np.dot(
            np.dot(
                m_diff.T,
                inv_b_sum
            ),
            m_diff
        )/4 +\
        np.log(
            np.linalg.det(b_sum)/
                np.sqrt(np.linalg.det(B1) * np.linalg.det(B2))
        )/2

def calc_p_m(M1, M2, B1, B2):
    ...

def create_plot(ax, x):
    ax.scatter(x[:, 0], x[:, 1])

def calc_x(eps, M, B):
    a = create_a(B)
    return np.dot(eps, a) + M
# print(calc_p_b(M1, M2, B_symm, B_symm))


fig, axs = plt.subplots(2,2)

fig.set_figheight(10)
fig.set_figwidth(16) 


# Симметричная матрица B
x_0_1 = calc_x(eps, M1, B_diag_symm)
x_0_2 = calc_x(eps, M2, B_diag_symm)


create_plot(axs[0,0], x_0_1)
create_plot(axs[0,0], x_0_2)

pb = calc_p_b(M1, M2, B_diag_symm, B_diag_symm)

axs[0,0].text(0.95, 0.01, f'Pb = {pb}',
        verticalalignment='bottom', horizontalalignment='right',
        transform=axs[0,0].transAxes,
        color='black', fontsize=15)

plt.show()

# x2 = calc_x(eps, M2, B_diag_asymm)

# x3 = calc_x(eps, M3, B_diag_asymm)

# x4 = calc_x(eps, M1, diag_flip(B_diag_asymm))

# x5 = calc_x(eps, M2, diag_flip(B_diag_asymm))

# x6 = calc_x(eps, M3, diag_flip(B_diag_asymm))
