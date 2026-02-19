
from flask import Flask, render_template, request, redirect, url_for, session, flash
import os
import json
from datetime import datetime
app = Flask(__name__)
app.secret_key = 'secret_key_for_session' 

# Ruta pentru pagina principala
@app.route('/')
def home():
    return render_template('base.html')

# Ruta pentru pagina produselor
@app.route('/products')
def products():
    products = [
        {'id': 1, 'name': 'CFMOTO 450L', 'price': 6400},
        {'id': 2, 'name': 'CFMOTO 600L OVERLAND', 'price': 7900},
        {'id': 3, 'name': 'CFMOTO 1000 PREMIUM', 'price': 12900},
        {'id': 4, 'name': 'CFMOTO 850 XC', 'price': 9800},
        {'id': 5, 'name': 'CFMOTO 1000 OVERLAND', 'price': 11700},
        {'id': 6, 'name': 'CFMOTO X10 SPECIAL EDITION', 'price': 15000}
    ]
    return render_template('products.html', products=products)

# Adaugare produs
@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    # Lista de produse
    products = [
        {'id': 1, 'name': 'CFMOTO 450L', 'price': 6400},
        {'id': 2, 'name': 'CFMOTO 600L OVERLAND', 'price': 7900},
        {'id': 3, 'name': 'CFMOTO 1000 PREMIUM', 'price': 12900},
        {'id': 4, 'name': 'CFMOTO 850 XC', 'price': 9800},
        {'id': 5, 'name': 'CFMOTO 1000 OVERLAND', 'price': 11700},
        {'id': 6, 'name': 'CFMOTO X10 SPECIAL EDITION', 'price': 15000}
    ]

    # Gasire produs corespunzator dupa id
    product = next((p for p in products if p['id'] == product_id), None)

    if product:
        try:
            quantity = int(request.form['quantity'])
        except ValueError:
            quantity = 1  

        # Cos curent
        cart_items = session.get('cart_items', [])

        # Verific daca am deja produsul respectiv in cos
        existing_item = next((item for item in cart_items if item['id'] == product_id), None)

        if existing_item:
            existing_item['quantity'] += quantity
        else:
            cart_items.append({
                'id': product['id'],
                'name': product['name'],
                'price': product['price'],
                'quantity': quantity
            })

        # Actualizare nr produse
        session['cart_items'] = cart_items

    return redirect(url_for('cart'))


# Cart
@app.route('/cart')
def cart():
    cart_items = session.get('cart_items', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)
    return render_template('cart.html', cart_items=cart_items, total_price=total_price)

# Stergere din cos
@app.route('/remove_from_cart/<int:product_id>')
def remove_from_cart(product_id):
    cart_items = session.get('cart_items', [])
    cart_items = [item for item in cart_items if item['id'] != product_id]
    session['cart_items'] = cart_items
    return redirect(url_for('cart'))

# Checkout
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    cart_items = session.get('cart_items', [])
    total_price = sum(item['price'] * item['quantity'] for item in cart_items)

    if request.method == 'POST':
        # Preia datele din formular
        full_name = request.form.get('full_name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        address = request.form.get('address')
        payment_method = request.form.get('payment_method')

        order_data = {
            'timestamp': datetime.now().isoformat(),
            'full_name': full_name,
            'email': email,
            'phone': phone,
            'address': address,
            'payment_method': payment_method,
            'items': cart_items,
            'total_price': total_price
        }

        # Salvare informatii comanda
        os.makedirs('submitted-data', exist_ok=True)
        filename = f"submitted-data/order_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(order_data, f, indent=4, ensure_ascii=False)

        # Golire cos
        session['cart_items'] = [] 

 
        return redirect(url_for('thank_you', name=full_name))

    
    return render_template('checkout.html', cart_items=cart_items, total_price=total_price)


# Cart


# Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.context_processor
def cart_quantity_context():
    cart_items = session.get('cart_items', [])
    total_quantity = sum(item['quantity'] for item in cart_items)
    return dict(cart_quantity=total_quantity)


@app.route('/thank_you')
def thank_you():
    name = request.args.get('name', 'Client')
    return render_template('thank_you.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
