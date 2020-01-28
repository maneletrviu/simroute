import numpy  as np
def cart2compass(deg):
   #Function that converts cartesian angles to compass angles arg <=360
   degN=90 - deg
   if ( degN) <0:
      return degN+360
   else:
      return degN
 
def compass2cart(degN):
    #Function that converts compass angles to cartesian angles arg <=360
   if (degN>=0) & (degN<=90):
      return abs(degN-90)
   else:
      return abs(450-degN)
   
def arrayRect2Comp(Ax,Ay):
   d=Ax.shape
   Az=np.zeros(shape=d)
   for i in range(d[1]):
      for j in range(d[0]):
         zeta=np.complex(Ax[j,i],Ay[j,i])
         an=cart2compass(np.angle(zeta,deg=True))
         Az[j,i]=an              
   return Az     

def arrayComp2Cart(Ax):
   d=Ax.shape
   Az=np.zeros(shape=d)
   for i in range(d[0]):
      for j in range(d[1]):
         Az[i,j]=compass2cart(Ax[i,j])
   return Az
  
def tic():
   #Homemade version of matlab tic and toc functions
   import time
   global startTime_for_tictoc
   startTime_for_tictoc = time.time()

def toc():
   import time
   if 'startTime_for_tictoc' in globals():
      print ('Elapsed time is  {}  seconds.'.format( (time.time() - startTime_for_tictoc)))
   else:
      print ("Toc: start time not set")
# diuen que es un invent https://gist.github.com/jeromer/2005586

def dir2dir(dir1,dir2,n):
   # passar de dir 1 a dir2 amb npassos compass a commpass
   #N son els nds interiors, o sigui:  rightn-leftn -1
   # el leftn i rihtn no surtiran al resultat
   #Tambe s'utilitza per fer el sud nort
   x1=np.cos(np.deg2rad(compass2cart(dir1)))
   y1=np.sin(np.deg2rad(compass2cart(dir1)))
   x2=np.cos(np.deg2rad(compass2cart(dir2)))
   y2=np.sin(np.deg2rad(compass2cart(dir2))) 
   dx=(x2-x1)/(n+1)
   dy=(y2-y1)/(n+1)
   out=np.zeros(n)
   for i in range(1,n+1):
      zeta=np.complex(x1+dx*i,y1+dy*i)
      out[i-1]=cart2compass(np.angle(zeta,deg=True))
   return out
   

   
   
