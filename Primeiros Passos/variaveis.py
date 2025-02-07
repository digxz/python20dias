total_seguranca = 5
total_docente = 16
total_diretoria = 1

salario_seguranca = 3000
salario_docente = 6000
salario_direoria = 12500

total_funcionarios = total_seguranca + total_docente + total_diretoria
diferenca_salarial = salario_direoria - salario_seguranca

media_ponderada = ((total_seguranca * salario_seguranca) + (total_docente * salario_docente) + (total_diretoria * salario_direoria))/(total_seguranca + total_docente + total_diretoria)

print("Total de funcionários: ", total_funcionarios)
print("Diferença salarial: ", diferenca_salarial)
print("Média ponderada: ", media_ponderada)