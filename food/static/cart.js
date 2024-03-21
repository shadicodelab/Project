document.addEventListener('DOMContentLoaded', function() {
    // Selecting necessary elements
    var orderedItemsList = document.querySelector('#ordered-items-list');
    var totalElement = document.querySelector('#total');

    // Function to update the order list and total
    function updateOrderList() {
        // Clear the existing items in the list
        orderedItemsList.innerHTML = '';
        
        // Retrieve cart items from localStorage
        var orders = JSON.parse(localStorage.getItem('orders')) || [];
        var total = parseFloat(localStorage.getItem('total')) || 0;

        // Display each item in the order list
        orders.forEach(function(order) {
            var listItem = document.createElement('li');
            listItem.textContent = `${order.name} - $${order.price.toFixed(2)}`;
            orderedItemsList.appendChild(listItem);
        });

        // Update total display
        totalElement.textContent = `Total: $${total.toFixed(2)}`;
    }

    // Update order list on page load
    updateOrderList();

    // Event listener for changes in the cart
    window.addEventListener('storage', function(event) {
        // Check if the storage event is related to the cart
        if (event.key === 'orders' || event.key === 'total') {
            // Update the order list and total
            updateOrderList();
        }
    });
});
