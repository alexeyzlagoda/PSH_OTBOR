import numpy as np
import scipy.integrate

from math import sin

def Kuramoto(dt,omega,phi_0,  K_I:list, phi:list):
    summa = 0
    for i, ph in zip(K_I,phi):
        summa +=i*sin(ph-phi_0)
    return (omega + summa/(len(phi)+1))*dt



def KuramotoOmega(omega,phi_0,  K:list, phi:list):
    summa = 0
    for i,ph in zip(K,phi):
        summa +=i*sin(ph-phi_0)
    return (omega + summa/(len(phi)+1))





def Integrator(resolution, duration, omegas, phis, K):
    Phi_data = []
    Omega_data = []
    for iteration in range(int(duration/resolution)):
        Phi_data_i = []
        Omega_data_i = []
        Time = iteration*resolution
        for i, omega, thisK in zip(range(len(omegas)), omegas, K):
            if i == 0:
                Kuramoto_Phis = phis[1:]
            if i == len(omegas)-1:
                Kuramoto_Phis = phis[:i]
            else:
                Kuramoto_Phis = np.concatenate((phis[:i], phis[i+1:]))
            print(phis[i])
            phis[i] += scipy.integrate.quad(Kuramoto, Time-resolution, Time, args=(omega,phis[i], thisK,Kuramoto_Phis))[0]
            Phi_data_i.append(phis[i])
            Omega_data_i.append(KuramotoOmega(omega,phis[i], thisK,Kuramoto_Phis))
        Phi_data.append(Phi_data_i)
        Omega_data.append(Omega_data_i)
    TimeAxis = np.linspace(0,duration, int(duration/resolution))
    return TimeAxis,np.transpose(Phi_data), np.transpose(Omega_data)


    

        