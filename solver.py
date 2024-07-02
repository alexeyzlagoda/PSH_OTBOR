import numpy as np
import scipy.integrate
from math import sin

def Kuramoto(dt,omega,phi_0,  K_I:list, phi:list):
    summa = 0
    for i, ph in zip(K_I,phi):
        summa +=i*sin((ph-phi_0))
    return (omega + summa/(len(phi)+1))*dt
def KuramotoOmega(omega,phi_0,  K:list, phi:list):
    summa = 0
    for i,ph in zip(K,phi):
        summa +=i*sin((ph-phi_0))
    return (omega + summa/(len(phi)+1))
def Integrator(resolution, time, omegas, phis, K):
    print(omegas)
    print(phis)
    print(K)
    phi_data = []
    omega_data = []
    TimeAxis = np.linspace(0, int(time), int(time/resolution))
    for tTime in range(0,int(time/resolution)):
        this_Time = tTime*resolution
        phi_data_i = []
        omega_data_i = []
        for i,omega, phi, _k in zip(range(len(omegas)),omegas, phis, K):
            print(this_Time, i, omega, phi, _k)
            if i == 0:
                new_phis = phis[1:]
            elif i != len(phis)-1:
                new_phis = np.concatenate((phis[:i], phis[i+1:])) 
            else:
                new_phis = phis[:i]
            phis[i] += scipy.integrate.quad(Kuramoto, 0, this_Time, args=(omega, phi,K[i], new_phis))[0]
            phi_data_i.append(phis[i])
            omega_data_i.append(KuramotoOmega(omega, phi, _k, new_phis))
        phi_data.append(phi_data_i)
        omega_data.append(omega_data_i)
    return TimeAxis,np.transpose(phi_data),np.transpose(omega_data)

        