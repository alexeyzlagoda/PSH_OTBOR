import numpy as np
import scipy.integrate
#from tqdm import tqdm
from math import sin

def KuramotoOmega(phi, t, omega,  K):
    dphi_dt = omega + np.sin(phi) * (K @ np.cos(phi)) - np.cos(phi) * (K @ np.sin(phi))
    return dphi_dt


def Integrator(resolution, duration, omegas, phis, K):
    Time = np.linspace(0,duration, int(duration/resolution))
    Phi_t = scipy.integrate.odeint(KuramotoOmega, phis, Time, args=(omegas, K))
    Omega_t = np.array([KuramotoOmega(phi_t, 0, omegas, K) for phi_t in Phi_t])
    return Time, Phi_t.T, Omega_t.T

# resolution = 1e-4
# duration = 1
# omega = np.array([5.0,2.0])
# phi = np.array([np.pi,np.pi/2])
# k = np.array([[5,5],
#          [5,5]])

# print(KuramotoOmega(phi, 0, omega, k)[0])

        