from flask import Blueprint, render_template
from flask_login import login_required, current_user

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
@login_required
def index():
    return render_template('index.html', user=current_user)


@main_bp.route('/dashboard')
@login_required
def dashboard():

    # Dados de teste (até ligar no banco)
    stats = {
        "racks": 4,
        "cables": 120,
        "rooms": 8,
        "open_tickets": 3
    }

    activities = [
        {"description": "Cabo adicionado ao Rack 02", "time": "Há 10 minutos"},
        {"description": "Novo chamado aberto por TI", "time": "Há 1 hora"},
        {"description": "Mapeamento atualizado na sala 3", "time": "Ontem"},
    ]

    return render_template(
        'dashboard.html',
        user=current_user,
        stats=stats,
        activities=activities
    )
