import time
from num2words import num2words

dia_semana = {
    0: "segunda",
    1: "terça",
    2: "quarta",
    3: "quinta",
    4: "sexta",
    5: "sabado",
    6: "domingo"
}

mes = {
    1: "Janeiro",
    2: "Fevereiro",
    3: "Março",
    4: "Abril",
    5: "Maio",
    6: "Junho",
    7: "Julho",
    8: "Agosto",
    9: "Setembro",
    10: "Outubro",
    11: "Novembro",
    12: "Dezembro"
}




def converter_data():
    ano = num2words(time.localtime().tm_year, lang='pt-br')
    data = f"{dia_semana[time.localtime().tm_wday]}, {time.localtime().tm_mday} de {mes[time.localtime().tm_mon]} de {ano}"
    return data