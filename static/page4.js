const ctx = document.getElementById('myChart').getContext('2d');

const chartData = {
  labels: ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday'],
  datasets: [{
    label: 'Temperature',
    data: [20, 22, 23, 21, 18, 17, 19],
    borderColor: 'blue',
    fill: false
  }]
};

const chartOptions = {
  scales: {
    yAxes: [{
      ticks: {
        beginAtZero: true
      }
    }]
  }
};

const myChart = new Chart(ctx, {
  type: 'line',
  data: chartData,
  options: chartOptions
});

function models() {
  // code to be executed when the button is clicked
  window.location.href = "page5.html";
}
