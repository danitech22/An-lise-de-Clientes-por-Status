clientes = [
    {"nome": "Ana", "idade": 25, "ativo": True, "compras": 5},
    {"nome": "João", "idade": 17, "ativo": False, "compras": 0},
    {"nome": "Maria", "idade": 32, "ativo": True, "compras": 8},
    {"nome": "Pedro", "idade": 40, "ativo": False, "compras": 2},
    {"nome": "Lucas", "idade": 15, "ativo": True, "compras": 1},
]

resumo = {}

for cliente in clientes:
    cliente_ativo = cliente["ativo"]

    if cliente_ativo not in resumo:
        resumo[cliente_ativo]={
            "total_clientes":0,
            "quantidade_vendas":0
            
        }

    resumo[cliente_ativo]["total_clientes"]+=1
    resumo[cliente_ativo]["quantidade_vendas"]+=cliente["compras"]

    
for cliente_ativo in resumo:
        
    resumo[cliente_ativo]["media"] = resumo[cliente_ativo]["quantidade_vendas"] /resumo[cliente_ativo]["total_clientes"]

print(resumo)



