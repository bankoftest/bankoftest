// Automatically detect language based on the URL
const language = window.location.pathname.includes("/zh/") ? "zh" : "en";

// Messages for both languages
const messages = {
    en: {
        correct: "Correct!",
        incorrect: "Incorrect."
    },
    zh: {
        correct: "回答正确！",
        incorrect: "回答错误！"
    }
};


function selectOption(questionId, selectedLetter, isCorrect) {
    // Clear previous styles
    const options = document.querySelectorAll(`#${questionId} .option`);
    options.forEach(option => {
        option.style.backgroundColor = ""; // Reset background color
        option.innerHTML = option.innerHTML.replace("👍", "").replace("👎", ""); // Remove emojis
    });

    // Highlight the selected option
    const selectedOption = document.querySelector(`#${questionId}-${selectedLetter}`);
    if (isCorrect) {
        selectedOption.style.backgroundColor = "green";
        selectedOption.innerHTML += " 👍";
    } else {
        selectedOption.style.backgroundColor = "red";
        selectedOption.innerHTML += " 👎";
    }

    // Display a result message
    const resultElement = document.getElementById(`${questionId}-result`);
    resultElement.innerText = isCorrect
        ? messages[language].correct
        : messages[language].incorrect;

    // Add a class for centered styling
    resultElement.classList.add("result-message");
    resultElement.style.color = "blue";

}
