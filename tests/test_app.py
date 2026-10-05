import pytest

from traceit import create_app, db
from traceit.models import Category, Ticket, User


@pytest.fixture()
def app(tmp_path):
    db_file = tmp_path / "test.db"
    app = create_app(
        {
            "TESTING": True,
            "SECRET_KEY": "test",
            "SQLALCHEMY_DATABASE_URI": f"sqlite:///{db_file}",
        }
    )
    return app


@pytest.fixture()
def client(app):
    return app.test_client()


def test_index_responds(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b"Tickets" in response.data


def test_create_update_delete_ticket(app, client):
    with app.app_context():
        user = User.query.first()
        category = Category.query.first()
        user_id = user.id
        category_id = category.id

    response = client.post(
        "/tickets/new",
        data={
            "title": "No puedo ingresar al campus virtual",
            "description": "El usuario recibe un mensaje de credenciales invalidas.",
            "user_id": str(user_id),
            "category_id": str(category_id),
            "priority": "Alta",
            "status": "Abierto",
        },
        follow_redirects=True,
    )
    assert response.status_code == 200
    assert b"Ticket creado correctamente" in response.data

    with app.app_context():
        ticket = Ticket.query.one()
        ticket_id = ticket.id

    response = client.post(
        f"/tickets/{ticket_id}/edit",
        data={
            "title": "Acceso al campus virtual restablecido",
            "description": "Se restablecio la clave y se valido el ingreso correctamente.",
            "user_id": str(user_id),
            "category_id": str(category_id),
            "priority": "Media",
            "status": "Resuelto",
        },
        follow_redirects=True,
    )
    assert b"Ticket actualizado correctamente" in response.data

    response = client.post(f"/tickets/{ticket_id}/delete", follow_redirects=True)
    assert b"Ticket eliminado" in response.data

    with app.app_context():
        assert Ticket.query.count() == 0
