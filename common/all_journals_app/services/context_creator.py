from common.all_journals_app.models import CellValue, JournalPage
from common.all_journals_app.tables import fields_info
from utils.deep_dict import deep_dict


def get_full_data(page):
    res = deep_dict()

    for val in CellValue.objects.filter(journal_page=page):
        res[val.table_name][val.field_name][val.index] = val.value

    return res


def get_fields_info():
    return fields_info


def get_common_context(page):
    res = deep_dict()

    # res['full_data'] = get_full_data(page)
    # res['fields_info'] = get_fields_info()

    return res