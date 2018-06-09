import json
from utils.deep_dict import deep_dict
from datetime import time
from common.all_journals_app.fields_descriptions.fields_classes import *


 #-----------------Left Table-----------------#
lt = deep_dict()

rows_names_for_db = [
    "zn",
    "h2so4",
    "solute1",
    "solute2",
    "mixture_temp",
    "bath_temp",
    "temp1",
    "amperage1"
    "amperage2"
]

rows_names_for_view = [
        "Zn в отр./смеси г/л",
        "H2SO4 отр. г/л",
        "Температура смеси, С",
        "Температура в ваннах, С",
        "Температура нейтр. град.",
        "I, кА 1 степени",
        "I, кА 2 степени"
]

lt.row_names = [{"db": db, "view": view} for db, view in
             zip(rows_names_for_db, rows_names_for_view)]


field_infos_for_rows = [numeric_default] * 12 + [text_default] * 2

lt.times = [
    ":".join(str(time(hour=hour % 24)).split(":")[:-1])
    for hour in range(20, 20 + 12)
]

lt.last_headers = ["inconsistencies", "measures"]
for row_name, desc in zip(rows_names_for_db, field_infos_for_rows):
    for time in lt.times + lt.last_headers:
        field_name = row_name + time
        lt[field_name] = desc

left_table_desc = lt.clear_empty().get_dict()


lt.grad1_vent = numeric_default
lt.grad2_vent = numeric_default
lt.grad3_vent = numeric_default
lt.grad4_vent = numeric_default
lt.grad5_vent = numeric_default
lt.grad6_vent = numeric_default
lt.grad7_vent = numeric_default
lt.grad8_vent = numeric_default
lt.grad9_vent = numeric_default

lt.grad1_mode = numeric_default
lt.grad2_mode = numeric_default
lt.grad3_mode = numeric_default
lt.grad4_mode = numeric_default
lt.grad5_mode = numeric_default
lt.grad6_mode = numeric_default
lt.grad7_mode = numeric_default
lt.grad8_mode = numeric_default
lt.grad9_mode = numeric_default

lt.crystal1 = numeric_default
lt.crystal2 = numeric_default
lt.common1 = numeric_default
lt.common2 = text_default
lt.series31 = numeric_default
lt.series32 = text_default
lt.series41 = numeric_default
lt.series42 = text_default

lt.pumps_summ = text_default


left_table_desc = lt.clear_empty().get_dict()
#-----------------Right Table-----------------#
rt = deep_dict()


rt.h2so4 = text_default
rt.zn = text_default

#--------part1----------#
rt.solodka = numeric_default
rt.glue = numeric_default
rt.stroncii = numeric_default
rt.magnaflok = numeric_default
rt.znk = numeric_default
rt.cu1 = numeric_default
rt.co1 = numeric_default
rt.cd1 = numeric_default
rt.sb1 = numeric_default
rt.fe2p1 = numeric_default
rt.bt1 = numeric_default
rt.weight1_1 = numeric_default

rt.glue_resid_up = numeric_default
rt.glue_resid_down = numeric_default
rt.solodka_resid_up = numeric_default
rt.solodka_resid_down = numeric_default
rt.magnaflok_resid = numeric_default
rt.stroncii_resid = numeric_default
rt.cryst1 = numeric_default
rt.cryst2 = numeric_default



right_table_desc = rt.clear_empty().get_dict()