var nam = document.querySelector("#name");
var price = document.querySelector("#price");
var bill = document.querySelector("#total");
var rm = document.querySelector("#rm");


function shoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartsize = orders.length;

    nam.innerHTML = '<h4>Name</h4>';
    price.innerHTML = '<h4>Price<h4>';
    rm.innerHTML = '<h4><br><h4>';


    for(let i = 0; i < cartsize; i++){
        rm.innerHTML += '<h5><button class="btn-danger" onclick="removeItem('+ i +')">X</button></h5>';
        nam.innerHTML += '<h5>' + orders[i][0] + '</h5>'
        price.innerHTML += '<h5>' + orders[i][1] + '</h5>'
    }  
    bill.innerHTML = 'Total: '+ total + '$';
}

shoppingCart();

function removeItem(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][1]);
    orders.splice(n,1);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length; 

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
    shoppingCart();
}

var note = document.querySelector('#message');

function order(){
    var msg = note.value;
    var orders = localStorage.getItem('orders');
    var ur = 'order';
    var orderData = {};
    orderData['orders'] = orders;
    orderData['note'] = msg;
    $.ajax({
        url: ur,
        type: "POST",
        data: orderData,
        headers: {'X-Requested-With': 'XMLHttpRequest'},
        success: function(data){
           window.location.replace('admin')
           localStorage.setItem('orders', JSON.stringify(orders));
           localStorage.setItem('total', total);
        }
    })

}

