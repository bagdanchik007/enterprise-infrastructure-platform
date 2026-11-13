from datetime import datetime

from sqlalchemy import CheckConstraint, DateTime, String, func
from sqlalchemy.orm import Mapped, mapped_column

from app.db.base import Base


class Server(Base):
    """Database model representing an IT infrastructure server."""

    __tablename__ = "servers"

    __table_args__ = (
        CheckConstraint(
            "status IN ('online', 'offline', 'maintenance', 'unknown')",
            name="ck_servers_status",
        ),
    )

    id: Mapped[int] = mapped_column(
        primary_key=True,
        autoincrement=True,
    )

    hostname: Mapped[str] = mapped_column(
        String(255),
        unique=True,
        index=True,
        nullable=False,
    )

    ip_address: Mapped[str] = mapped_column(
        String(45),
        nullable=False,
    )

    operating_system: Mapped[str | None] = mapped_column(
        String(100),
        nullable=True,
    )

    status: Mapped[str] = mapped_column(
        String(20),
        default="unknown",
        nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        nullable=False,
    )

    updated_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        server_default=func.now(),
        onupdate=func.now(),
        nullable=False,
    )

    def __repr__(self) -> str:
        return (
            f"Server(id={self.id!r}, "
            f"hostname={self.hostname!r}, "
            f"status={self.status!r})"
        )
