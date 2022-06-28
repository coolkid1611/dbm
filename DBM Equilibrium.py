#!/usr/bin/env python
# coding: utf-8

# In[4]:


from sympy import *
import scipy as sc
init_printing() # for pretty-printing equations etc
get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as p


# In[33]:


beta, b, c, r, K, omega, u_1, f, u_2, rho, gamma, phi, H, I, Z, N, t = var("beta, b, c, r, K, omega, u_1, f, u_2, rho, gamma, phi, H, I, Z, N, t",real = True)


# In[141]:


dH_dt = -beta*H*Z + b*I*N + c*I
dI_dt = beta*H*Z - b*I*N - c*I
dZ_dt = r*Z*(1-Z/K) - omega*Z*N - u_1*f*Z
dN_dt = u_2*rho + gamma*Z*N -phi*N

dH_dt, dI_dt, dZ_dt, dN_dt


# In[70]:


H_eqlb = Eq(dH_dt, 0)
I_eqlb = Eq(dI_dt, 0)
Z_eqlb = Eq(dZ_dt, 0)
N_eqlb = Eq(dN_dt, 0)


H_eqlb, I_eqlb, Z_eqlb, N_eqlb


# In[124]:


N1 = solve(Z_eqlb, N)
N2 = solve(N_eqlb, N)
N3 = (N1,N2)


N3 


# In[131]:


N4 = N4[0]

N4


# In[130]:


N5 = N5[0]

N5


# In[134]:


N4 = N3[0]
N4 = N4[0]

N4


# In[135]:


N5 = N3[1]
N5 = N5[0]

N5


# In[136]:


N6 = N4+N5

N6


# In[138]:


Z1 = Eq(N6, 0)

Z1


# In[140]:


Z2 = solve(Z1, Z)

Z2


# In[ ]:




