
#salvando os valores
#n=10**5
#k1:  t1= 0.042869 t2=0.020553
#k2:  t1= 0.053912 t2=0.023055
#k4:  t1= 0.066777 t2=0.023559
#k8:  t1= 0.074160 t2=0.025342
#k16: t1= 0.076031 t2=0.028028
#
#n=10**7
#k1:  t1=3.145584 t2=1.093375
#k2:  t1=3.217267 t2=1.096679
#k4:  t1=3.230374 t2=1.070671
#k8:  t1=3.167246 t2=1.120715
#k16: t1=3.269592 t2=1.236059

import matplotlib.pyplot as plt

k=[1,2,4,8,16]

#Para N=10**5
tc5 = [0.042869,0.053912,0.066777,0.074160,0.076031]
t5 = [0.020553,0.023055,0.023559,0.025342,0.028028]

#Para N=10**7
tc7 = [3.145584,3.217267,3.230374,3.167246,3.269592]
t7 = [1.093375,1.096679,1.070671,1.120715,1.236059]
    
#Não foi possível gerar dados pro N=10**9 por falta de capacidade de processamento.

fig = plt.figure(figsize=(11,10))


ax1 = fig.add_subplot(2,2,1)
ax1.plot(k,tc5,'r')
plt.scatter(k, tc5, color='red')
ax1.set_title('N=10**5,T=100 c/variável cumulativa')
ax1.set_ylabel('Tempo médio(t/T)')
ax1.set_xlabel('Threads(k)')

ax2 = fig.add_subplot(2,2,2)
ax2.plot(k,t5,'r')
plt.scatter(k, t5, color='red')
ax2.set_title('N=10**5, T=100')
ax2.set_ylabel('Tempo médio(t/T)')
ax2.set_xlabel('Threads(k)')

ax3 = fig.add_subplot(2,2,3)
ax3.plot(k,tc7,'r')
plt.scatter(k, tc7, color='red')
ax3.set_title('N=10**7,T=100 c/variável cumulativa')
ax3.set_ylabel('Tempo médio(t/T)')
ax3.set_xlabel('Threads(k)')

ax3 = fig.add_subplot(2,2,4)
ax3.plot(k,t7,'r')
plt.scatter(k, t7, color='red')
ax3.set_title('N=10**7, T=100')
ax3.set_ylabel('Tempo médio(t/T)')
ax3.set_xlabel('Threads(k)')


plt.show()