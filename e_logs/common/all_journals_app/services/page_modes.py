from e_logs.common.login_app.models import Employee
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required


APP = 'all_journals_app'
VALIDATE_CELLS = APP + ".validate_cells"
EDIT_CELLS = APP + ".edit_cells"
VIEW_CELLS = APP + ".view_cells"
PLANT_PERM = APP + ".modify_{plant}"


class PageModeError(Exception):
    def __init__(self, value):
        self.value = value


@login_required
def plant_permission(request):
    employee = Employee.objects.get(user=request.user)
    plant = request.path.split("/")[1]
    return employee.user.has_perm(PLANT_PERM.format(plant=plant))


@login_required
def page_mode_is_valid(request, page):
    employee = Employee.objects.get(user=request.user)
    page_mode = request.GET.get('page_mode')
    if page_mode:
        if request.user.is_superuser:
            return True
        if plant_permission(request):
            return check_mode_permissions(employee, page, page_mode)
        else:
            return page_mode == "view"
    else:
        return False


@login_required
def check_mode_permissions(employee, page, page_mode):
    is_valid = False
    if page_mode == "validate":
        is_valid = employee.user.has_perm(VALIDATE_CELLS)
    if page_mode == "edit":
        if page.type == "shift":
            is_valid = page.is_active and employee.user.has_perm(EDIT_CELLS)
        if page.type == "equipment":
            is_valid = employee.user.has_perm(EDIT_CELLS)
    if page_mode == "view":
        is_valid = employee.user.has_perm(VIEW_CELLS)
    return is_valid


@login_required
def has_edited(request, page):
    return page in list(request.user.employee.owned_shifts.all())


@login_required
def default_page_mode(request, page):
    employee = Employee.objects.get(user=request.user)
    if plant_permission(request):
        if employee.user.has_perm(VALIDATE_CELLS):
            return "validate"
        elif employee.user.has_perm(VIEW_CELLS):
            return "view"
        else:
            raise PermissionDenied("Вам нечего делать на этой странице. Уходите.")
    else:
        if employee.user.has_perm(VIEW_CELLS):
            return "view"
        else:
            raise PermissionDenied("У вас нет доступа к этому цеху.")


@login_required
def get_page_mode(request, page):
    if page_mode_is_valid(request, page):
        return request.GET.get('page_mode')
    else:
        return default_page_mode(request, page)
