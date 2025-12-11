import matplotlib.pyplot as plt
import numpy as np
feature_x=np.linspace(0,3,30)
feature_y=np.linspace(0,3,30) 
[X,Y]=np.meshgrid(feature_x,feature_y)
Z=X**2+Y**2
plt.contourf(X,Y,Z)
plt.xlabel('X-axis')
plt.ylabel('Y-label')
plt.title('Contour plot')
plt.show()