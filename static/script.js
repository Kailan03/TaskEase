// Get the button element
document.addEventListener('DOMContentLoaded', (event) => {
    const getstarted = document.getElementById('getstarted');
    if (getstarted) {
        // Add an event listener to the button
        getstarted.addEventListener('click', () => {
            // Redirect to Page B when the button is clicked
            window.location.href = '/register';
        });
    }

    const form = document.querySelector('form');
    if (form) {
        form.addEventListener('submit', handleFormSubmit);
    }
});

function handleFormSubmit(event) {
    event.preventDefault();  // Prevent the default form submission
    const form = event.target;
    const formData = new FormData(form);

    fetch(form.action, {
        method: 'POST',
        body: formData
    })
    .then(response => response.json())
    .then(data => {
        alert(data.message);  // Show the pop-up message
        window.location.href = '/login';  // Redirect to the login page
    })
    .catch(error => console.error('Error:', error));
}
