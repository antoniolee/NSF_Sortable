// <=============== START GRAPH JAVASCRIPT ==========================> 
        
    var emptySeries = [0,0,0,0,0,0];
    var value1, value2, value3, result;
    
      $.jqplot.config.enablePlugins = true;
      $("#generateGraphButton").on("click", generateGraph);
      
      $("#saveButton").on("click", function(){
          // Get values from the sliders
            value1 = $( "#amount1" ).val();
            value2 = $( "#amount2" ).val();
            value3 = $( "#amount3" ).val(); 
          var number = Math.floor((Math.random()*100)+1);
            result = number+"%";
         
          $.ajax({
              url:"{{=URL('default', 'save')}}",
              data: {'var1': value1, 'var2': value2, 'var3': value3, 'result':result }
          })      
      //    alert("Entry Saved");          
      });
 
        function generateGraph(state){
            // Clear the chart div before generating a new one
          $( "#chartDiv" ).empty();

            var series;
        
        var ran1 = Math.floor((Math.random()*10)-(Math.random()*10));
        var ran2 = Math.floor((Math.random()*10)-(Math.random()*10));
        var ran3 = Math.floor((Math.random()*10)-(Math.random()*10));

        if(state == 0){
            series = emptySeries;
        } else {
            series = [ran1,ran2,ran3];   
        }
          
          plot1 = $.jqplot('chartDiv', [series], {
              // Only animate if we're not using excanvas (not in IE 7 or IE 8)..
              animate: !$.jqplot.use_excanvas,
              seriesDefaults:{
                  renderer:$.jqplot.BarRenderer,
                  pointLabels: { show: true }
              },
              axes: {
                  xaxis: {
                      renderer: $.jqplot.CategoryAxisRenderer,
                  },     
              
                  yaxis:{
                      min:-10,
                      max:10,
                      labelRenderer: $.jqplot.CanvasAxisLabelRenderer 
                  }
              },
              highlighter: { show: true }
          });
        }
 
 // <================= ADD EMPTY CHART ===========================>
        
        generateGraph();
        
  // <================= End Graph Javascript ======================>
