import re
from datetime import datetime

date_test = """
         29 de
        maio de
        2024,
        16h54
        
    """

split_test = date_test.replace("\n", "").replace(" ", "")
split_test = re.split(r',|\s+de\s+', date_test)
split_test = [element.strip() for element in split_test if element.strip()]
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

mes = split_test[1]
print(mes)
if mes in meses:
    split_test[1] = meses[mes]

data_formatada = f"{split_test[0]}-{split_test[1]}-{split_test[2]} - {split_test[3]}"
data_formatada = datetime.strptime(data_formatada, "%d-%m-%Y - %Hh%Mm")
print(data_formatada)