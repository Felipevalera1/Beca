# Databricks notebook source
print ("hello world")

# COMMAND ----------

A = 1
B = 3
C = 7
D = 5
E = 10
F = 12
G = 18
H = 20
I = 4
J = 1205

# COMMAND ----------

A = A + B
C = C * D
E = E / F
G = G - H
I = 35 - I
J = J / 105

# COMMAND ----------

print (A)
print (C)
print (E)
print (G)
print (I)
print (J)

# COMMAND ----------

def par (a):
    if a % 2 == 0 :
        print ("par")
    else:
        print ("impar");

# COMMAND ----------

par (1)

# COMMAND ----------

class calculadora:
    

 def soma(a,b):
        c = a + b
        print(c)
        
 def subtrair(a,b):
        d = a - b
        print(d)
        
 def divisão(a,b):
        e = a / b
        print(e)
        
 def multiplicação(a,b):
        f = a * b
        print(f)

# COMMAND ----------

calculadora.soma(6,3)

# COMMAND ----------

calculadora.subtrair(6,3)

# COMMAND ----------

calculadora.divisão(6,3)

# COMMAND ----------

calculadora.multiplicação(6,3)

# COMMAND ----------

lista_multiplicação = [18]

# COMMAND ----------


