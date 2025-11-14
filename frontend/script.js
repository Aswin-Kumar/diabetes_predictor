document.getElementById("predictForm")?.addEventListener("submit", async (e) => {
  e.preventDefault();

  const inputs = Array.from(e.target.querySelectorAll("input")).map(i => i.value);
  const resultElement = document.getElementById("result");
  const recElement = document.getElementById("recommendation");

  resultElement.textContent = "⏳ Predicting...";
  recElement.textContent = "";
  resultElement.style.color = "#fff";

  try {
    const res = await fetch("/api/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ inputs }),
    });
    const data = await res.json();

    if (data.prediction) {
      let rec = "";
      if (data.prediction === "Diabetic" || data.prediction === 1) {
        resultElement.textContent = "⚠️ The person is Diabetic";
        resultElement.style.color = "#ff3b3b";
        rec = "💊 Maintain a balanced diet, regular exercise, and regular glucose monitoring.";
      } else {
        resultElement.textContent = "✅ The person is Not Diabetic";
        resultElement.style.color = "#32cd32";
        rec = "🥦 Keep up your healthy habits! Stay active and eat balanced meals.";
      }
      recElement.textContent = rec;
    } else {
      resultElement.textContent = `Error: ${data.error}`;
      resultElement.style.color = "#ffcc00";
    }
  } catch (err) {
    resultElement.textContent = "🚫 Server Error!";
    resultElement.style.color = "#ffcc00";
  }
});

/* 🌙 Dark / Light Mode */
const toggle = document.getElementById("modeToggle");
let darkMode = true;
toggle?.addEventListener("click", () => {
  darkMode = !darkMode;
  document.body.classList.toggle("light-mode", !darkMode);
  toggle.textContent = darkMode ? "🌙" : "☀️";
});
