document.addEventListener("DOMContentLoaded", function() {
    const term = document.getElementById("terminal");
    if (!term) return;

    const messages = [
        "Parsing CSV headers...",
        "Normalizing timestamps...",
        "Detecting gaps in host: server1...",
        "Scoring silence windows...",
        "Generating report..."
    ];

    let i = 0;
    function scrollMessages() {
        if (i < messages.length) {
            term.innerHTML += messages[i] + "<br>";
            term.scrollTop = term.scrollHeight;
            i++;
            setTimeout(scrollMessages, 500);
        }
    }
    scrollMessages();
});
