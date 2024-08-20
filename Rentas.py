import pandas as pd
import numpy as np

usuario = input("Que tipo de renta te gustaria utilizar? (AI) para A1NI o (SI) para S1NI ").lower()

monto_final = []

if usuario == "ai":
    def aini():
        valor_contado = input("Tiene su ejercicio un valor de contado? SI/NO ").lower()
        if valor_contado == "si":
            valor_contado = float(input("Cual es valor de contado del ejercicio? "))
            tasa_interes_anual = float(input("¿Cuál es la tasa de interés anual? ")) / 100
            numero_cuotas = int(input("En cuntas cuotas se realiza el resto del pago? "))
            valor_cuotas = float(input("Cual es el valor de las cuotas mensuales? "))
            frecuencia = int(input("¿Cuál es la frecuencia de pagos por año? (e.g., 12 para mensual) "))
            tasa_periodica = tasa_interes_anual / frecuencia
            monto_cero = valor_contado + valor_cuotas * ((1-(1 + tasa_periodica)**(-numero_cuotas))/tasa_periodica)

            for n in range(0, numero_cuotas+1):
                montos_finales = monto_cero * (1 + tasa_periodica)**n

                monto_final.append(round(montos_finales,2))
            
            df = pd.DataFrame({"Monto Final por Periodo" : monto_final})

            #Formatear los números con comas como separadores de miles
            df = df.applymap(lambda x: f"{x:,.2f}")

            # Mostrar el DataFrame
            print(df)
        
        elif valor_contado == "no":
            tasa_interes_anual = float(input("¿Cuál es la tasa de interés anual? ")) / 100
            numero_cuotas = int(input("En cuntas cuotas se realiza el resto del pago? "))
            valor_cuotas = float(input("Cual es el valor de las cuotas mensuales? "))
            frecuencia = int(input("¿Cuál es la frecuencia de pagos por año? (e.g., 12 para mensual) "))
            tasa_periodica = tasa_interes_anual / frecuencia
            monto_cero = valor_contado + valor_cuotas * ((1-(1 + tasa_periodica)**(-numero_cuotas))/tasa_periodica)

            for n in range(0, numero_cuotas+1):
                montos_finales = monto_cero * (1 + tasa_periodica)**n

                monto_final.append(round(montos_finales,2))
            
            df = pd.DataFrame({"Monto Final por Periodo" : monto_final})

            #Formatear los números con comas como separadores de miles
            df = df.applymap(lambda x: f"{x:,.2f}")

            # Mostrar el DataFrame
            print(df)
            
        else:
            print("Colocar una opcion correcta!")
    
    aini()

elif usuario == "si":
    print("Coca")

else:
    print("Colocar una respuesta correcta ")
