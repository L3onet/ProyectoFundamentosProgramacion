"""
>>> Leonel = MedidorEnergiaElectrica()
>>> Leonel.calcularConsumo(4900, 4390)
510
>>> Leonel.calcularCostoConsumo(4.3, 510)
2193.0
>>> Leonel.calcularTotalConsumoEnergiaElectrica(2193.0, 510)
2587.74
"""

# Crear la clase medidor de energia eléctrica

class MedidorEnergiaElectrica:
    """
    Esta clase calcula cuánto debe pagar por el consumo
    de energía eléctrica realizado en el último periodo. 
    """
    # Atributos de la clase medidor de energia eléctrica
    # Sintáxis es:
    # __nombreAtributo = tipo(valor)
    __consumoEnergiaElectrica = int(0)  # Consumo de energía eléctrica del periodo
    __costoKW = float(0.0)              # Costo del kiloWatt
    __lecturaAnterior = int(0)          # Lectura del periodo anterior
    __lecturaActual = int(0)            # Lectura del periodo actual
    __impuestos = float(0.0)            # Impuestos del periodo
    __costoConsumo = float(0.0)         # Total a pagar bruto (sin impuesto)
    __totalPagar = float(0.0)           # Total a pagar neto (con impuesto)

    # Métodos de la clase medidor de energia eléctrica
    # Sintáxis es:
    # def nombremetodo(parámetros separados por comas):

    def calcularConsumo(self, lecturaActual, lecturaAnterior):
        """
        Este método calcula el consumo de energía eléctrica del periodo
        actual.
        Parámetros de entrada:
            lecturaActual: Es el valor en KW del periodo actual
            lecturaAnterior: Es el valor en KW del periodo anterior

        Salida:
            El total de consumo de energía eléctrica del periodo.
        """
        self.__lecturaActual = lecturaActual
        self.__lecturaAnterior = lecturaAnterior
        self.__consumoEnergiaElectrica = self.__lecturaActual - self.__lecturaAnterior
        return self.__consumoEnergiaElectrica

    def calcularCostoConsumo(self, costoKw, consumoEnergiaElectrica):
        """
        Este método calcula el costo del consumo de energía 
        eléctrica del periodo actual.
        Parámetros de entrada:
            costoKw: Es el valor del KW 
            consumoEnergiaElectrica: Es el total de consumo de energía
            eléctrica del periodo
        Salida:
            El costo del consumo de energía eléctrica del periodo.
        """
        self.__costoKW = costoKw
        self.__costoConsumo = self.__costoKW * consumoEnergiaElectrica
        return self.__costoConsumo

    def calcularTotalConsumoEnergiaElectrica(self, costoConsumo, consumoEnergiaElectrica):
        """
        Este método calcula el total a pagar del consumo de energía 
        eléctrica del periodo actual con impuestos.
        Parámetros de entrada:
            costoConsumo: Es el total a pagar de energía eléctrica sin
            impuestos 
            consumoEnergiaElectrica: Es el total de consumo de energía
            eléctrica del periodo
        Salida:
            El total a pagar de energía eléctrica del periodo.
        """
        if consumoEnergiaElectrica < 500:
            self.__impuestos = costoConsumo * 0.22
            self.__totalPagar = costoConsumo + self.__impuestos
        if consumoEnergiaElectrica >= 500 and consumoEnergiaElectrica < 900:
            self.__impuestos = costoConsumo * 0.18
            self.__totalPagar = costoConsumo + self.__impuestos
        if consumoEnergiaElectrica > 900:
            self.__impuestos = costoConsumo * 0.12
            self.__totalPagar = costoConsumo + self.__impuestos
        return self.__totalPagar

if __name__ == "__main__":
    import doctest
    doctest.testmod()