function ajaxForm(){
    $.ajax({
        type: "POST",
        url: "/getMajorInfo",
        dataType: "json",
        success: function (data) {
            console.log(data);
            option['xAxis']['data'] = data['year'];
            option['series'][0]['data'] = data['rates_min'];
            option['series'][1]['data'] = data['rates_max'];
            myChart.setOption(option);
        }
    });
}