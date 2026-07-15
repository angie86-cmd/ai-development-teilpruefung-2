document.addEventListener("DOMContentLoaded", () => {
    const weatherForm = document.querySelector("#weather-form");
    const appointmentForm = document.querySelector("#appointment-form");
    const weatherResult = document.querySelector("#weather-result");
    const appointmentResult = document.querySelector("#appointment-result");

    async function postJson(url, payload) {
        const response = await fetch(url, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify(payload),
        });
        if (!response.ok) {
            throw new Error(`HTTP-Fehler ${response.status}`);
        }
        return response.json();
    }

    weatherForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        weatherResult.textContent = "Wetterdaten werden geladen …";
        try {
            const data = await postJson("/api/weather", {
                city: document.querySelector("#city").value,
            });
            weatherResult.textContent = data.message;
        } catch (error) {
            console.error(error);
            weatherResult.textContent =
                "Die Wetteranfrage konnte nicht verarbeitet werden. Bitte versuchen Sie es erneut.";
        }
    });

    appointmentForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        appointmentResult.textContent = "Termin wird geprüft …";
        try {
            const data = await postJson("/api/appointment", {
                date: document.querySelector("#date").value,
                time: document.querySelector("#time").value,
            });
            appointmentResult.textContent = data.message;
        } catch (error) {
            console.error(error);
            appointmentResult.textContent =
                "Die Terminbuchung konnte nicht verarbeitet werden. Bitte versuchen Sie es erneut.";
        }
    });
});
