console.log(dataset);
// TO DO:
// - Filter Function improve/get it to work
// - Add markers to the map (airport data?? location of start and end are not always takeoff and landing)
// - Create summary statistics tables

// Flight Summary Table
let icao = dataset[0][0]['ICAO24'][0];

let flight_info = "";
for (let f=0; f<dataset[1][0]['Callsign'].length;f++) {
    if (dataset[1][0]['ICAO24'][f] == icao) {
        for (const [key, value] of Object.entries(dataset[1][0])) { 
            if (value[f] != 'NaN') {
                flight_info += "<p><span>"+key+":</span> "+value[f]+"</p>";
            }
        }
    }
};
document.getElementById("flight_info").innerHTML = flight_info


// Aircraft Info Table
let meta = dataset[2][0];
let aircraft = "";
for (const [key, value] of Object.entries(meta)) {
    if (value != 'NaN') {
        aircraft += "<p><span>"+key+":</span> "+value+"</p>";
    }
}
document.getElementById("aircraft_info").innerHTML = aircraft

// Flight Title
let flight_title = ""
flight_title += "<p>Flight "+dataset[0][0]['Callsign'][0]+"</p>";
document.getElementById("flight_title").innerHTML = flight_title

// Altitude/Speed Plot
labels = [];
for (let i = 0; i < dataset[0][0]['Squawk'].length; i++) {
    labels.push(`Squawk: ${dataset[0][0]['Squawk'][i]}`);
};

let trace1 = {
    x: dataset[0][0]['Timestamp'],
    y: dataset[0][0]['Altitude'],
    text: labels,
    type: 'line',
    name: "Altitude (ft.)"
};

let trace2 = {
    x: dataset[0][0]['Timestamp'],
    y: dataset[0][0]['Groundspeed'],
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

// Dynamically Create Options for Dropdown
var dropdown = document.getElementById("selDataset");
var opt = document.createElement("option"); 
opt.text = 'Select Flight';
opt.value = '';
dropdown.options.add(opt);
for (var j = 0; j < dataset[1][0]['Callsign'].length; j++) {
    var dropdown = document.getElementById("selDataset");
    var opt = document.createElement("option"); 
    opt.text = dataset[1][0]['Callsign'][j].toString();
    opt.value = dataset[1][0]['ICAO24'][j].toString();
    dropdown.options.add(opt);
};

var dropdown = document.getElementById("selDataset1");
var opt = document.createElement("option"); 
opt.text = 'Select Origin';
opt.value = '';
dropdown.options.add(opt);
for (var j = 0; j < dataset[1][0]['Origin'].length; j++) {
    var dropdown = document.getElementById("selDataset1");
    var opt = document.createElement("option"); 
    opt.text = dataset[1][0]['Origin'][j].toString();
    opt.value = dataset[1][0]['Origin'][j].toString();
    dropdown.options.add(opt);
};

// Function to Dynamically Populate Table
function populateTable(rows, cells, content) {
    table = document.createElement('table');
    header = document.createElement('thead');
    head = document.createElement('tr');
    head.appendChild(document.createElement('th'));
    head.cells[0].appendChild(document.createTextNode('Callsign'));
    head.appendChild(document.createElement('th'));
    head.cells[1].appendChild(document.createTextNode('Origin'));
    head.appendChild(document.createElement('th'));
    head.cells[2].appendChild(document.createTextNode('Diverted'));
    head.appendChild(document.createElement('th'));
    head.cells[3].appendChild(document.createTextNode('Landing'));
    head.appendChild(document.createElement('th'));
    head.cells[4].appendChild(document.createTextNode('Typecode'));
    head.appendChild(document.createElement('th'));
    head.cells[5].appendChild(document.createTextNode('ICAO24'));
    header.appendChild(head)
    table.appendChild(header)
    body = document.createElement('tbody');

    for (var i = 0; i < rows; ++i) {
        row = document.createElement('tr');
        for (var j = 0; j < cells; ++j) {
            row.appendChild(document.createElement('td'));
            row.cells[j].appendChild(document.createTextNode(content[j][i]));
        }
        table.appendChild(row);
    }
    table.appendChild(body)
    return table
}
filter_data = dataset[1][0]

// Event Handling to Filter Data
d3.selectAll("#selDataset1").on("change", create_table);

filter_data = dataset[1][0]
cols = ['Callsign','Origin','Diverted','Landing','Typecode','ICAO24'];


function filter_func() {
    for (let x=0; x<filter_data;x++) {
        if (filter_data['Origin'][x] != d3.select("#selDataset").property("value")) {
            for (var y in cols) {
                filter_data[y].splice(x,1)
            }
        }
    };
    row_count = filter_data['Callsign'].length;
    let filter_content = {};

    for (var i=0; i<cols.length;i++) {
        filter_content[i] = filter_data[cols[i]]
    }
    return filter_content
};

// Create the Table
function create_table() {
    tab = document.getElementById('flight_table');
    tab.innerHTML='';
    tab.appendChild(populateTable(filter_data['Callsign'].length, cols.length, filter_func()));
};
create_table()

// Event Handling to highlight table rows and change flights on click
d3.selectAll("tr")
.on("mouseover", function(){
    d3.select(this)
        .style("background-color", "orange");
})
.on("mouseout", function(){
    d3.select(this)
        .style("background-color", "white")
})
.on("click", change_flight);


// Function to change Displayed Data with User Click
function change_flight() {
    var dropdownMenu = d3.selectAll('td')
    output = d3.select(this).text()
    new_flight = output.substring(output.length - 6)
    window.location.href = ('http://127.0.0.1:5000/flight_dashboard_'+new_flight);
}

// Flight Trajectory Map
var lats = dataset[0][0]['Latitude'];
var lons = dataset[0][0]['Longitude'];
let coords = [];
for (let x=0;x<lats.length;x++) {
    coords.push([lats[x],lons[x]])
};
middle_coords = coords[Math.round(lats.length / 2)];

let myMap = L.map("map").setView(middle_coords, 5);

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(myMap);

L.polyline(coords,
    {color: 'black',weight: 3})
    .bindPopup("<h3>Flight Path: "+dataset[0][0]['Callsign'][0]+"</h3><hr>")
    .addTo(myMap)
