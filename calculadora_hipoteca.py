#Vamos a calcular tu cuota mensual
#Y si puedes pagarlo con tu sueldo 
capital_inicial = float(input("Cuanto capital te ha prestado el banco? "))
euribor = 3.354
interes = (euribor+1)/100
interes_mensual = interes/12
duracion_meses_year = float(input("Cuantos anos vas a pagar la hipoteca? "))
n = 12*duracion_meses_year

sueldo_mensual_neto = float(input("Cual es tu sueldo mensual neto? "))
sueldo_treinta = sueldo_mensual_neto*0.30

cuota_mensual = round(capital_inicial * ((interes_mensual*(1+interes_mensual)**n)/(-1+(1+interes_mensual)**n)),2)

print("La cuota mensual que debes pagar es ",cuota_mensual,"€")

if sueldo_treinta < cuota_mensual:
    print("No puedes entrar a la hipoteca.")
else:
    print("Enhorabuena por tu nueva hipoteca, puedes pagarla.")

