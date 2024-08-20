import pandas as pd
import numpy as np

operacion = input("Que sistema de amortizacion va a utilizar? (F) (A) o (U) ")

if operacion == "f":

    def frances():
        #Inicializar las listas
        cuota = []
        intereses = []
        capitales = []
        saldo = []

        # Solicitar datos al usuario
        valor_prestamo = float(input("¿Cuál es el valor del préstamo que quiere solicitar? "))
        tasa_interes_anual = float(input("¿Cuál es la tasa de interés anual? ")) / 100
        tiempo_años = float(input("¿Cuál es el período de devolución del préstamo en años? (e.g., 1.5 para año y medio) "))
        frecuencia = int(input("¿Cuál es la frecuencia de pagos por año? (e.g., 12 para mensual) "))
        periodos = int(tiempo_años * frecuencia)

        # Calcular la cuota mensual usando la fórmula de amortización
        tasa_periodica = tasa_interes_anual / frecuencia
        cuota_mensual = valor_prestamo * (tasa_periodica) / (1 - (1 + tasa_periodica) ** (-periodos))

        # Inicializar el saldo actual
        saldo_actual = valor_prestamo

        # Calcular las cuotas, intereses, capital y saldo para cada período
        for n in range(1, periodos + 1):
            interes_periodo = saldo_actual * tasa_periodica
            capital_periodo = cuota_mensual - interes_periodo
            saldo_actual = cuota_mensual * (1 - ( 1 + (tasa_periodica))**(-(periodos-n)))/(tasa_periodica)

            # Agregar los valores a las listas correspondientes
            cuota.append(round(cuota_mensual, 2))
            intereses.append(round(interes_periodo, 2))
            capitales.append(round(capital_periodo, 2))
            saldo.append(round(saldo_actual, 2))

        # Crear el DataFrame
        df = pd.DataFrame({
            "Cuotas": cuota,
            "Intereses": intereses,
            "Capital": capitales,
            "Saldos": saldo
        })

        #Calculo datos importantes
        suma_intereses = df["Intereses"].sum().round(2)
        suma_cuotas = df["Cuotas"].sum().round(2)
        suma_capital = df["Capital"].sum().round(2)
        numerador = ((-valor_prestamo*0.5/cuota_mensual)*tasa_periodica)+1
        denominador = 1+tasa_periodica
        mitad_amortizacion = -1* (np.log(numerador)/np.log(denominador)).round(2)

        # Redondear los valores del DataFrame a 2 decimales
        df = df.round(2)
        
        #Formatear los números con comas como separadores de miles
        df = df.applymap(lambda x: f"{x:,.2f}")

        # Configurar el índice para comenzar en 1
        df.index = range(1, len(df) + 1)

        # Mostrar el DataFrame
        print(df)

        #Muestro datos complementarios
        print(f"La suma de los intereses totales es de {suma_intereses}")
        print(f"La suma de las cuotas es de {suma_cuotas}")
        print(f"La suma de el capital es de {suma_capital}")
        print(f"La mitad del prestamo se amortiza en {mitad_amortizacion} meses")
        
    frances()
    
elif operacion == "a":

    def aleman():
        # Inicializar las listas
        cuota = []
        intereses = []
        capitales = []
        saldo = []

        # Solicitar datos al usuario
        valor_prestamo = float(input("¿Cuál es el valor del préstamo que quiere solicitar? "))
        tasa_interes_anual = float(input("¿Cuál es la tasa de interés anual? ")) / 100
        tiempo_años = float(input("¿Cuál es el período de devolución del préstamo en años? (e.g., 1.5 para año y medio) "))
        frecuencia = int(input("¿Cuál es la frecuencia de pagos por año? (e.g., 12 para mensual) "))
        periodos = int(tiempo_años * frecuencia)

        # Calculo la tasa periodica
        tasa_periodica = tasa_interes_anual / frecuencia
        
        # Inicializar el saldo actual
        saldo_actual = valor_prestamo

        # Calcular las cuotas, intereses, capital y saldo para cada período
        for n in range (1, periodos+1):
            intereses_periodicos = tasa_periodica * saldo_actual
            capital_mensual = valor_prestamo / periodos
            cuota_mensual = intereses_periodicos + capital_mensual
            saldo_actual = saldo_actual - capital_mensual

            # Agrego los valores a las lista
            cuota.append(cuota_mensual)
            intereses.append(intereses_periodicos)
            capitales.append(capital_mensual)
            saldo.append(saldo_actual)
        
        df = pd.DataFrame({
            "Cuotas": cuota,
            "Intereses": intereses,
            "Capital": capitales,
            "Saldos": saldo
        })

        #Calculo datos importantes
        suma_intereses = df["Intereses"].sum().round(2)
        suma_cuotas = df["Cuotas"].sum().round(2)
        suma_capital = df["Capital"].sum().round(2)
        numerador = ((-valor_prestamo*0.5/cuota_mensual)*tasa_periodica)+1
        denominador = 1+tasa_periodica
        mitad_amortizacion = -1* (np.log(numerador)/np.log(denominador)).round(2)

        # Redondear los valores del DataFrame a 2 decimales
        df = df.round(2)
        
        #Formatear los números con comas como separadores de miles
        df = df.applymap(lambda x: f"{x:,.2f}")

        # Configurar el índice para comenzar en 1
        df.index = range(1, len(df) + 1)

        # Mostrar el DataFrame
        print(df)

        #Muestro datos complementarios
        print(f"La suma de los intereses totales es de {suma_intereses}")
        print(f"La suma de las cuotas es de {suma_cuotas}")
        print(f"La suma de el capital es de {suma_capital}")
        print(f"La mitad del prestamo se amortiza en {mitad_amortizacion} meses")
    
    aleman()

elif operacion == "u":
        def USA():
            #Inicializar las listas
            cuota = []
            intereses = []
            capitales = []
            saldo = []
            ahorro = []

            # Solicitar datos al usuario
            valor_prestamo = float(input("¿Cuál es el valor del préstamo que quiere solicitar? "))
            tasa_interes_anual = float(input("¿Cuál es la tasa de interés anual? ")) / 100
            tiempo_años = float(input("¿Cuál es el período de devolución del préstamo en años? (e.g., 1.5 para año y medio) "))
            frecuencia = int(input("¿Cuál es la frecuencia de pagos por año? (e.g., 12 para mensual) "))
            periodos = int(tiempo_años * frecuencia)
            tasa_ahorro = float(input("Cual es la tasa de ahorro que le proporciona su banco? ")) / 100

            # Calculo la tasa periódica
            tasa_periodica = tasa_interes_anual / frecuencia
            tasa_periodica_ahorro = tasa_ahorro / frecuencia

            # Inicializar el saldo actual
            saldo_actual = valor_prestamo

            # Calcular las cuotas, intereses y saldo para cada período
            for n in range(1, periodos + 1):
                intereses_periodicos = tasa_periodica * saldo_actual
                
                # El capital solo se paga al final del periodo total
                if n == periodos:
                    capital_mensual = valor_prestamo
                else:
                    capital_mensual = 0
                
                cuota_mensual = intereses_periodicos + capital_mensual
                saldo_actual = saldo_actual - capital_mensual
                ahorro_mensual = valor_prestamo * (tasa_periodica_ahorro / (((1 + tasa_periodica_ahorro)**(periodos)) -1))

                # Agregar los valores a las listas
                cuota.append(cuota_mensual)
                intereses.append(intereses_periodicos)
                capitales.append(capital_mensual)
                saldo.append(saldo_actual)
                ahorro.append(ahorro_mensual)

            # Crear el DataFrame
            df = pd.DataFrame({
                "Cuotas": cuota,
                "Intereses": intereses,
                "Capital": capitales,
                "Saldos": saldo,
                "Ahorro": ahorro
            })

            #Calculo datos importantes
            suma_intereses = df["Intereses"].sum().round(2)
            suma_cuotas = df["Cuotas"].sum().round(2)
            suma_capital = df["Capital"].sum().round(2)
            numerador = ((-valor_prestamo*0.5/cuota_mensual)*tasa_periodica)+1
            denominador = 1+tasa_periodica
            mitad_amortizacion = -1* (np.log(numerador)/np.log(denominador)).round(2)

            # Redondear los valores del DataFrame a 2 decimales
            df = df.round(2)

            # Formatear los números con comas como separadores de miles
            df = df.applymap(lambda x: f"{x:,.2f}")

            # Configurar el índice para comenzar en 1
            df.index = range(1, len(df) + 1)

            # Mostrar el DataFrame
            print(df)

            #Muestro datos complementarios
            print(f"La suma de los intereses totales es de {suma_intereses}")
            print(f"La suma de las cuotas es de {suma_cuotas}")
            print(f"La suma de el capital es de {suma_capital}")
            print(f"La mitad del prestamo se amortiza en {mitad_amortizacion} meses")
        
        USA()

else:
    print("Porfavor ingresar una opcion correcta")
