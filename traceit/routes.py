from flask import Blueprint, flash, redirect, render_template, request, url_for

from . import db
from .models import Category, Ticket, User

bp = Blueprint("tickets", __name__)

PRIORITIES = ("Baja", "Media", "Alta")
STATUSES = ("Abierto", "En proceso", "Resuelto")


def _reference_data():
    return {
        "users": User.query.order_by(User.name).all(),
        "categories": Category.query.order_by(Category.name).all(),
        "priorities": PRIORITIES,
        "statuses": STATUSES,
    }


def _validate_ticket_form(form):
    errors = []
    title = form.get("title", "").strip()
    description = form.get("description", "").strip()
    user_id = form.get("user_id", "").strip()
    category_id = form.get("category_id", "").strip()
    priority = form.get("priority", "Media")
    status = form.get("status", "Abierto")

    if len(title) < 5:
        errors.append("El título debe tener al menos 5 caracteres.")
    if len(description) < 10:
        errors.append("La descripción debe tener al menos 10 caracteres.")
    if not user_id.isdigit() or db.session.get(User, int(user_id)) is None:
        errors.append("Seleccione un usuario válido.")
    if not category_id.isdigit() or db.session.get(Category, int(category_id)) is None:
        errors.append("Seleccione una categoría válida.")
    if priority not in PRIORITIES:
        errors.append("La prioridad seleccionada no es válida.")
    if status not in STATUSES:
        errors.append("El estado seleccionado no es válido.")

    cleaned = {
        "title": title,
        "description": description,
        "user_id": int(user_id) if user_id.isdigit() else None,
        "category_id": int(category_id) if category_id.isdigit() else None,
        "priority": priority,
        "status": status,
    }
    return cleaned, errors


@bp.route("/")
def index():
    status_filter = request.args.get("status", "").strip()
    query = Ticket.query.order_by(Ticket.created_at.desc())
    if status_filter in STATUSES:
        query = query.filter_by(status=status_filter)
    return render_template(
        "tickets/list.html",
        tickets=query.all(),
        statuses=STATUSES,
        status_filter=status_filter,
    )


@bp.route("/tickets/new", methods=("GET", "POST"))
def create():
    if request.method == "POST":
        data, errors = _validate_ticket_form(request.form)
        if not errors:
            ticket = Ticket(**data)
            db.session.add(ticket)
            db.session.commit()
            flash("Ticket creado correctamente.", "success")
            return redirect(url_for("tickets.detail", ticket_id=ticket.id))
        for error in errors:
            flash(error, "danger")

    return render_template("tickets/form.html", ticket=None, **_reference_data())


@bp.route("/tickets/<int:ticket_id>")
def detail(ticket_id):
    ticket = db.get_or_404(Ticket, ticket_id)
    return render_template("tickets/detail.html", ticket=ticket)


@bp.route("/tickets/<int:ticket_id>/edit", methods=("GET", "POST"))
def edit(ticket_id):
    ticket = db.get_or_404(Ticket, ticket_id)
    if request.method == "POST":
        data, errors = _validate_ticket_form(request.form)
        if not errors:
            for field, value in data.items():
                setattr(ticket, field, value)
            db.session.commit()
            flash("Ticket actualizado correctamente.", "success")
            return redirect(url_for("tickets.detail", ticket_id=ticket.id))
        for error in errors:
            flash(error, "danger")

    return render_template("tickets/form.html", ticket=ticket, **_reference_data())


@bp.route("/tickets/<int:ticket_id>/delete", methods=("POST",))
def delete(ticket_id):
    ticket = db.get_or_404(Ticket, ticket_id)
    db.session.delete(ticket)
    db.session.commit()
    flash("Ticket eliminado.", "warning")
    return redirect(url_for("tickets.index"))
