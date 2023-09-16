document.addEventListener("DOMContentLoaded", function () {
    const loginForm = document.getElementById("loginForm");
    const errorMessage = document.getElementById("error-message");

    loginForm.addEventListener("submit", function (event) {
        event.preventDefault(); // Prevent the default form submission behavior

        const formData = new FormData(loginForm);

        fetch("{{ url_for('home_bp.log_in') }}", {
            method: "POST",
            body: formData,
        })
            .then(response => response.json())
            .then(data => {
                if (data.error) {
                    errorMessage.textContent = data.error;
                    errorMessage.style.display = 'block'; // Show the error message
                } else if (data.success) {
                    errorMessage.textContent = ""; // Clear any previous error messages
                    window.location.href = data.redirect_url;
                }
            })
            .catch(error => {
                console.error("Error:", error);
            });
    });
});