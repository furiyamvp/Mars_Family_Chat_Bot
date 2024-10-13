from enum import Enum


class EmployeeRole(str, Enum):
    admin = "admin"
    moderator = "moderator"
