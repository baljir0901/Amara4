document.addEventListener("DOMContentLoaded", function() {
    // Language selection
    const languageSelect = document.getElementById("language");
    if (languageSelect) {
        languageSelect.addEventListener("change", function() {
            window.location.href = `/change_language/${this.value}`;
        });
    }

    // Form validation
    const form = document.querySelector(".survey-form");
    if (form) {
        form.addEventListener("submit", function(event) {
            if (!validateForm()) {
                event.preventDefault();
            }
        });
    }

    // File upload preview
    const fileInputs = document.querySelectorAll("input[type=file]");
    fileInputs.forEach(input => {
        input.addEventListener("change", function() {
            previewFile(this);
        });
    });
});

function validateForm() {
    // Add your validation logic here
    return true;
}

function previewFile(input) {
    if (input.files && input.files[0]) {
        const reader = new FileReader();
        reader.onload = function(e) {
            const preview = document.getElementById(`${input.id}-preview`);
            if (preview) {
                preview.src = e.target.result;
            }
        };
        reader.readAsDataURL(input.files[0]);
    }
}
