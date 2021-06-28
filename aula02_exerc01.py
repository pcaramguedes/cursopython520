#!/usr/bin/python3

ano=input("Qual o seu ano de nascimento: ")

print("--------------------------")
print("   Geracao       Intervalo")

if int(ano) <= 1964:
    print("Baby Boomer ---> Até 1964")
elif int(ano) >=1965 and int(ano) <= 1979:
    print("Geracao X ---> 1965 - 1979")
elif int(ano) >= 1980 and int(ano) <= 1994:
    print("Geracao Y ---> 1980 - 1994")
elif int(ano) >= 1995:
    print("Geracao Z ---> 1995 - Atual")


