from common.all_journals_app.fields_descriptions.fields_classes import *
from utils.deep_dict import deep_dict

ut = deep_dict()
ut.ks1 = numeric_default   # № печи
ut.val1 = numeric_default  # значение
ut.ks2 = numeric_default   # № печи
ut.val2 = numeric_default  # значение
ut.ks3 = numeric_default   # № печи
ut.val3 = numeric_default  # значение

udel_table_desc = ut.clear_empty().get_dict()

p1t3 = deep_dict()
p1t3.gmc4_1 = numeric_default
p1t3.gmc4_2 = numeric_default
p1t3.gmc1_1 = numeric_default
p1t3.gmc1_2 = numeric_default
p1t3.uk3 = numeric_default
p1t3.uk5 = numeric_default
p1t3.uk7 = numeric_default
p1t3.uk4 = numeric_default
p1t3.uk6 = numeric_default
p1t3.tonn = numeric_default
p1t3.silos1 = numeric_default
p1t3.silos2 = numeric_default
p1t3.silos3 = numeric_default
p1t3.silos4 = numeric_default
p1t3.silos5 = numeric_default
p1t3.silos6 = numeric_default
p1t3.silos7 = numeric_default
p1t3.silos8 = numeric_default
p1t3.silos9 = numeric_default

page1_table3_desc = p1t3.clear_empty().get_dict()



p2t1 = deep_dict()
p2t1.time = time_default
p2t1.collector = numeric_default
p2t1.concentration = numeric_default
p2t1.mixture = text_default
p2t1.conformity = text_default
p2t1.sign = text_default
page2_table1_desc = p2t1.clear_empty().get_dict()


p2t2 = deep_dict()
p2t2.time = time_default
p2t2.place = numeric_default
p2t2.S_cinder = numeric_default
p2t2.S_general = text_default
p2t2.conformity = text_default
p2t2.sign = text_default
p2t2.event = text_default
page2_table2_desc = p2t2.clear_empty().get_dict()


p2t3 = deep_dict()
p2t3.time = time_default
p2t3.character = text_default
p2t3.correction = text_default
p2t3.extra = numeric_default
p2t3.ks_comment = text_default
page2_table3_desc = p2t3.clear_empty().get_dict()


p2t4 = deep_dict()
p2t4.time = time_default
p2t4.comments = text_default
p2t4.mark = text_default
p2t4.sign = text_default
page2_table4_desc = p2t4.clear_empty().get_dict()


p2t5 = deep_dict()
p2t5.material = text_default
p2t5.note = text_default
p2t5.aspiration = text_default
p2t5.kip = text_default
p2t5.electro = text_default
p2t5.extra_note = text_default
page2_table5_desc = p2t5.clear_empty().get_dict()



