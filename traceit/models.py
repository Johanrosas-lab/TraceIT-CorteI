from datetime import datetime, timezone

from . import db


class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(150), unique=True, nullable=False)
    role = db.Column(db.String(50), nullable=False, default="Usuario")

    tickets = db.relationship("Ticket", back_populates="user", lazy=True)

    def __repr__(self):
        return f"<User {self.email}>"


class Category(db.Model):
    __tablename__ = "categories"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.String(220), nullable=True)

    tickets = db.relationship("Ticket", back_populates="category", lazy=True)

    def __repr__(self):
        return f"<Category {self.name}>"


class Ticket(db.Model):
    __tablename__ = "tickets"

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(140), nullable=False)
    description = db.Column(db.Text, nullable=False)
    priority = db.Column(db.String(20), nullable=False, default="Media")
    status = db.Column(db.String(25), nullable=False, default="Abierto")
    created_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
    )
    updated_at = db.Column(
        db.DateTime(timezone=True),
        nullable=False,
        default=lambda: datetime.now(timezone.utc),
        onupdate=lambda: datetime.now(timezone.utc),
    )

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey("categories.id"), nullable=False)

    user = db.relationship("User", back_populates="tickets")
    category = db.relationship("Category", back_populates="tickets")

    def __repr__(self):
        return f"<Ticket {self.id}: {self.title}>"


def seed_reference_data():
    """Crea usuarios y categorías mínimas solo si la base está vacía."""
    if User.query.count() == 0:
        db.session.add_all(
            [
                User(name="Johan Rosas", email="johan.rosas@universidad.edu", role="Administrador TI"),
                User(name="Laura Gómez", email="laura.gomez@universidad.edu", role="Docente"),
                User(name="Carlos Pérez", email="carlos.perez@universidad.edu", role="Estudiante"),
            ]
        )

    if Category.query.count() == 0:
        db.session.add_all(
            [
                Category(name="Acceso", description="Problemas de ingreso y credenciales"),
                Category(name="Conectividad", description="Internet, Wi-Fi y red"),
                Category(name="Hardware", description="Equipos y periféricos"),
                Category(name="Software", description="Aplicaciones y sistemas"),
            ]
        )

    db.session.commit()
