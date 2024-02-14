function myFunction() {
  var selectedOption = document.getElementById("river").options[document.getElementById("river").selectedIndex];
  
  // Get the ID attribute of the selected option
  var selectedOptionId = selectedOption.getAttribute("id");
  
  // Store the ID value in a hidden input field to submit to the server
  document.getElementById("selectedRiverId").value = selectedOptionId;
  
  }