var Acart = document.querySelector('#Acart');
var Atotal = document.querySelector('#Atotal');

function addAppetizer(Aid){
    AppetizerId = '#appetizer'+ Aid;
    var nam = document.querySelector(AppetizerId).innerHTML;
    var radio = 'appetizer' + Aid;
    var pri = document.getElementsByName(radio)

    if(pri[0].checked){
        var price = pri[0].value;
    }
    
    else{
        price = pri[0].value;
    }

    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartsize = orders.length;

    //saving items and total in loc storage
    orders[cartsize] = [nam, price];
    localStorage.setItem('orders', JSON.stringify(orders));

    total = Number(total) + Number(price);
    localStorage.setItem('total', total);

    //updating number of item count
    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length; 
    butto = '<h5><button class="btn-danger" onclick="removeAppetizer('+ cartsize +')">X</button></h5>';

    Atotal.innerHTML = 'Total: '+ total + '$';
    Acart.innerHTML += '<li>'+ nam + '  '+ price + ' $' + butto + '</li>'; 
}
function AshoppingCart(){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    var cartsize = orders.length;
    Acart.innerHTML = '';
    for(let i = 0; i < cartsize; i++){
        butto = '<h5><button class="btn-danger" onclick="removeAppetizer('+ i +')">X</button></h5';
        Acart.innerHTML += '<li>'+ orders[i][0] + ': ' + orders[i][1] + ' $' + butto + '</li>';
    }  
    Atotal.innerHTML = 'Total: '+ total + '$';
}

AshoppingCart();

function removeAppetizer(n){
    var orders = JSON.parse(localStorage.getItem('orders'));
    var total = localStorage.getItem('total');
    total = Number(total) - Number(orders[n][0]);
    orders.splice(n,1);

    var cart = document.querySelector("#cart");
    cart.innerHTML = orders.length; 

    localStorage.setItem('orders', JSON.stringify(orders));
    localStorage.setItem('total', total);
 AshoppingCart();
}

