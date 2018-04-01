import random
class Fecha:
    def __init__(self,dia,mes,año):
        self.dia = dia
        self.mes = mes
        self.año = año

    def getDateRandomyymmdd(self):
        self.dateRandomGenerator()
        return str(self.año + self.mes + self.dia)

    def dateRandomGenerator(self):
        año = str(random.randint(0,99))
        if año in ['0','1','2','3','4','5','6','7','8','9']:
            self.año = str('0' + año)
        else:
            self.año = str(año)
        mes = str(random.randint(1,12))
        if mes in ['0','1','2','3','4','5','6','7','8','9']:
            self.mes = str('0' + mes)
        else:
            self.mes = str(mes)
        if mes in ['1','3','5','7','8','10','12']:
            dia = str(random.randint(1,31))
            if dia in ['0','1','2','3','4','5','6','7','8','9']:
                self.dia = str('0' + dia)
            else:
                self.dia = str(dia)
        elif mes in ['4','6','9','11']:
            dia = str(random.randint(1,30))
            if dia in ['0','1','2','3','4','5','6','7','8','9']:
                self.dia = str('0' + dia)
            else:
                self.dia = str(dia)
        elif mes in ['2']:
            if int(año) % 4 == 0:
                dia = str(random.randint(1,29))
                if dia in ['0','1','2','3','4','5','6','7','8','9']:
                    self.dia = str('0' + dia)
                else:
                    self.dia = str(dia)
            else:
                dia = str(random.randint(1,28))
                if dia in ['0','1','2','3','4','5','6','7','8','9']:
                    self.dia = str('0' + dia)
                else:
                    self.dia = str(dia)
