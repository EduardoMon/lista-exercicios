import numpy as np
import matplotlib.pyplot as pl

X=np.linspace(0,10,11)
Y=np.arange(11)
soma=X+Y
print('lista X:')
print(X)
print('lista Y:')
print(Y)
print('soma:')
print(soma)
pl.ion()
pl.plot(soma)

pl.xlabel('eixo X')
pl.ylabel('eixo Y')
pl.title('Gráfico')
pl.axis([-1,11,-1,21])
pl.grid()
