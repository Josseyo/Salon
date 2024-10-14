document.addEventListener('DOMContentLoaded', () => {
    // Toggle answer visibility
    document.querySelectorAll('.question').forEach(question => {
        question.addEventListener('click', () => {
            const answer = question.nextElementSibling;
            const caret = question.querySelector('.caret');
            const isExpanded = question.getAttribute('aria-expanded') === 'true';

            answer.style.display = isExpanded ? 'none' : 'block';
            caret.textContent = isExpanded ? '▶' : '▼';
            question.setAttribute('aria-expanded', !isExpanded);
        });
    });

    // Handle vote form submissions
    document.querySelectorAll('.vote-form').forEach(form => {
        form.addEventListener('submit', function(event) {
            event.preventDefault();

            const formData = new FormData(this);

            fetch(this.action, {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': formData.get('csrfmiddlewaretoken')
                }
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    const yesButton = this.querySelector('input[value="True"]');
                    const noButton = this.querySelector('input[value="False"]');
                    const yesCountSpan = yesButton.parentNode.querySelector('button');
                    const noCountSpan = noButton.parentNode.querySelector('button');
                    yesCountSpan.textContent = `Yes (${data.new_helpful_count})`;
                    noCountSpan.textContent = `No (${data.new_not_helpful_count})`;
                } else {
                    console.error('Vote unsuccessful:', data.message);
                }
            })
            .catch(error => console.error('Error:', error));
        });
    });
});
