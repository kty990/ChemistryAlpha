// Terminal > output
// Terminal Cline

const terminal = document.getElementById("terminal");
const output = terminal.querySelector("#output");
const cline = terminal.querySelector("#cline");

function runCommand() {
    let cmd = cline.value;
    if (cmd.length > 0) {
        // Attempt to run command
    } else {
        // Invalid attempt
    }
}