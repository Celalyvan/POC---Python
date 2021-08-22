# actualiza una columna de precios a dolar a precios de peso

import pandas  #sirve para interpretar excel
import requests
import statistics

r = request.get("https:\\api.recursospython.com/dollar")
cotizacion = statistics.mean(r.json().values())  # statistics.mean() calcula un promedio

print(cotizacion)

def dolar_a_peso(precioEnUSD):
    return precioEnUSD * cotizacion

excel = pandas.read_excel("productos.xlsx")
excel["precio en pesos"] = excel["precio en dólares"].apply(dolar_a_peso)

excel.to_excel("productos.xlsx", index=False)



