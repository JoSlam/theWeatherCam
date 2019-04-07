//Api url
const base_url = 'http://api.openweathermap.org/data/2.5/weather?q=';
const search_area = 'curepe, tt';
const api_key = '13ceb7203fe9f550a498f8e24d080268'
const units = 'metric';
const url = base_url + "" + search_area + '&APPID=' + api_key + '&units=' + units;

//document.addEventListener('DOMContentLoaded', getData);
function getData() {
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState === 4 && this.status === 200) {
            var jsonDat = JSON.parse(this.responseText); //parse response to string
            console.log(jsonDat);
            
            var table = `
            <tr>
                <th scope='row'>Date:</th>
                <td>${Date(jsonDat.dt)}</td>
            </tr>
            <tr>
                <th scope='row'>Wind speed:</th>
                <td>${jsonDat.wind.speed} m/s</td>
            </tr>
            <tr>
                <th scope='row'>Temperature</th>
                <td>${jsonDat.main.temp} °C</td>
            </tr>
            <tr>
                <th scope='row'>Humidity:</th>
                <td>${jsonDat.main.humidity} %</td>
            </tr>
            <tr>
                <th scope='row'>Pressure</th>
                <td>${jsonDat.main.pressure} hPa</td>
            </tr>
            `;
            if(document.getElementById('curr_weather') != null){
                document.getElementById('curr_weather').innerHTML = table;                 //update table contents
            }
        }
    }
    xhttp.open("GET", url, true);
    xhttp.send();                               //send request
}
