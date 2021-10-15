# this module will be imported in the into your flowgraph
import numpy as np
import math

def nyq(Sps,ntaps):
    k=np.linspace(-ntaps/2, ntaps/2-1, ntaps)
    h=np.sinc(k/Sps)
    return h
    
#######################################################
##                  Delta                            ##
#######################################################                       
def delta(ntaps):
    cerosd=(   [0]*(int(ntaps/2)-1)    )
    cerosdi=(   [0]*(int(ntaps/2))     )
    delta_i= np.concatenate(( cerosdi, ([1]) ))
    delta=np.concatenate(( delta_i, cerosd ))
    return delta
   
#######################################################
##               Forma Coseno Alzado                 ##
#######################################################                       
def rcos(Sps,ntaps,beta):
    if beta==0:
        h=nyq(Sps,ntaps)
    else:
        h=ntaps*[0,]
        for n in range(ntaps):
            k=n-ntaps/2. # esto es para que h[n] quede centrada en la mitad del vector
            if abs(k)==Sps/(2.*beta):
                h[n]=np.sinc(1./(2.*beta))*math.pi/4.
            else:
                h[n]=np.sinc(k/Sps)*math.cos(beta*k*math.pi/Sps)/(1.-(2.*beta*k/Sps)**2)                
    Amp=np.amax(h)
    return h/Amp
    
#######################################################
##            Forma Raiz de Coseno Alzado            ##
#######################################################                       

def rrcos(Sps,ntaps,beta):
    if beta==0:
        h=nyq(Sps,ntaps)
    else:
        h=ntaps*[0,]
        beta4=4.*beta
        for n in range(ntaps):
            k=n-ntaps/2. # esto es para que h[n] quede centrada en la mitad del vector
            if k==0:
                h[n]=1+beta*(4./math.pi-1.)
            elif abs(k)==Sps/beta4:
                ha=(1.+2./math.pi)*math.sin(math.pi/beta4)
                hb=(1.-2./math.pi)*math.cos(math.pi/beta4)
                h[n]=(ha+hb)*beta/math.sqrt(2.)
            else:
                ks=k/Sps
                kspi=math.pi*ks
                Num=math.sin(kspi*(1-beta))+beta4*ks*math.cos(kspi*(1+beta))
                Den=kspi*(1.-(beta4*ks)**2)
                h[n]=Num/Den                
    Amp=np.amax(h)
    return h/Amp

