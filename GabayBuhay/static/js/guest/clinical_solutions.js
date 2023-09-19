document.addEventListener('DOMContentLoaded', function () {
    const log_in_nav = document.getElementById('log-in');
    const lichenCheckBtn = document.getElementById('lichenCheckBtn');
    const seeADoctorBtn = document.getElementById('seeADoctorBtn');
    const dermAwareBtn = document.getElementById('dermAwareBtn');
    const overlay = document.getElementById('overlay');
    const registrationFormPopup = document.getElementById('registrationFormPopup');
    const loginFormPopup = document.getElementById('loginFormPopup');
    const form = document.querySelector('form');
    const redirect_to_login = document.getElementById('redirect_to_login'); 
    const redirect_to_register = document.getElementById('redirect_to_register');
    const patientRadio = document.getElementById("patientRadio");
    const clinicianRadio = document.getElementById("clinicianRadio");
    const licenseDiv = document.getElementById("licenseDiv");
    const passwordField = document.querySelector('#pass');
    const confirmPasswordField = document.querySelector('[name="repeat_password"]');
    const submitButton = document.querySelector('.submit');
    const closeButton = document.querySelector(".btn-close");
    const getStartedBtn1 = document.getElementById('getStartedBtn1');
    const getStartedBtn2 = document.getElementById('getStartedBtn2');
    const getStartedBtn3 = document.getElementById('getStartedBtn3');
    const getStartedBtn4 = document.getElementById('getStartedBtn4');
    const getStartedBtn5 = document.getElementById('getStartedBtn5');
    
    if (loginFormPopup && registrationFormPopup) {

        // Even listener for "Log-in" button in the navbar in base.html
        log_in_nav.addEventListener('click', function () {
            loginFormPopup.style.display = 'block';
            overlay.style.display = 'block';
            registrationFormPopup.style.display = 'none';
        });

        // Even listener for "LichenCheck" NAV-link
        lichenCheckBtn.addEventListener('click', function () {
            overlay.style.display = 'block';   
            loginFormPopup.style.display = 'none';
            registrationFormPopup.style.display = 'block';
        });

        // Even listener for "See a Doctor" NAV-link
        seeADoctorBtn.addEventListener('click', function () {
            overlay.style.display = 'block';   
            loginFormPopup.style.display = 'none';
            registrationFormPopup.style.display = 'block';
        });

        // Even listener for "DermAware" NAV-link
        dermAwareBtn.addEventListener('click', function () {
            overlay.style.display = 'block';   
            loginFormPopup.style.display = 'none';
            registrationFormPopup.style.display = 'block';
        });

        // Event listener for "Already have an account? {Log in here} button"
        redirect_to_login.addEventListener('click', function () {
            // Hide the registration form and show the login form
            loginFormPopup.style.display = 'block';
            registrationFormPopup.style.display = 'none';
        });
    
        // Event listener for "Don't have an account? {Sign up here} button"
        redirect_to_register.addEventListener('click',function (){
            // Hide the login form and show the registration form
            loginFormPopup.style.display = 'none';
            registrationFormPopup.style.display = 'block';
        });

         // Event listeners to the radio buttons
         patientRadio.addEventListener("click", () => {
            // Hide the license div when the patient radio button is clicked
            licenseDiv.style.display = "none";
            console.log("Patient radio clicked")
        });

        // Event listeners to the radio buttons
        clinicianRadio.addEventListener("click", () => {
            // Show the license div when the clinician radio button is clicked
            licenseDiv.style.display = "block";
            licenseDiv.querySelector('input').setAttribute('required', 'required');
        });

        // Password and confirm password matching 
        confirmPasswordField.addEventListener('input', function () {
            const password = passwordField.value;
            const confirmPassword = confirmPasswordField.value;

            if (password !== confirmPassword) {
                confirmPasswordField.setCustomValidity("Passwords do not match");
            } else {
                confirmPasswordField.setCustomValidity("");
            }
        }); passwordField.addEventListener('input', function () {
            confirmPasswordField.setCustomValidity("");
        }); submitButton.addEventListener('click', function () {
            confirmPasswordField.reportValidity();
        });

        // Event listener to the close button
        closeButton.addEventListener("click", function() {
            // Close the registration form popup or perform any desired action
            registrationFormPopup.style.display = "none";
            loginFormPopup.style.display = 'none';
            overlay.style.display = 'none';
        });

        // Event listener to the submit button
        form.addEventListener('submit', function (event) {
            if (!patientRadio.checked && !clinicianRadio.checked) {
                event.preventDefault(); // Prevent form submission if neither option is selected
                alert('Please choose your account type by selecting either "Patient" or "Clinician".');
            }
        });

    } else {
        console.error('One or more elements not found.');
    }

});




