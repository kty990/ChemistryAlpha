const closeBtn = document.getElementById("close");
const minBtn = document.getElementById("minimize");

closeBtn.addEventListener("click", () => {
    window.api.send("close");
})

minBtn.addEventListener("click", () => {
    window.api.send("minimize");
})

window.addEventListener("keydown", (e) => {
    if (e.key == "t" && e.ctrlKey) {
        window.api.send("toggle-dev-tools")
    } else if (e.key == "r" && e.ctrlKey) {
        window.api.send("dev-refresh");
    }
})

// --------------------------------------------------------------------------------------------------
// ==================================================================================================
// --------------------------------------------------------------------------------------------------
