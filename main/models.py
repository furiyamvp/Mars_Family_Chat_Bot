from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey, Table, Enum, func

from main.constants import EmployeeRole
from main.database import metadata


EmployeeTable = Table(
    "employee",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("first_name", String),
    Column("last_name", String),
    Column("chat_id", BigInteger, unique=True),
    Column("phone_number", String),
    Column("role", Enum(EmployeeRole), nullable=False),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
)

ForbiddenWordTable = Table(
    "forbidden_word",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("word", String, nullable=False, unique=True),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),

    Column("employee_id", BigInteger, ForeignKey("employee.id"), nullable=False),
)
