document.getElementById('paymentMode').addEventListener('change', function () {
    var creditCardFields = document.getElementById('creditCardFields');

    if (this.value === 'creditCard' || this.value === 'debitCard') {
        creditCardFields.style.display = 'block';
    } else {
        creditCardFields.style.display = 'none';
    }
});

// Additional logic to handle the form submission
document.getElementById('paymentForm').addEventListener('submit', function (event) {
    event.preventDefault();

    // Add your logic here to handle the form submission
    var receiverName = document.getElementById('receiverName').value;
    var receiverAddress = document.getElementById('receiverAddress').value;
    var paymentMode = document.getElementById('paymentMode').value;

    if (paymentMode === 'creditCard' || paymentMode === 'debitCard') {
        // Additional validation for credit card fields
        var cardNumber = document.getElementById('cardNumber').value;
        var expDate = document.getElementById('expDate').value;
        var cvv = document.getElementById('cvv').value;

        // Add your logic to handle credit card details
        console.log('Credit Card Details:');
        console.log('Card Number:', cardNumber);
        console.log('Expiration Date:', expDate);
        console.log('CVV:', cvv);
    }

    // Add your logic to handle other payment modes

    // You can redirect or perform further actions based on the form data
    alert('Payment submitted successfully!');
});
