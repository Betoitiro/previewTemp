document.getElementById("cards").onmousemove = e => {
    for(const card of document.getElementsByClassName("card")) {
        const rect = card.getBoundingClientRect(),
        x = e.clientX - rect.left,
        y = e.clientY - rect.top;

        card.getElementsByClassName.setProperty("--mouse-x", `${x}px`);
        card.getElementsByClassName.setProperty("--mouse-y", `${y}px`);
    }
}