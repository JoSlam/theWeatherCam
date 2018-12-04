function renderChart(container, name, weather_array) {            //highchart render function
    var today = new Date();
    if (container != null) {
        Highcharts.chart(container.id, {
            chart: {
                height: 400,
                width: null,
                // type: 'pie'
            },

            xAxis: {
                type: 'datetime',
                title: {
                    text: 'Date'
                }
            },

            title: {
                align: 'center',
                style: {
                    "color": "#CC6733"
                },
                text: name,
            },

            plotOptions: {
                series: {
                    pointStart: today.setDate(today.getDate() - 7),
                    pointInterval: 24 * 3600 * 1000 // one day
                }
            },

            tooltip: {
                formatter: function () {
                    return '<b>' + this.series.name + '</b><br/>' +
                        this.x + ': ' + this.y;
                }
            },

            series: [{
                name: name,
                data: weather_array
            }]
        });
    }
}


function loadChart(){
    var xhttp = new XMLHttpRequest();
    var url = 'http://localhost:8000/chart_data';             //reqeuest to localhost - needs to fix
    xhttp.onreadystatechange = function() {
        if(this.readyState === 4 && this.status === 200){
            var container_id = 0;
            var json_dat = JSON.parse(this.responseText);
            var highchart_containers = document.getElementsByName('highchart-container');
            if(json_dat != null && highchart_containers != null && highchart_containers.length > 0){
                for (let i in json_dat) {
                    renderChart(highchart_containers[container_id], i, json_dat[i]);
                    container_id++;
                }
            }
        }
    }
    xhttp.open('GET', url, true);
    xhttp.send();                   //send response
}

document.addEventListener('DOMContentLoaded', function(){
    loadChart();
});