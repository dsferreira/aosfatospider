from itemadapter import ItemAdapter
import re
from datetime import datetime

class AosfatoscraperPipeline:
    def process_item(self, item, spider):
        adapter = ItemAdapter(item)

        date_test = adapter.get('date')
        date_test = ' '.join(date_test.split())

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

        if mes in meses:
            split_test[1] = meses[mes]  

        data_formatada = f"{split_test[0]}-{split_test[1]}-{split_test[2]} {split_test[3]}"
        ano = split_test[2]
        mes = split_test[1]
        dia = split_test[0]
        hora = split_test[3]

        try:
            datetime_object = datetime.strptime(data_formatada, "%d-%m-%Y %Hh%M")
            adapter['date'] = datetime_object  
        except Exception as e:
            spider.logger.error(f"Erro ao formatar a data: {e}")
            adapter['date'] = None  
        return item
