from common.all_journals_app.fields_descriptions.fields_classes import *
from utils.deep_dict import deep_dict


cft = deep_dict()
cft.date_start = date_default
cft.shift_number = number_default
cft.massa_fur = dict(type="number", units='г')
cft.massa_sit = dict(type="number", units='г')
cft.fraction = percent_default
cft.executer = text_default

change_fraction_table_desc = cft.clear_empty().get_dict()
