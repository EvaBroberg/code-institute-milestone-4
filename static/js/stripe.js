// $(function () {
//     $("#payment-form").submit(function () {
//         var form = this;
//         var card = {
//             number: $("#id_credit_card_number").val(),
//             expMonth: $("#id_expiry_month").val(),
//             expYear: $("#id_expiry_year").val(),
//             cvc: $("#id_cvv").val(),
//         };

//         Stripe.createToken(card, function (status, response) {
//             if (status === 200) {
//                 $("#credit-card-errors").hide();
//                 $("#id_stripe_id").val(response.id);

//                 // Prevent the credit card details from being submitted
//                 // to our server
//                 $("#id_credit_card_number").removeAttr("name");
//                 $("#id_cvv").removeAttr("name");
//                 $("#id_expiry_month").removeAttr("name");
//                 $("#id_expiry_year").removeAttr("name");

//                 form.submit();
//             } else {
//                 $("#stripe-error-message").text(response.error.message);
//                 $("#credit-card-errors").show();
//                 $("#validate_card_btn").attr("disabled", false);
//             }
//         });
//         return false;
//     });
// });

// Create a Stripe client.
var stripe = Stripe('pk_test_mad7JiUbrREpfoByUSybHG1g007YSkoeIm');

// Create an instance of Elements.
var elements = stripe.elements();

// Custom styling can be passed to options when creating an Element.
// (Note that this demo uses a wider set of styles than the guide below.)
var style = {
  base: {
    color: '#32325d',
    lineHeight: '18px',
    fontFamily: '"Helvetica Neue", Helvetica, sans-serif',
    fontSmoothing: 'antialiased',
    fontSize: '16px',
    '::placeholder': {
      color: '#aab7c4',
    },
  },
  invalid: {
    color: '#fa755a',
    iconColor: '#fa755a',
  },
};

// Create an instance of the card Element.
var card = elements.create('card', { style: style });

// Add an instance of the card Element into the `card-element` <div>.
card.mount('#card-element');

// Handle real-time validation errors from the card Element.
card.addEventListener('change', function (event) {
  var displayError = document.getElementById('card-errors');
  if (event.error) {
    displayError.textContent = event.error.message;
  } else {
    displayError.textContent = '';
  }
});

// Handle form submission.
var form = document.getElementById('payment-form');
form.addEventListener('submit', function (event) {
  event.preventDefault();

  stripe.createToken(card).then(function (result) {
    if (result.error) {
      // Inform the user if there was an error.
      var errorElement = document.getElementById('card-errors');
      errorElement.textContent = result.error.message;
    } else {
      // Send the token to your server.
      stripeTokenHandler(result.token);
    }
  });
});

var successElement = document.getElementById('stripe-token-handler');
document.querySelector('.wrapper').addEventListener('click', function () {
  successElement.className = 'is-hidden';
});

function stripeTokenHandler(token) {
  successElement.className = '';
  successElement.querySelector('.token').textContent = token.id;
  // Insert the token ID into the form so it gets submitted to the server
  var form = document.getElementById('payment-form');
  var hiddenInput = document.createElement('input');
  hiddenInput.setAttribute('type', 'hidden');
  hiddenInput.setAttribute('name', 'stripeToken');
  hiddenInput.setAttribute('value', token.id);
  form.appendChild(hiddenInput);

  // Submit the form
  form.submit();
}
