console.log(dataset);

console.log(dataset[0][0]['Number of Flights with 7700 Squawk Code'])
console.log(dataset[0][0]['Flight Manufacturer'])

// let bar_title = ""
// bar_title += "<p>Top 10 Flight Manufacturers With Aircraft Emergencies</p>";
// document.getElementById("bar_chart").innerHTML = bar_title;

var opts={0:'Flight Manufacturer',
    1:'Origin',
    2:'Destination',
    3:'Aircraft Type',
    4:'AVH Problem',
    5:'AVH Result'}

// Create Default Plot
const data = {
    labels: dataset[0][0]['Flight Manufacturer'],
    datasets: [{
        label: 'Aircraft Emergencies',
        data: dataset[0][0]['Number of Flights with 7700 Squawk Code'],
        backgroundColor: '#268BD2'
    }]
};

const config = {
    type: 'bar',
    data: data,
    options: {
        legend: {display: false},
        plugins: {
            title: {
                display: true,
                text: 'Top 10 Flight Manufacturers With Aircraft Emergencies'
            }
        }
    }
  };

let myChart = new Chart(
    document.getElementById('myChart'),
    config);


// Create Drowdown Menu Items
for (var j = 0; j < Object.keys(opts).length; j++) {
    var dropdown = document.getElementById("sel");
    var opt = document.createElement("option"); 
    opt.text = opts[j].toString();
    opt.value = j;
    dropdown.options.add(opt);
};

// Event Handling
d3.selectAll("#sel").on("change", new_chart);

// Function to Create Plot
function new_chart() {
    var dropdownMenu = d3.select("#sel");
    var choice = dropdownMenu.property("value");
    console.log(choice)

    // New Plot
    const data = {
        labels: dataset[choice][0][opts[choice]],
        datasets: [{
            label: 'Aircraft Emergencies',
            data: dataset[choice][0]['Number of Flights with 7700 Squawk Code'],
            backgroundColor: '#268BD2'
        }]
    };

    myChart.data = data
    myChart.options = {
        legend: {display: false},
        plugins: {
            title: {
                display: true,
                text: 'Top 10'+opts[choice]+'With Aircraft Emergencies'
            }
        }
    };
    myChart.update()

    // var bar_title = "<h3 style='color: black;text-align: center;font-size: 18px;'>Top 10"+String(opts[choice])+"With Aircraft Emergencies</h3>";
    // document.getElementById("bar_chart").innerHTML = bar_title
};