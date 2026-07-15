// Wartet, bis die HTML-Struktur verfügbar ist, bevor Formulare verknüpft werden.
document.addEventListener("DOMContentLoaded", () => {
    const weatherForm = document.querySelector("#weather-form");
    const appointmentForm = document.querySelector("#appointment-form");
    const weatherResult = document.querySelector("#weather-result");
    const appointmentResult = document.querySelector("#appointment-result");

    // Sendet JSON-Nutzdaten asynchron an Flask und liest die JSON-Antwort.
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

    // Sendet z. B. { "city": "Berlin" } ohne Seitenreload an /api/weather.
    weatherForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        weatherResult.textContent = "Wetterdaten werden geladen …";
        try {
            const data = await postJson("/api/weather", {
                city: document.querySelector("#city").value,
            });
            // Zeigt die vom Flask-Endpunkt gelieferte JSON-Nachricht direkt an.
            weatherResult.textContent = data.message;
        } catch (error) {
            console.error(error);
            // Eine verständliche Meldung ersetzt technische Fehlerdetails für Nutzende.
            weatherResult.textContent =
                "Die Wetteranfrage konnte nicht verarbeitet werden. Bitte versuchen Sie es erneut.";
        }
    });

    // Sendet z. B. { "date": "20.07.2026", "time": "14:00" } an /api/appointment.
    appointmentForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        appointmentResult.textContent = "Termin wird geprüft …";
        try {
            const data = await postJson("/api/appointment", {
                date: document.querySelector("#date").value,
                time: document.querySelector("#time").value,
            });
            // Aktualisiert den Termin-Ergebnisbereich mit der JSON-Antwort.
            appointmentResult.textContent = data.message;
        } catch (error) {
            console.error(error);
            // Auch Netzwerk- oder Serverfehler werden nutzerfreundlich dargestellt.
            appointmentResult.textContent =
                "Die Terminbuchung konnte nicht verarbeitet werden. Bitte versuchen Sie es erneut.";
        }
    });
});
