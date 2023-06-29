// Function to check if any duplicate values exist in an array
function hasDuplicates(array) {
return (new Set(array)).size !== array.length;
}

// Function to validate the form before submission
function validateForm(event) {
event.preventDefault(); // Prevent form submission

var selectedPlayers = [];

// Get all the selected players from the input fields
var playerInputs = document.getElementsByTagName('input');
for (var i = 0; i < playerInputs.length; i++) {
    var playerInput = playerInputs[i];
    if (playerInput.value.trim() !== '') {
    selectedPlayers.push(playerInput.value.trim());
    }
}

// Check if there are any duplicate players
if (hasDuplicates(selectedPlayers)) {
    alert('Please select different players for each field.');
    return false; // Stop further execution
}

// If no duplicates found, submit the form
event.target.submit();
}

// Attach event listener to the form's submit event
document.getElementById('test').addEventListener('submit', validateForm);