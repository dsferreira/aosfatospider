import re
from datetime import datetime

date_test = """
         29 de
        maio de
        2024,
        16h54
        
    """

# Primeiro, substitua múltiplos espaços e quebras de linha por um único espaço
date_test = ' '.join(date_test.split())

# Depois, divida com expressões regulares considerando vírgulas e " de "
split_test = re.split(r',|\sde\s', date_test)

meses = {
    "janeiro": 1,
    "fevereiro": 2,
    "março": 3,
    "abril": 4,
    "maio": 5,
    "junho": 6,
    "julho": 7,
    "agosto": 8,
    "setembro": 9,
    "outubro": 10,
    "novembro": 11,
    "dezembro": 12
}

mes = split_test[1].strip().lower()
print("Mês extraído:", mes)  # Para verificação

if mes in meses:
    split_test[1] = meses[mes]  # Substituir o nome do mês pelo número

# Formata a data e a hora corretamente para conversão
data_formatada = f"{split_test[0]}-{split_test[1]}-{split_test[2]} - {split_test[3]}"

# Certifique-se de que o formato corresponde à string de data
data_formatada = datetime.strptime(data_formatada, "%d-%m-%Y - %Hh%M")
print(data_formatada)
