suma_par=0
suma_impar=0
suma_total=0
cont_par=0
cont_impar=0
numeros = []
class Ingreso:
    def __init__(self, array:list = None):
        self.__tam = len(array)
        self.__suma_par = None
        self.__suma_impar = None
        self.__suma_total = None
        self.__cont_par = None
        self.__cont_impar = None

    # Metodos gets  
    @property           
    def get_tam(self):
        return self.__tam

    @property 
    def getsuma_par(self):
        return self.__suma_par

    @property 
    def getsuma_impar(self):
        return self.__suma_impar

    @property 
    def getsuma_total(self):
        return self.__suma_total

    @property 
    def getcont_par(self):
        return self.__cont_par

    @property 
    def getcont_impar(self):
        return self.__cont_impar

    def valores(self):
        i=0
        for i in range(self.get_tam):
            num=int(input("Ingrese el valor #[",i + 1,"]: "))
            numeros.append(num)
            if (numeros[i]%2==0):
                self.cont_par=self.cont_par+1
                self.suma_par=self.suma_par+numeros[i]
            else:
                self.cont_impar=self.cont_impar+1
                self.suma_impar=self.suma_impar+numeros[i]
            i=i+1
        for i in range(self.get_tam):
            print("numeros[",i,"] ",numeros[i])
        for i in range(self.get_tam):
            self.suma_total=self.suma_total+numeros[i]
    
    def datos(self):
        print("Los numeros pares son: ",self.getcont_par())
        print("Los numeros impares son: ",self.getcont_impar())
        print("La suma de numeros pares es: ",self.getsuma_par())
        print("La suma de numeros impares es: ",self.getsuma_impar())
        print("La suma de numeros es: ",self.getsuma_total())
    
if __name__ == "__main__":
    c = Ingreso(int(input("Ingrese un rango: ")) )
    c.valores()
    c.datos()