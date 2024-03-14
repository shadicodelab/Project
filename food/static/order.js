var Acart = document.querySelector('#Acart');
var Atotal = document.querySelector('#Atotal');
var cartItemCount = 0; // New variable to keep track of the number of items in the cart

// Function to update the cart icon count
function updateCartIconCount(count) {
    var cartIcon = document.querySelector('#cart-icon');
    cartIcon.textContent = count;
}

function addAppetizer(Aname, Aprice) {
    // Check if the item is already in the cart
    var existingItem = Array.from(Acart.children).find(item => item.textContent.includes(Aname));

    if (!existingItem) {
        var listItem = document.createElement('li');
        listItem.textContent = `${Aname} - $${Aprice}`;

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
    }
}

function removeAppetizer(item, price) {
    Acart.removeChild(item);
    updateTotal(-parseFloat(price)); // Subtract the price when removing an item

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

    localStorage.setItem('total', newTotal);
}

document.addEventListener('DOMContentLoaded', function() {
    var previousOrders = JSON.parse(localStorage.getItem('orders'));

    if (previousOrders && previousOrders.length > 0) {
        previousOrders.forEach(order => {
            addAppetizer(order.name, order.price);
        });
    }
});

document.addEventListener('click', function(event) {
    if (event.target.classList.contains('btn-primary')) {
        var card = event.target.closest('.card');
        var Aname = card.querySelector('.card-title').textContent.trim();
        var Aprice = card.querySelector('.card-text').textContent.trim().replace('$', '');

        addAppetizer(Aname, Aprice);
    }
});
