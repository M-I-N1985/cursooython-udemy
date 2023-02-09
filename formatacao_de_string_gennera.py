"""
Falei com os meninos e eles informaram que eu poderia trabalhar com o código como se fossem strings,
para fazer uma iteração
"""
list = ["ASP121", "ASP60", "CLI06", "C01"]
numeros = "0123456789"
inicial = "ASPCLI"
a = ""
b = ""
c = ""
cod = ""
for codigo in list:
    for letra in codigo:
        if letra in inicial:
            cod = cod + letra
        print(cod)
    # else:
    #     if codigo[0] == "C":
    #         if codigo[1] in numeros:
    #             cod = "CLI"+str(codigo[1:])
