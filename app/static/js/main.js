document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('.survey-form');
    
    // Form validation messages in multiple languages
    const validationMessages = {
        ja: {
            required: '必須項目です',
            email: '有効なメールアドレスを入力してください',
            date: '有効な日付を入力してください',
            number: '数値を入力してください',
            fileSize: 'ファイルサイズは5MB以下にしてください',
            fileType: '許可されていないファイル形式です'
        },
        en: {
            required: 'This field is required',
            email: 'Please enter a valid email address',
            date: 'Please enter a valid date',
            number: 'Please enter a number',
            fileSize: 'File size must be less than 5MB',
            fileType: 'Invalid file type'
        },
        mn: {
            required: 'Заавал бөглөх',
            email: 'Зөв имэйл хаяг оруулна уу',
            date: 'Зөв огноо оруулна уу',
            number: 'Тоо оруулна уу',
            fileSize: 'Файлын хэмжээ 5MB-аас бага байх ёстой',
            fileType: 'Файлын төрөл буруу байна'
        },
        vi: {
            required: 'Trường này là bắt buộc',
            email: 'Vui lòng nhập địa chỉ email hợp lệ',
            date: 'Vui lòng nhập ngày hợp lệ',
            number: 'Vui lòng nhập số',
            fileSize: 'Kích thước tệp phải nhỏ hơn 5MB',
            fileType: 'Loại tệp không hợp lệ'
        }
    };

    // Get current language
    const getCurrentLanguage = () => {
        return document.querySelector('.survey-form').dataset.language || 'ja';
    };

    // Validate email
    const validateEmail = (email) => {
        return /^[^\s@]+@[^\s@]+\.[^\s@]+$/.test(email);
    };

    // Validate date
    const validateDate = (date) => {
        return !isNaN(new Date(date).getTime());
    };

    // File validation
    const validateFile = (file, allowedTypes) => {
        if (file.size > 5 * 1024 * 1024) {
            return 'fileSize';
        }
        if (!allowedTypes.includes(file.type)) {
            return 'fileType';
        }
        return '';
    };

    // Add validation to required fields
    const addFieldValidation = (field) => {
        field.addEventListener('blur', function() {
            const lang = getCurrentLanguage();
            let error = '';

            if (field.required && !field.value) {
                error = validationMessages[lang].required;
            } else if (field.type === 'email' && field.value && !validateEmail(field.value)) {
                error = validationMessages[lang].email;
            } else if (field.type === 'date' && field.value && !validateDate(field.value)) {
                error = validationMessages[lang].date;
            }

            // Show/hide error message
            let errorDiv = field.nextElementSibling;
            if (!errorDiv || !errorDiv.classList.contains('error-message')) {
                errorDiv = document.createElement('div');
                errorDiv.classList.add('error-message');
                field.parentNode.insertBefore(errorDiv, field.nextSibling);
            }
            errorDiv.textContent = error;
            field.classList.toggle('error', !!error);
        });
    };

    // Add validation to all form fields
    document.querySelectorAll('input, select, textarea').forEach(addFieldValidation);

    // Form submission handling
    form.addEventListener('submit', function(e) {
        let hasErrors = false;
        const lang = getCurrentLanguage();

        // Validate all required fields
        form.querySelectorAll('[required]').forEach(field => {
            if (!field.value) {
                hasErrors = true;
                field.classList.add('error');
                let errorDiv = field.nextElementSibling;
                if (!errorDiv || !errorDiv.classList.contains('error-message')) {
                    errorDiv = document.createElement('div');
                    errorDiv.classList.add('error-message');
                    field.parentNode.insertBefore(errorDiv, field.nextSibling);
                }
                errorDiv.textContent = validationMessages[lang].required;
            }
        });

        if (hasErrors) {
            e.preventDefault();
            // Scroll to first error
            const firstError = form.querySelector('.error');
            if (firstError) {
                firstError.scrollIntoView({ behavior: 'smooth', block: 'center' });
            }
        }
    });

    // Dynamic form sections (Education and Work Experience)
    const addRowButtons = document.querySelectorAll('.add-row-button');
    addRowButtons.forEach(button => {
        button.addEventListener('click', function() {
            const table = this.previousElementSibling;
            const newRow = table.querySelector('tr:last-child').cloneNode(true);
            newRow.querySelectorAll('input').forEach(input => input.value = '');
            table.querySelector('tbody').appendChild(newRow);
        });
    });
});
