#======================================================
# Cálculo de curva Z-spline en n dimensiones
#======================================================
# Diego Vargas
#===========================
import numpy as np

#======================
# Clase Curva
#======================
class Curva:
    """==============================================================
        Curva construye la curva que pasa por los puntos x
       ==============================================================
        Parámetros: x coordenadas ordenadas ((x1),(x2),...)
                    f propiedades (f1(x), f2(x), ...)
                    dim dimendiones
       ==============================================================
    """
    #==============
    # Constructor
    #==============
    def __init__(self, x:float=[], dim:int=3):
        self.x = np.array(x,dtype=np.float64)
        self.dim = dim
        self.n:np.int32 = int(len(self.x)/self.dim) # Número de puntos
        self.l = []                                 # Longitud sobre la curva
        self.lista_de_puntos()
        self.longitud()

    #==================
    # Lista de puntos
    #==================
    def lista_de_puntos(self) -> str:
        print(f"Número de puntos = {str(self.n)}")

        # Formato de datos
        self.formato = ""
        for j in range(self.dim):
            self.formato += "%15.8e"
        self.formato += "\n"

        # Tupla de variables a imprimir
        for i in range(0, self.n):
            self.tup = (self.x[i],)
            for ii in range(1, self.dim):
                self.tup = self.tup + (self.x[i+ii*self.n], )
            print(self.formato % self.tup)

    #========================
    # Longitud punto a punto
    #========================
    def longitud(self) -> None:
        t:np.float64 = 0.0
        for i in range(0, self.n):
            ip1 = i+1
            if i == self.n-1:
                ip1 = 0
            d:np.float64 = (self.x[ip1]-self.x[i])**2
            for j in range(1, self.dim):
                d += (self.x[ip1+j*self.n]-self.x[i+j*self.n])**2
            t +=  d**0.5
            self.l.append(t)
        self.L = t
        self.dx = t/float(self.n)

    #===========================
    # Interpolación
    #===========================
    def interpolacion(self, p:int=0, r:float=0.0) -> list:
        """ r es el parámetro sobre la curva [0,1)
            p es la suavidad de la curva """
        
        rdx:np.float64 = 1.0/self.dx
        xi:float = []
        i:np.int32 = int(r*self.L*rdx)
        a:np.float64 = r*self.L*rdx - float(i)  # Distancia normalizada

        #==========================
        # Interpolación lineal C0
        #==========================
        if p == 0:
            ip1:no.int32 = i+1
            if i == self.n-1:
                ip1 = 0
            xi.append(a*self.x[ip1] + (1.0-a)*self.x[i])
            for j in range(1, self.dim):
                xi.append(a*self.x[ip1+j*self.n]+(1.0)*self.x[i+j*self.n])


        #============================
        # Interpolación Cúbica C1
        #============================

        elif p == 1:
            ip1:np.int32 = i + 1
            ip2:np.int32 = i + 2
            if i ==  self.n-1:
                ip1 = 0
                ip2 = 1
            if i == self.n-2:
                ip2 = 0
            im1:np.int32 = i-1
            if i == 0:
                im1 = self.n-1
            am1:np.float64 = a + 1.0
            ap1:np.float64 = 1.0-a
            ap2:np.float64 = 2.0-a
            z:np.float64 = 1.0 - 2.5*a*a + 1.5*a*a*a
            zp1:np.float64 = 1.0 - 2.5*ap1*ap1 + 1.5*ap1*ap1*ap1
            zp2:np.float64 = 0.5*(2.0-ap2)*(2.0-ap2)*(1.0-ap2)
            zm1:np.float64 = 0.5*(2.0-am1)*(2.0-am1)*(1.0-am1)
            xi.append(zp1*self.x[ip1]+z*self.x[i]+zp2*self.x[ip2]+zm1*self.x[im1])
            for j in range(1, self.dim):
                xi.append(zp1*self.x[ip1+j*self.n]+z*self.x[i+j*self.n]+zp2*self.x[ip2+j*self.n]+zm1*self.x[im1+j*self.n])

        #===================================
        # Interpolación Quintica C2
        #===================================
        
        elif p == 2:
            ip1:np.int32 = i+1
            ip2:np.int32 = i+2
            ip3:np.int32 = i+3
            if i == self.n-1:
                ip1 = 0
                ip2 = 1
                ip3 = 2
            if i == self.n-2:
                ip2 = 0
                ip3 = 1
            if i == self.n-3:
                ip3 = 0
            im1:np.int32 = i-1
            im2:np.int32 = i-2
            if i == 0:
                im1 = self.n-1
                im2 = self.n-2
            if i == 1:
                im2 = self.n-1
            u12:np.float64 = 1.0/12.0
            am1:np.flaot64 = a+1.0
            am2:np.flaot64 = a+2.0
            ap1:np.float64 = 1.0-a
            ap2:np.float64 = 2.0-a
            ap3:np.float64 = 3.0-a
            z:np.float64 = 1.0+a*a*u12*(-15.0+a*(-35.0+a*(63.0+a*(-25.0))))
            zp1:np.float64 = 1.0+ap1*ap1*u12*(-15.0+ap1*(-35.0+ap1*(63.0+ap1*(-25.0))))
            zp2:np.float64 = -4.0+u12*ap2*(225.0+ap2*(-367.5+ap2*(272.5+ap2*(-94.5+12.5*ap2))))
            zp3:np.float64 = 18.0+u12*ap3*(-495.0+ap3*(382.5+ap3*(-156.5+ap3*(31.5-2.5*ap3))))
            zm1:np.float64 = -4.0+u12*am1*(225.0+am1*(-367.5+am1*(272.5+am1*(-94.5+12.5*am1))))
            zm2:np.float64 = 18.0+u12*am2*(-495.0+am2*(382.5+am2*(-156.5+am2*(31.5-2.5*am2))))
            xi.append(zp1*self.x[ip1]+z*self.x[i]+zp2*self.x[ip2]+zp3*self.x[ip3]+zm1*self.x[im1]+zm2*self.x[im2])
            for j in range(1, self.dim):
                xi.append(zp1*self.x[ip1+j*self.n]+z*self.x[i+j*self.n]+zp2*self.x[ip2+j*self.n]+zp3*self.x[ip3+j*self.n]+zm1*self.x[im1+j*self.n]+zm2*self.x[im2+j*self.n])

        else:
            print("La suavidad debe ser 0, 1 o 2")
        
        return xi


#================================================================================
# Función zspline crea el z-spline de un conjunto de puntos en dim dimensiones,
# n segmentos y continuidad (aproximación) cont
# x,y = zspline(conjunto de puntos, dimensión, número de segmentos, continuidad)
#================================================================================
def zspline(puntos, dim, n, cont):

    curva = Curva(puntos, dim)
    dx:np.float64 =  1.0/float(n)
    x = np.zeros(n, dtype=np.float64)
    y = np.zeros(n, dtype=np.float64)

    for i in range(0,n):
        r:np.float64 = float(i)*dx
        [x[i],y[i]] = curva.interpolacion(cont, r)

    return x,y

