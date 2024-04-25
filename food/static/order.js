document.addEventListener('DOMContentLoaded', function() {
    const addToCartButtons = document.querySelectorAll('.add-to-cart-btn');
    const selectedPrices = [];

    addToCartButtons.forEach(button => {
        button.addEventListener('click', function(event) {
            event.preventDefault();

            const appetizerName = this.dataset.name;
            const appetizerPrice = parseFloat(this.dataset.price);

            // Add the price to the selectedPrices array
            selectedPrices.push(appetizerPrice);

            // Create a new list item for the order list
            const listItem = document.createElement('li');
            listItem.textContent = `${appetizerName} - Ksh ${appetizerPrice.toFixed(2)}`;

            // Add the new item to the order list
            const orderList = document.getElementById('Acart');
            orderList.appendChild(listItem);

            // Update the total price
            const totalElement = document.getElementById('Atotal');
            const newTotal = selectedPrices.reduce((acc, curr) => acc + curr, 0);
            totalElement.textContent = `Total: Ksh ${newTotal.toFixed(2)}`;
        });
    });
});
