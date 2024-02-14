        
function autoFillDates() {
  var startDate = new Date(document.getElementById("date1").value); // Get the value of the start date input field
  for (var i = 2; i <= 14; i++) {
    var currentDate = new Date(startDate.getTime() + (i - 1) * 24 * 60 * 60 * 1000); // Calculate the current date based on the start date
    var currentDateString = currentDate.toISOString().split("T")[0]; // Format the current date as a string in the format YYYY-MM-DD
    document.getElementById("date" + i).value = currentDateString; // Set the value of the current date input field to the formatted date string
  }
}

function loadCSV() {
   // Read the CSV file
   const fileInput = document.createElement('input');
   fileInput.type = 'file';
   fileInput.accept = '.csv';
   fileInput.addEventListener('change', (event) => {
     const file = event.target.files[0];
     const reader = new FileReader();
     reader.onload = (event) => {
       const csvData = event.target.result;
 
       // Parse the CSV data
       const rows = csvData.split('\n');
       //const headers = rows[0].split(',');
       const data = rows.slice(1).map((row) => row.split(','));
       console.log(data[0][3]);
       // Find the specific values
       const text_area_1 = data[0][0];
       const text_area_2 = data[0][1];
       const text_area_3 = data[0][2];
       const text_area_4 = data[0][3];
       const text_area_5 = data[0][4];
       const text_area_6 = data[0][5];
       const text_area_7 = data[0][6];
       const text_area_8 = data[0][7];
       const text_area_9 = data[1][0];
       const text_area_10 = data[1][1];
       const text_area_11 = data[1][2];
       const text_area_12 = data[1][3];
       const text_area_13 = data[1][4];
       const text_area_14 = data[1][5];
       const text_area_15 = data[1][6];
       const text_area_16 = data[1][7];
       const text_area_17 = data[2][0];
       const text_area_18 = data[2][1];
       const text_area_19 = data[2][2];
       const text_area_20 = data[2][3];
       const text_area_21 = data[2][4];
       const text_area_22 = data[2][5];
       const text_area_23 = data[2][6];
       const text_area_24 = data[2][7];
       const text_area_25 = data[3][0];
       const text_area_26 = data[3][1];
       const text_area_27 = data[3][2];
       const text_area_28 = data[3][3];
       const text_area_29 = data[3][4];
       const text_area_30 = data[3][5];
       const text_area_31 = data[3][6];
       const text_area_32 = data[3][7];
       const text_area_33 = data[4][0];
       const text_area_34 = data[4][1];
       const text_area_35 = data[4][2];
       const text_area_36 = data[4][3];
       const text_area_37 = data[4][4];
       const text_area_38 = data[4][5];
       const text_area_39 = data[4][6];
       const text_area_40 = data[4][7];
       const text_area_41 = data[5][0];
       const text_area_42 = data[5][1];
       const text_area_43 = data[5][2];
       const text_area_44 = data[5][3];
       const text_area_45 = data[5][4];
       const text_area_46 = data[5][5];
       const text_area_47 = data[5][6];
       const text_area_48 = data[5][7];
       const text_area_49 = data[6][0];
       const text_area_50 = data[6][1];
       const text_area_51 = data[6][2];
       const text_area_52 = data[6][3];
       const text_area_53 = data[6][4];
       const text_area_54 = data[6][5];
       const text_area_55 = data[6][6];
       const text_area_56 = data[6][7];
       const text_area_57 = data[7][0];
       const text_area_58 = data[7][1];
       const text_area_59 = data[7][2];
       const text_area_60 = data[7][3];
       const text_area_61 = data[7][4];
       const text_area_62 = data[7][5];
       const text_area_63 = data[7][6];
       const text_area_64 = data[7][7];
       const text_area_65 = data[8][0];
       const text_area_66 = data[8][1];
       const text_area_67 = data[8][2];
       const text_area_68 = data[8][3];
       const text_area_69 = data[8][4];
       const text_area_70 = data[8][5];
       const text_area_71 = data[8][6];
       const text_area_72 = data[8][7];
       const text_area_73 = data[9][0];
       const text_area_74 = data[9][1];
       const text_area_75 = data[9][2];
       const text_area_76 = data[9][3];
       const text_area_77 = data[9][4];
       const text_area_78 = data[9][5];
       const text_area_79 = data[9][6];
       const text_area_80 = data[9][7];
       const text_area_81 = data[10][0];
       const text_area_82 = data[10][1];
       const text_area_83 = data[10][2];
       const text_area_84 = data[10][3];
       const text_area_85 = data[10][4];
       const text_area_86 = data[10][5];
       const text_area_87 = data[10][6];
       const text_area_88 = data[10][7];
       const text_area_89 = data[11][0];
       const text_area_90 = data[11][1];
       const text_area_91 = data[11][2];
       const text_area_92 = data[11][3];
       const text_area_93 = data[11][4];
       const text_area_94 = data[11][5];
       const text_area_95 = data[11][6];
       const text_area_96 = data[11][7];
       const text_area_97 = data[12][0];
       const text_area_98 = data[12][1];
       const text_area_99 = data[12][2];
       const text_area_100 = data[12][3];
       const text_area_101 = data[12][4];
       const text_area_102 = data[12][5];
       const text_area_103 = data[12][6];
       const text_area_104 = data[12][7];
       const text_area_105 = data[13][0];
       const text_area_106 = data[13][1];
       const text_area_107 = data[13][2];
       const text_area_108 = data[13][3];
       const text_area_109 = data[13][4];
       const text_area_110 = data[13][5];
       const text_area_111 = data[13][6];
       const text_area_112 = data[13][7];

      for (let i = 0; i < data.length; i++) {       //inputting data from each excel sheet cell to  text area input
        for (let j = 0; j < data[i].length; j++) {
          const index = i * 8 + j + 1;
          const value = data[i][j];
          document.getElementById(`text_area_${index}`).value = value;
        }
      }
      

    //   // Fill out specific cells in the table
    // document.getElementById("r1c1").innerHTML = values[0][0];
    // document.getElementById("r1c2").innerHTML = values[0][1];
    // document.getElementById("r1c3").innerHTML = values[0][2];
    // document.getElementById("r1c4").innerHTML = values[0][3];
    // document.getElementById("r1c5").innerHTML = values[0][4];
    // document.getElementById("r1c6").innerHTML = values[0][5];
    // document.getElementById("r1c7").innerHTML = values[0][6];
    // document.getElementById("r1c8").innerHTML = values[0][7];
    // document.getElementById("r2c1").innerHTML = values[1][0];
    // document.getElementById("r2c2").innerHTML = values[1][1];
    // document.getElementById("r2c3").innerHTML = values[1][2];
    // document.getElementById("r2c4").innerHTML = values[1][3];
    // document.getElementById("r2c5").innerHTML = values[1][4];
      
     };
     reader.readAsText(file);
   });
   fileInput.click();
 }







