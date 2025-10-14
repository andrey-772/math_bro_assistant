async function solve_by_simple_iteration_method() {
    url = "/solve_by_simple_iteration_method/"
    try {
        const response = await fetch(url, {
            method: 'GET'
        });
        if (!response.ok) {
            throw new Error("Response status: ${response.status}");
        }
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, "text/html");
        const newBlock = doc.querySelector(".matrix-calculation-simple-iteration-method-block");
        document.querySelector(".matrix-calculation-simple-iteration-method-block").innerHTML = newBlock.innerHTML;
        document.getElementById("matrix-calculation-simple-iteration-method-anchor").click();
        animate_solution();
        if (document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-4").textContent == "System is convergent")
        {
            if (
                document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-3").textContent.includes("0.0") ||
                document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-2").textContent.includes("0.0")
            ) {
                document.getElementById("matrix-calculation-simple-iteration-method-block-block-step2-1").style.display = "block"
                document.getElementById("matrix-calculation-simple-iteration-method-block-block-step2-1-error").style.display = "block"
            } else {
                document.getElementById("matrix-calculation-simple-iteration-method-block-block-step2-1").style.display = "block"
                document.getElementById("matrix-calculation-simple-iteration-method-block-block-step2-2").style.display = "block"
                document.getElementById("matrix-calculation-simple-iteration-method-block-block-step2-3").style.display = "block"
            }
        };
     
    } catch {
        console.error(error.message)
    }
}


function sleep(ms) {
    return new Promise(resolve => setTimeout(resolve, ms));
}
async function animate_solution() {
    document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-1").style.display = "block"
    //await sleep(1000)
    document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-2").style.display = "block"
    //document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-2-anchor").click()
    //await sleep(1000)
    document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-3").style.display = "block"
    //document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-3-anchor").click()
    //await sleep(1000)
    document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-4").style.display = "block"
    //document.getElementById("matrix-calculation-simple-iteration-method-block-block-step1-4-anchor").click()
    //await sleep(1000)
    console.log(12)
}


function load_js_handlers() {

    const cells = document.querySelectorAll('.matrix-table-block-column-cell');

    cells.forEach(cell => {
        cell.addEventListener("input", function () {
            this.value = this.value
                // 1. allow only digits, comma, minus
                .replace(/[^0-9,-]/g, '')
                // 2. allow only one comma
                .replace(/(,)(?=.*\1)/g, '')
                // 3. minus only at the beginning
                .replace(/(?!^)-/g, '');

        });
    });
}

load_js_handlers()
solve_by_simple_iteration_method();