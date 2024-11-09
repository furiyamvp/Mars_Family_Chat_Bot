from sqlalchemy import Column, String, BigInteger, DateTime, ForeignKey, Table, Enum, func
from main.constants import EmployeeRole
from main.database import metadata

EmployeeModel = Table(
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


CategoryModel = Table(
    "category",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("name", String, nullable=False, unique=True),
    Column("description", String, nullable=False),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
    Column("employee_id", BigInteger, ForeignKey("employee.id", ondelete="SET NULL"), nullable=True),
)

ForbiddenWordModel = Table(
    "forbidden_word",
    metadata,
    Column("id", BigInteger, primary_key=True),
    Column("word", String, nullable=False, unique=True),
    Column("answer", String, nullable=False),
    Column("created_at", DateTime, default=func.now()),
    Column("updated_at", DateTime, onupdate=func.now()),
    Column("employee_id", BigInteger, ForeignKey("employee.id", ondelete="SET NULL"), nullable=True),
    Column("category_id", BigInteger, ForeignKey("category.id", ondelete="CASCADE"), nullable=True),
)
