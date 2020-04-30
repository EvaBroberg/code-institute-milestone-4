// chart

window.onload = function () {
  var chart = new CanvasJS.Chart('chartContainer', {
    animationEnabled: true,
    theme: 'light2',
    title: {
      text: 'Daily Visitors',
    },
    axisY: {
      includeZero: false,
    },
    data: [
      {
        type: 'line',
        dataPoints: [
          { y: 450 },
          { y: 414 },
          {
            y: 520,
            indexLabel: 'highest',
            markerColor: 'red',
            markerType: 'triangle',
          },
          { y: 460 },
          { y: 450 },
          { y: 500 },
          { y: 480 },
          { y: 480 },
          {
            y: 410,
            indexLabel: 'lowest',
            markerColor: 'DarkSlateGrey',
            markerType: 'cross',
          },
          { y: 500 },
          { y: 480 },
          { y: 510 },
        ],
      },
    ],
  });
  setTimeout(function () {
    chart.render();
  }, 1000);
};

setTimeout(function () {
  $(document).ready(function () {
    // Counter
    $('.count').each(function () {
      $(this)
        .prop('Counter', 0)
        .animate(
          {
            Counter: $(this).text(),
          },
          {
            duration: 1000,
            easing: 'swing',
            step: function (now) {
              $(this).text(Math.ceil(now));
            },
          }
        );
    });

    //Todos
    $('#todo-form').submit(function (e) {
      const output = `
       <li class="collection-item">
         <div>
           ${$('#todo').val()}
           <a href="#!" class="secondary-content delete">
             <i class="material-icons">close</i>
           </a>
         </div>
       </li>
       `;

      $('.todos').append(output);

      Materialize.toast('Todo added', 3000);
      e.preventDefault();
    });

    //Delete todos
    $('.todos').on('click', '.delete', function (e) {
      $(this).parent().parent().remove();
      Materialize.toast('Todo deleted', 3000);
      e.preventDefault();
    });

    CKEDITOR.replace('body');
  });
}, 1000);
