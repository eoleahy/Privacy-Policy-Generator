
function openPage(pageName) {
    let i, tablinks;
    let subjectTab = document.getElementsByClassName("subject-section");
    let dpvTab = document.getElementsByClassName("dpv-section")
    let controllerTab = document.getElementsByClassName("controller-section");

    let len = subjectTab.length;

    if (pageName === "DPV") {
        for (i = 0; i < len; i++) {
            subjectTab[i].style.display = "none";
            controllerTab[i].style.display = "none";

            dpvTab[i].style.display = "block";
        }
    }
    else if (pageName === "Subject") {
        for (i = 0; i < len; i++) {
            dpvTab[i].style.display = "none";
            controllerTab[i].style.display = "none";
            subjectTab[i].style.display = "block";
        }
    }
    else if (pageName === "DataController") {
        for (i = 0; i < len; i++) {
            subjectTab[i].style.display = "none";
            dpvTab[i].style.display = "none";
            controllerTab[i].style.display = "block";
        }
    }
}
