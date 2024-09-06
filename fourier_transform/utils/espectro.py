from scipy.fft import fft
from numpy import arange, floor, angle, pi
import matplotlib.pyplot as plt

def espectro1D(sinal, fs):
    fsinal = fft( sinal )
    
    N = sinal.size
    df = fs/N
    freq = arange(0,fs,df)
    
    #fig, axs = plt.subplots(2,1)
    # plt.figure(nfig)
    
    ax1 = plt.subplot(2,1,1)
    Ampl = 2*abs( fsinal[0:int(floor(N/2))] )/N
    Ampl[0] = Ampl[0] / 2; # correcao na amplitude da componente DC
    ax1.stem( freq[0:int(floor(N/2))], Ampl )
    ax1.set_ylabel( 'Amplitude' )
    #axs[0].set_xlabel( 'Freq. [Hz]' )
    ax1.axis([0,fs/2,0,1.1*max(Ampl)])
    ax1.grid(True)

    ax2 = plt.subplot(2,1,2)
    Fase = (angle( fsinal[0:int(floor(N/2))] ) )*180/pi
    ax2.stem( freq[0:int(floor(N/2))], Fase )
    ax2.set_ylabel( 'Fase [graus]' )
    ax2.set_xlabel( 'Freq. [Hz]' )
    ax2.axis([0,fs/2,1.1*min(Fase),1.1*max(Fase)])
    ax2.grid(True)

    plt.show()
