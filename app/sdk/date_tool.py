import datetime


def date_diff_in_seconds(dt2, dt1):
    timedelta = dt2 - dt1  # type: datetime.timedelta
    return int(timedelta.total_seconds())


def date_diff_str(date_now, date, txt_prefix):
    seconds = date_diff_in_seconds(date_now, date)
    msg = ""

    if seconds <= 60:  # 1 minuto
        msg = "{} ahora".format(txt_prefix)
    elif seconds <= 3600:  # 1 hora
        number = round(seconds / 60)
        text = '' if number == 1 else 's'
        msg = "{} hace {} minuto{}".format(txt_prefix, number, text)
    elif seconds <= 86400:  # 1 dia
        number = round(seconds / 3600)
        text = '' if number == 1 else 's'
        msg = "{} hace {} hora{}".format(txt_prefix, number, text)
    elif seconds <= 2592000:  # 30 dias
        number = round(seconds / 86400)
        text = '' if number == 1 else 's'
        msg = "{} hace {} día{}".format(txt_prefix, number, text)
    elif seconds <= 31536000:  # 1 año
        number = round(seconds / 2592000)
        if number == 1:
            msg = "{} hace 1 mes".format(txt_prefix, number)
        else:
            msg = "{} hace {} meses".format(txt_prefix, number)
    else:
        msg = "{} el {}".format(txt_prefix, convert_date_to_str(date))

    return msg


def convert_date_to_str(date):
    months = ["",
              "ENE",
              "FEB",
              "MAR",
              "ABR",
              "MAY",
              "JUN",
              "JUL",
              "AGO",
              "SET",
              "OCT",
              "NOV",
              "DIC"]

    return '{} - {} - {}'.format(date.strftime("%d"), months[date.month], date.strftime("%Y"))


def date_diff_relative_str(date_now, date, txt_prefix, txt_sufijo):
    seconds = date_diff_in_seconds(date_now, date)
    msg = ""

    if seconds <= 60:  # 1 minuto
        msg = "{} en menos de 1 minuto".format(txt_prefix)
    elif seconds <= 3600:  # 1 hora
        number = round(seconds / 60)
        text = '' if number == 1 else 's'
        msg = "{} {} minuto{} {}".format(txt_prefix, number, text, txt_sufijo)
    elif seconds <= 86400:  # 1 dia
        number = round(seconds / 3600)
        text = '' if number == 1 else 's'
        msg = "{} {} hora{} {}".format(txt_prefix, number, text, txt_sufijo)
    elif seconds <= 2592000:  # 30 dias
        number = round(seconds / 86400)
        text = '' if number == 1 else 's'
        msg = "{} {} día{} {}".format(txt_prefix, number, text, txt_sufijo)
    else:  # 1 año
        number = round(seconds / 2592000)
        if number == 1:
            msg = "{} 1 mes {}".format(txt_prefix, number, txt_sufijo)
        else:
            msg = "{} {} meses {}".format(txt_prefix, number, txt_sufijo)

    return msg
