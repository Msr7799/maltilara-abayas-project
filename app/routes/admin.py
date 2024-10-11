from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app.models import Abaya, Order, User
from app import db
from app.forms import AbayaForm

admin = Blueprint('admin', __name__)

@admin.route('/admin')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash('غير مصرح لك بالوصول إلى لوحة التحكم.', 'error')
        return redirect(url_for('main.index'))
    return render_template('admin.html')

@admin.route('/admin/abayas')
@login_required
def admin_abayas():
    if not current_user.is_admin:
        flash('غير مصرح لك بالوصول إلى هذه الصفحة.', 'error')
        return redirect(url_for('main.index'))
    abayas = Abaya.query.all()
    return render_template('admin_abayas.html', abayas=abayas)

@admin.route('/admin/add_abaya', methods=['GET', 'POST'])
@login_required
def add_abaya():
    if not current_user.is_admin:
        flash('غير مصرح لك بالوصول إلى هذه الصفحة.', 'error')
        return redirect(url_for('main.index'))
    form = AbayaForm()
    if form.validate_on_submit():
        abaya = Abaya(name=form.name.data,
                      description=form.description.data,
                      price=form.price.data,
                      stock=form.stock.data)
        # هنا يمكنك إضافة منطق معالجة الصورة المرفوعة
        db.session.add(abaya)
        db.session.commit()
        flash('تمت إضافة العباية بنجاح.', 'success')
        return redirect(url_for('admin.admin_abayas'))
    return render_template('add_abaya.html', form=form)

@admin.route('/admin/edit_abaya/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_abaya(id):
    if not current_user.is_admin:
        flash('غير مصرح لك بالوصول إلى هذه الصفحة.', 'error')
        return redirect(url_for('main.index'))
    abaya = Abaya.query.get_or_404(id)
    form = AbayaForm(obj=abaya)
    if form.validate_on_submit():
        abaya.name = form.name.data
        abaya.description = form.description.data
        abaya.price = form.price.data
        abaya.stock = form.stock.data
        # هنا يمكنك إضافة منطق معالجة الصورة المرفوعة إذا تم تحديثها
        db.session.commit()
        flash('تم تحديث العباية بنجاح.', 'success')
        return redirect(url_for('admin.admin_abayas'))
    return render_template('add_abaya.html', form=form, abaya=abaya)

@admin.route('/admin/delete_abaya/<int:id>')
@login_required
def delete_abaya(id):
    if not current_user.is_admin:
        flash('غير مصرح لك بالوصول إلى هذه الصفحة.', 'error')
        return redirect(url_for('main.index'))
    abaya = Abaya.query.get_or_404(id)
    db.session.delete(abaya)
    db.session.commit()
    flash('تم حذف العباية بنجاح.', 'success')
    return redirect(url_for('admin.admin_abayas'))

@admin.route('/admin/orders')
@login_required
def admin_orders():
    if not current_user.is_admin:
        flash('غير مصرح لك بالوصول إلى هذه الصفحة.', 'error')
        return redirect(url_for('main.index'))
    orders = Order.query.all()
    return render_template('admin_orders.html', orders=orders)

@admin.route('/admin/update_order_status', methods=['POST'])
@login_required
def update_order_status():
    if not current_user.is_admin:
        return jsonify({'success': False, 'message': 'غير مصرح لك بتنفيذ هذا الإجراء.'}), 403
    order_id = request.form.get('order_id')
    new_status = request.form.get('status')
    order = Order.query.get_or_404(order_id)
    order.status = new_status
    db.session.commit()
    return jsonify({'success': True, 'message': 'تم تحديث حالة الطلب بنجاح.'})