import matplotlib.pyplot as plt
import numpy as np
import solver
def main():
    ### Ну тут чето надо написать, но я хз пока что...
    resolution = 10**(-2)
    duration = 10**(0)*2
    omegas = [10.0,10.0]
    phis = [np.pi, np.pi*0.75]
    k_arr = [[0, 10],
             [15, 0]]
    TimeAxis, Phi_Axis, Omega_Axis = solver.Integrator(resolution, duration, omegas, phis, k_arr)
    Omega_Axis = (Omega_Axis)
    Phi_Axis = (Phi_Axis)
    
    plt.plot(TimeAxis,(Omega_Axis)[0], color = "red", label = "Omega 1")
    plt.plot(TimeAxis,(Omega_Axis)[1], color = "blue", label = "Omega 2")
    plt.title("Зависимость угловой скорости от времени")
    plt.legend()
    plt.show()

    plt.plot(TimeAxis,(Phi_Axis)[0], color = "red", label = "Phi 1")
    plt.plot(TimeAxis,(Phi_Axis)[1], color = "blue", label = "Phi 2")
    plt.title("Зависимость угла  от времени")
    plt.legend()
    plt.show()
main()