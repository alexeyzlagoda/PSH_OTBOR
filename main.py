import matplotlib.pyplot as plt
import numpy as np
import solver
def main():
    ### Ну тут чето надо написать, но я хз пока что...
    resolution = 10**(-4)
    duration = 10**(1)*2
    omegas = [5.0,2.0]
    phis = [np.pi,0]
    k_arr = [[5,5],
             [5,5]]
        
    TimeAxis, Phi_Axis, Omega_Axis = solver.Integrator(resolution, duration, omegas, phis, k_arr)
    Omega_Axis = (Omega_Axis)
    Phi_Axis = (Phi_Axis)
    Phi_Axis = np.sin(Phi_Axis)
    plt.plot(TimeAxis,(Omega_Axis)[0], color = "red", label = "Omega 1")
    plt.plot(TimeAxis,(Omega_Axis)[1], color = "blue", label = "Omega 2")
    '''
    plt.plot(TimeAxis,(Omega_Axis)[2], color = "black", label = "Omega 3")
    plt.plot(TimeAxis,(Omega_Axis)[3], color = "orange", label = "Omega 4")
    plt.plot(TimeAxis,(Omega_Axis)[4], color = "purple", label = "Omega 5")
    plt.plot(TimeAxis,(Omega_Axis)[5], color = "yellow", label = "Omega 6")
    plt.plot(TimeAxis,(Omega_Axis)[6], color = "green", label = "Omega 7")
    '''
    plt.title("Зависимость угловой скорости от времени")
    plt.legend()
    plt.show()

    plt.plot(TimeAxis,(Phi_Axis)[0], color = "red", label = "Phi 1")
    plt.plot(TimeAxis,(Phi_Axis)[1], color = "blue", label = "Phi 2")
    '''
    plt.plot(TimeAxis,(Phi_Axis)[2], color = "black", label = "Phi 3")
    plt.plot(TimeAxis,(Phi_Axis)[3], color = "orange", label = "Phi 4")
    plt.plot(TimeAxis,(Phi_Axis)[4], color = "purple", label = "Phi 5")
    plt.plot(TimeAxis,(Phi_Axis)[5], color = "yellow", label = "Phi 6")
    plt.plot(TimeAxis,(Phi_Axis)[6], color = "green", label = "Phi 7")
    '''
    plt.title("Зависимость угла  от времени")
    plt.legend()
    plt.show()
main()