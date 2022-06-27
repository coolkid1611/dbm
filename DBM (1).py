#!/usr/bin/env python
# coding: utf-8

# In[134]:


import scipy.integrate
import numpy
import matplotlib.pyplot as plt


# In[135]:


def SIZN_model(y, t, beta, b, c, r, K, m, alpha, d, s, phi, rho):
    S, I, Z, N = y
    
    dS_dt = -beta*S*Z + b*I*Z + c*I
    dI_dt = beta*S*Z - b*I*Z - c*I
    dZ_dt = r*Z - (r*Z*Z)/K - m*Z*N + alpha*S*Z - d*Z
    dN_dt = rho + s*Z*N - phi*N
    
    return([dS_dt, dI_dt, dZ_dt, dN_dt])


# In[147]:


S0 = 0.9999
I0 = 0.0001
Z0 = 1.2
N0 = 0.8
beta = 0.170
c = 0.5
b = 0.35
r = 0.026
m = 0.2
K = 15
alpha = 0.25
d = 0.9
s = 1.2 
rho = 1.2
phi = 0.6


t = numpy.linspace(0, 20, 100)

solution = scipy.integrate.odeint(SIZN_model, [S0,I0,Z0,N0], t, args=(beta, b, c, r, K, m, alpha, d, s, phi, rho))
solution = numpy.array(solution)


# In[148]:


plt.figure(figsize=[10, 8])
plt.plot(t, solution[:, 0], label="S(t)")
plt.plot(t, solution[:, 1], label="I(t)")
plt.plot(t, solution[:, 2], label="Z(t)")
plt.plot(t, solution[:, 3], label="N(t)")
plt.legend()
plt.xlabel("Time")
plt.ylabel("Proportions of Population")
plt.title("Model")
plt.show()


# In[149]:


solution.T[1]*10000


# In[150]:


solution.T[0]*10000


# In[151]:


S = solution.T[0]*10000
x = S[99]
print(x)


# In[153]:


I = solution.T[1]*10000
y = I[99]
print(y)


# In[ ]:




