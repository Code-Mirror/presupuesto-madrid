// Theme custom js methods
$(document).ready(function(){

  var addChartsAlert = function(selector){
    var str = {
      'es': 'Datos actualizados a 31 de agosto de 2016',
      'en': 'Data up to 31st August 2016'
    };
    var cont = $(selector);
    if( cont.size() > 0 ){
      cont.prepend('<div class="alert alert-data-update">'+str[ $('html').attr('lang') ]+'</div>');
    }
  };

  var addYearSelectorCustomLabels = function(){
    var str2017 = {
      'es': 'proyecto',
      'en': 'pending approval',
    };

    $('.data-controllers .layout-slider .slider .slider-tick-label').each(function(){
      var val = $(this).html();
      if (val === '2017'){
        $(this).html(val + '<br/><small><i> ('+ str2017[ $('html').attr('lang') ] +')</i></small>');
      }
    });
  };

  addYearSelectorCustomLabels();

  addChartsAlert('.policies-chart');
  addChartsAlert('.sankey-container');
});