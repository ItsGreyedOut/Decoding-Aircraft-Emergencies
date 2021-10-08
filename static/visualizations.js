console.log(dataset);


// Default Flight Summary Table
let one = 'ARG1511_20180101';

let flight_info = "";
for (let f=0; f<dataset[1][0]['Flight ID'].length;f++) {
    if (dataset[1][0]['Flight ID'][f] = one) {
        for (const [key, value] of Object.entries(dataset[1][0])) { 
            flight_info += key+" : "+value[f]+"<br>";
        }
    }
};

document.getElementById("flight_info").innerHTML = flight_info


// Default Aircraft Info Table
let meta = dataset[2][0];
let aircraft = "";
for (const [key, value] of Object.entries(meta)) {
    aircraft += key+" : "+value+"<br>";
}
document.getElementById("aircraft_info").innerHTML = aircraft


// Default Altitude/Speed Plot
labels = [];
for (let i = 0; i < dataset[0][0]['Squawk'].length; i++) {
    labels.push(`Squawk: ${dataset[0][0]['Squawk'][i]}`);
};

let trace1 = {
    x: dataset[0][0]['timestamp'],
    y: dataset[0][0]['altitude'],
    text: labels,
    type: 'line',
    name: "Altitude (ft.)"
};

let trace2 = {
    x: dataset[0][0]['timestamp'],
    y: dataset[0][0]['groundspeed'],
    text: labels,
    type: 'line',
    yaxis: 'y2',
    name: "Groundspeed (kts.)"
};
var layout1 = {
    title: {
        text: 'Flight Telemetry'
    },
    xaxis: {
        title: {text:'Time'}
    },
    yaxis: {
        title: {text:'Altitude (ft.)'}
    },
    yaxis2: {
        title: 'Groundspeed (kts.)',
        overlaying: 'y',
        side: 'right'
    },
    legend: {
        x: 0.8,
        y: 1.2
    }
};
var data1 = [trace1,trace2];
Plotly.newPlot("line",data1,layout1)

/*
for (var j = 0; j < dataset[].length; j++) {
    var dropdown = document.getElementById("selDataset");
    var opt = document.createElement("option"); 
    opt.text = subj[j].toString();
    opt.value = subj[j].toString();
    dropdown.options.add(opt);
};


d3.selectAll("#selDataset").on("change", change_flight);

function change_flight() {
    var dropdownMenu = d3.select("#selDataset");
    var new_flight = dropdownMenu.property("value");
    window.location.href = ('http://127.0.0.1:5000/flight_dashboard'+new_flight);
}
*/

/*
// Default Flight Trajectory Map
var street = L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
});

var topo = L.tileLayer('https://{s}.tile.opentopomap.org/{z}/{x}/{y}.png', {
	attribution: 'Map data: &copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors, <a href="http://viewfinderpanoramas.org">SRTM</a> | Map style: &copy; <a href="https://opentopomap.org">OpenTopoMap</a> (<a href="https://creativecommons.org/licenses/by-sa/3.0/">CC-BY-SA</a>)'
});

// Importing Data
var url = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

d3.json(url).then(function(response) {
    console.log(response)

    var quakeMarkers = [];

    for (var i = 0; i < response.features.length; i++) {
        var location = response.features[i];
    
        if (location) {

            if (location.geometry.coordinates[2] < 10) {color = 'green'}
            else if (location.geometry.coordinates[2] < 30) {color = 'greenyellow'}
            else if (location.geometry.coordinates[2] < 50) {color = 'yellow'}
            else if (location.geometry.coordinates[2] < 70) {color = 'orange'}
            else if (location.geometry.coordinates[2] < 90) {color = 'orangered'}
            else {color = 'red'}

            quakeMarkers.push(
                L.circle([location.geometry.coordinates[1], location.geometry.coordinates[0]],
                    {
                        color: 'black',
                        weight: 1,
                        fillColor: color,
                        fillOpacity: 0.6,
                        radius: Math.sqrt(Math.abs(location.properties.mag)) ** 2 * 10000
                    })
                    .bindPopup("<h3>Magnitude "+location.properties.mag+"</h3><hr>"
                        +'<span style="font-weight: bold">Location:</span> ' + location.properties.place 
                        + '<br><span style="font-weight: bold">Depth:</span> ' + location.geometry.coordinates[2]
                        + '<br><span style="font-weight: bold">ID:</span> ' + location.id
                        )
            )
        }
      };
    
    var url2 = "tectonic.json";

    d3.json(url2).then(function(tec) {
        console.log(tec)

        var tectonicMarkers = [];

        for (var i=0; i < tec.features.length; i++) {
            var location = tec.features[i];
            for (var x=0; x < location.geometry.coordinates.length; x++) {
                var tmp = location.geometry.coordinates[x][0];
                location.geometry.coordinates[x][0] = location.geometry.coordinates[x][1]
                location.geometry.coordinates[x][1] = tmp;
            };

            tectonicMarkers.push(
                L.polyline([location.geometry.coordinates],
                    {color: 'black',weight: 3})
                    .bindPopup("<h3>Boundary Name: "+location.properties.Name+"</h3><hr>"
                        +'<span style="font-weight: bold">Plate A:</span> ' + location.properties.PlateA 
                        + '<br><span style="font-weight: bold">Plate B:</span> ' + location.properties.PlateB
                        + '<br><span style="font-weight: bold">Source:</span> ' + location.properties.Source 
                        )
            )    
        };

    // Create overlay groups
    var quakes = L.layerGroup(quakeMarkers);
    var tectonic = L.layerGroup(tectonicMarkers);

    // Create a baseMaps object.
    var baseMaps = {
        "Street Map": street,
        "Topographic Map": topo
    };
    
    // Create an overlay object.
    var overlayMaps = {
        "Earthquakes": quakes,
        "Tectonic Boundaries": tectonic
    };

    // Define a map object.
    let myMap = L.map("map", {
        center: [37.09, -120],
        zoom: 6,
        layers: [street, quakes, tectonic]
    });
    
    // Pass our map layers to our layer control.
    // Add the layer control to the map.
    L.control.layers(baseMaps, overlayMaps, {
        collapsed: false
    }).addTo(myMap);

    // Add legend to map
    var legend = L.control({position: 'bottomright'});
    var colors = ['green','greenyellow','yellow','orange','orangered','red'];

    legend.onAdd = function (myMap) {
    
        var div = L.DomUtil.create('div', 'info legend'),
            grades = ['<10', '10-30', '30-50', '50-70', '70-90','>90'],
            labels = [];
        div.innerHTML += "<h4>Legend</h4>";
        div.innerHTML += "<h5>(Epicenter Depth)</h5>";
    
        for (var i = 0; i < colors.length; i++) {
            div.innerHTML +=
                    '<i style="background:' + colors[i] + '"></i><span>' + grades[i] + '</span><br>'}
        return div;
    };
    
    legend.addTo(myMap);

    });
});

*/