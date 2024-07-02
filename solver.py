import numpy as np
import scipy.integrate

def Kuramoto(dt,omega,phi_0,  K_I:list, phi:list):
    summa = 0
    for i, ph in zip(K_I,phi):
        summa +=i*(ph-phi_0)
    return (omega + summa/len(phi))*dt
def KuramotoOmega(omega,phi_0,  K:list, phi:list):
    summa = 0
    for i,ph in zip(K,phi):
        summa +=i*(ph-phi_0)
    return (omega + summa/len(phi))
def Integrator(resolution, time, omegas, phis, K):
    phi_data = []
    omega_data = []
    this_Time = 0
    TimeAxis = np.linspace(0, int(time), int(time/resolution)+1)
    while (this_Time<=time):
        print("Working...")
        phi_data_i = []
        omega_data_i = []
        for i,omega, phi, _k in zip(range(len(omegas)),omegas, phis, K):
            if i == 0:
                new_phis = phis[1:]
            elif i != len(phis)-1:
                new_phis = np.concatenate((phis[:i], phis[i+1:])) 
            else:
                new_phis = phis[:i]
            phis[i] += scipy.integrate.quad(Kuramoto, this_Time, this_Time + resolution, args=(omega, phi,K[i], new_phis))[0]
            phi_data_i.append(phi)
            omega_data_i.append(KuramotoOmega(omega, phi, _k, new_phis))
        phi_data.append(phi_data_i)
        omega_data.append(omega_data_i)
        this_Time +=resolution
    return TimeAxis,np.transpose(phi_data),np.transpose(omega_data)

        