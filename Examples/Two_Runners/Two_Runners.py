import matplotlib.pyplot as plt
import numpy as np


#Parameters:

def solver(phi_1, phi_2, omega_1, omega_2, k1,k2, iteration):
    Resolution = 10**(-4)
    Time = 2*10**(1)
    GraphRes = 1
    phi_1_data = []
    phi_2_data = []
    omega_1_data = []
    omega_2_data = []
    dots_num = int(Time/Resolution)

    for iteration in range(dots_num):
        phi_1 += (k1*np.sin(-(phi_2-phi_1))+ omega_1)*Resolution
        phi_2 += (k2*np.sin(-(phi_1-phi_2))+ omega_2)*Resolution
        phi_1_data.append(phi_1)
        phi_2_data.append(phi_2)
        omega_1_data.append((k1*np.sin(-(phi_2-phi_1))+ omega_1))
        omega_2_data.append(k2*np.sin(-(phi_1-phi_2))+ omega_2)
    T = np.linspace(0,Time, dots_num)
    plt.plot(T,omega_1_data, color = "red", label = "Omega 1")
    plt.plot(T,omega_2_data, color = "blue", label = "Omega 2")
    plt.title("Зависимость угловой скорости от времени")
    plt.legend()
    plt.savefig("D:\Интеллект\ПШ_ДЕМО\Examples\Two_Runners\Graphs\Omega_by_time_"+str(iteration) +".png")
    plt.show()
    plt.plot(T,phi_1_data, color = "red", label = "Phi 1")
    plt.plot(T,phi_2_data, color = "blue", label = "Phi 2")
    plt.title("Зависимость угла  от времени")
    plt.legend()
    plt.savefig("D:\Интеллект\ПШ_ДЕМО\Examples\Two_Runners\Graphs\Phi_by_time_"+str(iteration) +".png")
    plt.show()
solver()