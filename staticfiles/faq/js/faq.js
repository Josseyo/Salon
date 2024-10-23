// faq.js
document.addEventListener('DOMContentLoaded', function() {
    const questions = document.querySelectorAll('.question-container');
    questions.forEach(container => {
        const questionHeader = container.querySelector('.question');
        const answerDiv = container.querySelector('.answer');
        questionHeader.addEventListener('click', function() {
            answerDiv.style.display = answerDiv.style.display === 'none' ? 'block' : 'none';
            const caret = questionHeader.querySelector('.caret');
            caret.textContent = answerDiv.style.display === 'block' ? '▼' : '▶';
        });
    });
});
