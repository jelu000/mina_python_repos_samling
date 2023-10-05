antal_riskorn=1

for n in range(0, 64):
    antal_riskorn=antal_riskorn + antal_riskorn
    print(f"ruta nr {n+1} = antal riskorn: {antal_riskorn}")
print(f"\n Antal riskorn {antal_riskorn}")

gramris =antal_riskorn*0.017
print(f"\n Vikten om riskornet väger 0,017gr blir totalt {gramris} gr")
ton = gramris/100000
print(f"\nI ton blir de: {ton}")
print(f"\nI Giga ton blir de: {ton/1000000000}")

print(f"\nom alla i världen delar: {ton/7500000000}")

print(f"\nAntal år det tar att odla fram med nuvarande produktion: {ton/600000000} år")