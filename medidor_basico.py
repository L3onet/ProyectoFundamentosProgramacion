"""
>>> Leonel = MedidorEnergiaElectrica()
>>> Leonel.calcularConsumo(4900, 4390, 4.3)
2587.74
"""
# Crear la clase medidor de energia eléctrica

class MedidorEnergiaElectrica:
    """
    Esta clase calcula cuánto debe pagar por el consumo
    de energía eléctrica realizado en el último periodo. 
    """
    
    # Métodos de la clase medidor de energia eléctrica
    # Sintáxis es:
    # def nombremetodo(parámetros separados por comas):

    def calcularConsumo(self, lecturaActual, lecturaAnterior, costoKW):
        impuestos = float(0.0)            # Impuestos del periodo
        totalPagar = float(0.0)           # Total a pagar neto (con impuesto)
        consumoEnergiaElectrica = lecturaActual - lecturaAnterior
        costoConsumo = costoKW * consumoEnergiaElectrica
        if consumoEnergiaElectrica < 500:
            impuestos = costoConsumo * 0.22
            totalPagar = costoConsumo + impuestos
        if consumoEnergiaElectrica >= 500 and consumoEnergiaElectrica < 900:
            impuestos = costoConsumo * 0.18
            totalPagar = costoConsumo + impuestos
        if consumoEnergiaElectrica > 900:
            impuestos = costoConsumo * 0.12
            totalPagar = costoConsumo + impuestos
        return totalPagar

if __name__ == "__main__":
    import doctest
    doctest.testmod()