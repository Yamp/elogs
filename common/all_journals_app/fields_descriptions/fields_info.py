from common.all_journals_app.fields_descriptions.tables.change_fraction import change_fraction_table_desc
from common.all_journals_app.fields_descriptions.tables.conc_raports_tables import *
from common.all_journals_app.fields_descriptions.tables.electrolysis_masters_reports import *
from common.all_journals_app.fields_descriptions.tables.furnace_repair_table import *
from common.all_journals_app.fields_descriptions.tables.furnace_stove_area import *
from common.all_journals_app.fields_descriptions.tables.input_output_report import *
from common.all_journals_app.fields_descriptions.tables.leaching_express_analysis import *
from common.all_journals_app.fields_descriptions.tables.leaching_repair_equipment import leaching_repair_table_desc
from common.all_journals_app.fields_descriptions.tables.metals_compute import *
from common.all_journals_app.fields_descriptions.tables.electrolysis_technical_report_4_degree_tables import *
from common.all_journals_app.fields_descriptions.tables.technological_tasks import *
import common.all_journals_app.fields_descriptions.tables.electrolysis_technical_report_3_degree_tables as t3
import common.all_journals_app.fields_descriptions.tables.electrolysis_technical_report_12_degree_tables as t12
from common.all_journals_app.fields_descriptions.tables.electrolysis_repair_report_tables import *


from utils.deep_dict import deep_dict

fields_info_desc = deep_dict()

fields_info_desc.leaching_express_analysis.vsns_table = vsns_table_desc
fields_info_desc.leaching_express_analysis.thickeners_table = thickeners_table_desc
fields_info_desc.leaching_express_analysis.zinc_pulp_table = zinc_pulp_desc
fields_info_desc.leaching_express_analysis.appt_hydrometal_table = aph_table_desc
fields_info_desc.leaching_express_analysis.agitators_table = agitator_table_desc
fields_info_desc.leaching_express_analysis.reagents_table = reagents_table_desc
fields_info_desc.leaching_express_analysis.neutral_thickeners_table = neutral_thickeners_desc
fields_info_desc.leaching_express_analysis.tanks_availability_table = tanks_availability_desc
fields_info_desc.leaching_express_analysis.tanks_for_finished_products_table = tanks_for_finished_products_desc
fields_info_desc.leaching_express_analysis.self_protection_table = self_protection_desc
fields_info_desc.leaching_express_analysis.cinder_table = cinder_table_desc
fields_info_desc.leaching_express_analysis.sample_table = sample_table_desc
fields_info_desc.leaching_express_analysis.loads_table = loads_table_desc
fields_info_desc.leaching_express_analysis.neutral_table = neutral_table_desc
fields_info_desc.leaching_express_analysis.shift_info_table = shift_info_table_desc

fields_info_desc.leaching_repair_quipment.repair_table = leaching_repair_table_desc

fields_info_desc.concentrate_report_journal.big_table = big_table_desc
fields_info_desc.concentrate_report_journal.small_table = small_table_desc
fields_info_desc.concentrate_report_journal.upper_table = upper_table_desc
fields_info_desc.concentrate_report_journal.lower_table = lower_table_desc

fields_info_desc.report_income_outcome_schieht.main_table = main_table_desc
fields_info_desc.report_income_outcome_schieht.supply_of_zinc_concentrates = supply_zinc_desc
fields_info_desc.report_income_outcome_schieht.year_plan_schieht = year_plan_schieht_desc
fields_info_desc.report_income_outcome_schieht.summary_table = summary_table_desc

fields_info_desc.metals_compute.main_table = metals_main_desc
fields_info_desc.metals_compute.sns_table = sns_table_desc
fields_info_desc.metals_compute.sgok_table = sgok_table_desc
fields_info_desc.metals_compute.gof_table = gof_table_desc
fields_info_desc.metals_compute.avg_month_table = avg_month_table_desc
fields_info_desc.metals_compute.cinder_conc_table = cinder_conc_table_desc
fields_info_desc.metals_compute.concentrat_table = concentrat_table_desc
fields_info_desc.metals_compute.contain_zn_table = contain_zn_table_desc


fields_info_desc.technological_tasks.main_table = technologial_tasks_main_desc
fields_info_desc.furnace_repair.repair_table = repair_table_desc
fields_info_desc.furnace_changed_fraction.main_table = change_fraction_table_desc

fields_info_desc.electrolysis_technical_report_4_degree.left_table = left_table_desc
fields_info_desc.electrolysis_technical_report_4_degree.right_table = right_table_desc
fields_info_desc.electrolysis_technical_report_3_degree.left_table = t3.left_table_desc
fields_info_desc.electrolysis_technical_report_3_degree.right_table = t3.right_table_desc
fields_info_desc.electrolysis_technical_report_12_degree.left_table = t12.left_table_desc
fields_info_desc.electrolysis_technical_report_12_degree.right_table = t12.right_table_desc
fields_info_desc.electrolysis_repair_report_tables.main_table = repair_main_table_desc

fields_info_desc.masters_report.seria1_table = seria1_table_desc
fields_info_desc.masters_report.seria3_table = seria3_table_desc
fields_info_desc.masters_report.seria4_table = seria4_table_desc
fields_info_desc.masters_report.params_table = params_table_desc
fields_info_desc.masters_report.melt_area1_table = melt_area1_table_desc
fields_info_desc.masters_report.melt_area2_table = melt_area2_table_desc
fields_info_desc.masters_report.zinc_table = zinc_table_desc
fields_info_desc.masters_report.last_table = last_table_desc


fields_info_desc.reports_furnace_area.main_table = fa_main_table_desc
fields_info_desc.reports_furnace_area.udel_table = udel_table_desc
fields_info_desc.reports_furnace_area.area_class_cinder = page1_table3_desc
fields_info_desc.reports_furnace_area.electrofilter = electro_filters_desc
fields_info_desc.reports_furnace_area.warehouse_concentrates = wh_concentrates_desc
fields_info_desc.reports_furnace_area.airmachines = air_machines_desc
fields_info_desc.reports_furnace_area.fences_table = page1_fences_desc

fields_info_desc.reports_furnace_area.concentration_by_time_table = page2_table1_desc
fields_info_desc.reports_furnace_area.places_of_sampling_table = page2_table2_desc
fields_info_desc.reports_furnace_area.corrective_actions_table = page2_table3_desc
fields_info_desc.reports_furnace_area.self_protection_table = page2_table4_desc
fields_info_desc.reports_furnace_area.worth_table = page2_table5_desc


bf = deep_dict()
bf.column1 = numeric_default
bf.column2 = numeric_default
bf.column3 = numeric_default
fields_info_desc.buff_journal.trening_table = bf.clear_empty().get_dict()
