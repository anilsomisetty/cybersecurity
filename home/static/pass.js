/* PLACEHOLD
 *
 * This function cycles through all of the common
 * text inputs on the page and converts the label
 * to placeholder text. The labels are then given
 * the 'sr-only' class for hiding.
 *
 * If the input has class 'no-placehold' this operation
 * is skipped.
 */
function placehold()
{
  if(Modernizr.input.placeholder)
  {
    var inputs = [
      'input[type="text"]',
      'input[type="tel"]',
      'input[type="password"]',
      'textarea'
    ];

    $(inputs.join(", ")).each(function(){	
      var id   = $(this).attr('id');
      var text = $('label[for="' + id + '"]').html();

      // If it's not explicitly stated that we don't want
      // the label converted, we convert it.
      if (!$(this).hasClass('no-placehold'))
      {
        $('label[for="' + id + '"]').addClass('sr-only');
        $(this).attr('placeholder', text);
      }
    });
  }
}

$(document).ready(function() {
placehold();
});