function checkAnswer(questionId, selectedOption) {
    const questionDiv = document.getElementById(questionId);
    const correctAnswer = questionDiv.getAttribute("data-correct-answer");

    const resultElement = document.getElementById(`${questionId}-result`);

    if (correctAnswer === selectedOption) {
        resultElement.textContent = "Correct!";
        resultElement.style.color = "green";
    } else {
        resultElement.textContent = "Wrong! Try again.";
        resultElement.style.color = "red";
    }
}
