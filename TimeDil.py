################################################################################################################################################################

#                                                                             Time Dilation
#                                                                           By : Andrew Dotson

################################################################################################################################################################
import math
import numpy as np
import matplotlib.pyplot as plt
c =  3.0e8
xval = np.linspace(0,c-0.0001,100000) #equally spaces x values that you're going to evaluate the functiona at and then plot
yval = [] # a list to store the corresponding yvalue which is just the factor that time is dilated
xlist = np.linspace(-10,110,100000)

def f(v):
    gamma = 1/(1-(v/c)**2.0)**(1/2.0) #definition of gamma
    return gamma


################################################################################################################################################################

#                                                                           Velocity that would Give that Gamma

################################################################################################################################################################
def velocity(gamma):
    v = c*(1 - (1 / gamma**2.0))**(1/2.0)
    return v /c*100.0, v # returning two values so that I can get both the percent of c as well as the actual velocity

for i in xval:
    dilation = f(i)
    yval.append(dilation)

gamma = float(input('Enter what factor you want time stretched by: ')) 


if gamma <= 1:
    print 'Gamma has to be greater than 1, try again'

else:
    print 'You would have to be traveling at about ',velocity(gamma)[0],' percent the speed of light', ' or ', round(velocity(gamma)[1]), ' meters per second', 'which is',round(velocity(gamma)[1]*2.24), 'mph'

const = []
for i in xval:
    const.append(gamma)
################################################################################################################################################################

#                                                                           Plotting

################################################################################################################################################################

plt.ylim(0,10) ## Because of the asymptotic behavior, limit the y axis to 10 times stretching of time
plt.xlim(-10,105)
plt.plot((xval/c)*100,yval, color = 'm') # plots x = percent of c, and y being gamma (not just the one input)

plt.plot(xlist,const,'k', linestyle = '--', linewidth = 1.5)  #Plotting a horizontal line that intersects a vertical line at the percent of c corresponding to the input gamma

plt.axvline(x = velocity(gamma)[0],color = 'k', linestyle = '--',linewidth = 1.5) # this is the vertical line. btw, 'k' means black in python for some reason
plt.title('Gamma vs % of c')
plt.xlabel('Percent of the Speed of Light')
plt.ylabel('Time Stretched by a factor of')

plt.grid() # this puts grid lines on your plot
plt.show()