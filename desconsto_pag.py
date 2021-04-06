vr = 21
dias_pagos = 24
total_pago = dias_pagos * vr

dias_desc = 5
total_desc = dias_desc * vr

dias_abril = 13
total_abril = dias_abril * vr

desconto = (-total_pago + -total_desc) + total_abril

print(f'Dias pagos {total_pago:.2f}, Dias Feriado {total_desc:.2f}, Dias trabalhados em abril {total_abril:.2f}')
print(f'Saldo de descontos {desconto}')
