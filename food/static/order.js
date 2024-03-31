var Acart = document.querySelector('#Acart');
var Atotal = document.querySelector('#Atotal');
var cartItemCount = 0;

function updateCartIconCount(count) {
    var cartIcon = document.querySelector('#cart-icon');
    cartIcon.textContent = count;
}

function addAppetizer(Aname, Aprice) {
    // Check if the item is already in the cart
    var existingItem = Acart.querySelector(`li[data-name="${Aname}"][data-price="${Aprice}"]`);

    if (!existingItem) {
        var listItem = document.createElement('li');
        listItem.textContent = `${Aname} - $${Aprice}`;
        listItem.setAttribute('data-name', Aname);
        listItem.setAttribute('data-price', Aprice);

        // Add remove button
        var removeButton = document.createElement('button');
        removeButton.textContent = 'X';
        removeButton.classList.add('btn', 'btn-danger', 'btn-sm', 'remove-btn');
        removeButton.addEventListener('click', function() {
            removeAppetizer(listItem, Aprice);
        });

        listItem.appendChild(removeButton);
        Acart.appendChild(listItem);

        updateTotal(Aprice);

        // Increment cart item count and update cart icon
        cartItemCount++;
        updateCartIconCount(cartItemCount);

        // Store the added item in localStorage
        var order = { name: Aname, price: Aprice };
        var previousOrders = JSON.parse(localStorage.getItem('orders')) || [];
        previousOrders.push(order);
        localStorage.setItem('orders', JSON.stringify(previousOrders));
    }
}

function removeAppetizer(item, price) {
    Acart.removeChild(item);
    updateTotal(-parseFloat(price));

    // Update localStorage
    var currentTotal = parseFloat(localStorage.getItem('total'));
    var newTotal = currentTotal - parseFloat(price);
    localStorage.setItem('total', newTotal);

    // Remove from the orders in localStorage
    var previousOrders = JSON.parse(localStorage.getItem('orders')) || [];
    previousOrders = previousOrders.filter(order => order.price !== price);
    localStorage.setItem('orders', JSON.stringify(previousOrders));

    // Decrement cart item count and update cart icon
    cartItemCount--;
    updateCartIconCount(cartItemCount);
}

function updateTotal(price) {
    var currentTotal = parseFloat(Atotal.textContent.split('$')[1]);
    var newTotal = currentTotal + parseFloat(price);
    Atotal.textContent = `Total: $${newTotal.toFixed(1)}`;

    localStorage.setItem('total', newTotal.toFixed(1));
}

document.addEventListener('DOMContentLoaded', function() {
    var previousOrders = JSON.parse(localStorage.getItem('orders'));

    if (previousOrders && previousOrders.length > 0) {
        previousOrders.forEach(order => {
            addAppetizer(order.name, order.price);
        });
    }

    var previousTotal = parseFloat(localStorage.getItem('total'));
    if (!isNaN(previousTotal)) {
        Atotal.textContent = `Total: $${previousTotal.toFixed(1)}`;
    }

    // Update cart item count and icon
    cartItemCount = previousOrders.length;
    updateCartIconCount(cartItemCount);
});

document.addEventListener('click', function(event) {
    if (event.target.classList.contains('btn-primary')) {
        var card = event.target.closest('.card');
        var Aname = card.querySelector('.card-title').textContent.trim();
        var Aprice = card.querySelector('.card-text').textContent.trim().replace('Price: Ksh', '').trim();

        // Check if the item is already in the cart (localStorage)
        var previousOrders = JSON.parse(localStorage.getItem('orders')) || [];
        var itemExists = previousOrders.some(order => order.name === Aname && order.price === Aprice);

        if (!itemExists) {
            addAppetizer(Aname, Aprice);
        }
    }
});
