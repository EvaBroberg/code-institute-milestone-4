// var stripe = Stripe('pk_test_mad7JiUbrREpfoByUSybHG1g007YSkoeIm');
// var elements = stripe.elements();

// var card = elements.create('card', {
//   style: {
//     base: {
//       fontFamily: 'Arial, sans-serif',
//       fontSize: '8px',
//       color: '#C1C7CD',
//     },
//     invalid: {
//       color: 'red',
//     },
//   },
// });
// card.mount('#card-element');

// var stripeResponseHandler = function (status, response) {
//   var form = document.getElementById('payment-form');
//   if (response.error) {
//     var errorElement = document.getElementById('card-errors');
//     errorElement.textContent = result.error.message;
//   } else {
//     var token = response.id;

//     var form = document.getElementById('payment-form');
//     var hiddenInput = document.createElement('input');
//     hiddenInput.setAttribute('type', 'hidden');
//     hiddenInput.setAttribute('name', 'stripeToken');
//     hiddenInput.setAttribute('value', token);
//     form.appendChild(hiddenInput);

//     form.submit();
//   }
// };

// var form = document.getElementById('payment-form');
// form.addEventListener('submit', function (e) {
//   e.preventDefault();
//   Stripe.card.createToken(form, stripeResponseHandler);
// });

// function stripeTokenHandler(token) {
//   // Insert the token ID into the form so it gets submitted to the server
//   var form = document.getElementById('payment-form');
//   var hiddenInput = document.createElement('input');
//   hiddenInput.setAttribute('type', 'hidden');
//   hiddenInput.setAttribute('name', 'stripeToken');
//   hiddenInput.setAttribute('value', token.id);
//   form.appendChild(hiddenInput);

//   // Submit the form
//   form.submit();
// }

// function createToken() {
//   stripe.createToken(card).then(function (result) {
//     if (result.error) {
//       // Inform the user if there was an error
//       var errorElement = document.getElementById('card-errors');
//       errorElement.textContent = result.error.message;
//     } else {
//       // Send the token to your server
//       stripeTokenHandler(result.token);
//     }
//   });
// }

// // Create a token when the form is submitted.
// var form = document.getElementById('payment-form');
// form.addEventListener('submit', function (e) {
//   e.preventDefault();
//   createToken();
// });

// cardElement.addEventListener('change', function (event) {
//   var displayError = document.getElementById('card-errors');
//   if (event.error) {
//     displayError.textContent = event.error.message;
//   } else {
//     displayError.textContent = 'ERROORRRR';
//   }
// });
