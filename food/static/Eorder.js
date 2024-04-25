document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    const orderList = document.getElementById('Ecart');
    const totalElement = document.getElementById('Etotal');
    let total = 0;

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();

            const entreeName = this.dataset.name;
            const entreePrice = parseFloat(this.dataset.price);

            // Create a new list item for the order list
            const listItem = document.createElement('li');
            listItem.textContent = `${entreeName} - $${entreePrice.toFixed(2)}`;

            // Add the new item to the order list
            orderList.appendChild(listItem);

            // Update the total price
            total += entreePrice;
            totalElement.textContent = `Total: $${total.toFixed(2)}`;
        });
    });
});
