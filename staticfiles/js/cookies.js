/**
 * Initializes the cookie consent functionality once the DOM is fully loaded.
 * This script sets up the appearance and content of the cookie consent popup.
 */
document.addEventListener("DOMContentLoaded", function() {
    window.cookieconsent.initialise({
        palette: {
            popup: { background: "#AFDBF6" },  // Background color of the popup
            button: { background: "#F4F4F4" }  // Background color of the button
        },
        theme: "edgeless",  // Specifies the theme of the popup
        content: {
            header: "We use cookies",  // Header text for the popup
            message: "This website uses cookies to ensure you get the best experience.",  // Message text
            dismiss: "I agree",  // Text for the dismiss button
        }
    });
});