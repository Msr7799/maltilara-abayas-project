from flask import Blueprint, render_template, request, jsonify
from app.models import Abaya, Review
from app import db

bp = Blueprint('main', __name__)

@bp.route('/')
def index():
    featured_abayas = Abaya.query.limit(4).all()
    return render_template('index.html', featured_abayas=featured_abayas)

@bp.route('/gallery')
def gallery():
    abayas = Abaya.query.all()
    return render_template('gallery.html', abayas=abayas)

@bp.route('/product/<int:id>')
def product(id):
    abaya = Abaya.query.get_or_404(id)
    reviews = Review.query.filter_by(abaya_id=id).all()
    return render_template('product.html', abaya=abaya, reviews=reviews)

@bp.route('/submit_review', methods=['POST'])
def submit_review():
    # Implement review submission logic
    pass

@bp.route('/payment/<int:abaya_id>')
def payment(abaya_id):
    abaya = Abaya.query.get_or_404(abaya_id)
    return render_template('payment.html', abaya=abaya)

@bp.route('/process_payment', methods=['POST'])
def process_payment():
    # Implement payment processing logic
    pass