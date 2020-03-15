
let accordion = document.getElementsByClassName("accordion");

for (let i = 0; i < accordion.length; i++) {
    acccordion[i].addEventListener("click", () => {
        this.classList.toggle("active");
        let panel = this.nextElementSibling;
        if (panel.style.maxHeight) {
            panel.style.maxHeight = null;
        } else {
            panel.style.maxHeight = panel.scrollHeight + "px";
        }
    });
}
