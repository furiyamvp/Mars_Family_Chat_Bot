from filters.role import EmployeeRoleFilter
from loader import dp


if __name__ == "filters":
    dp.filters_factory.bind(EmployeeRoleFilter)

