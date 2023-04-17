document.querySelector('form').addEventListener('submit', async function(event) {
    event.preventDefault();

    // Get the input value
    var url = document.getElementById('urlInput').value;

    // Call the Flask server to generate QR code
    var response = await fetch('/', {
        method: 'POST',
        body: new FormData(event.target)
    });

    // Refresh the page to display the generated QR code
    location.reload();
});
