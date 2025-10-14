

function load_send_matrix_table_button_event() {
    send_matrix_table_button = document.querySelector(".generate-the-matrix-block-button-generate");
    send_matrix_table_button.addEventListener("click", sendMatrixTable);
};


async function sendMatrixTable() {
    const row1 = document.getElementById("generate-the-matrix-block-table-section-button-1").textContent;
    const column1 = document.getElementById("generate-the-matrix-block-table-section-button-2").textContent;
    const row2 = document.getElementById("generate-the-matrix-block-table-section-button-3").textContent;
    const column2 = document.getElementById("generate-the-matrix-block-table-section-button-4").textContent;
    const url = "/generate_table/";
    try {
        const response = await fetch(url, {
            method: "POST",
            body: JSON.stringify({
                'row1': row1,
                'column1': column1,
                'row2': row2,
                'column2': column2,
            })
        });
        if (!response.ok) {
            throw new Error("Response status: ${response.status}");
        }
        const html = await response.text();
        const parser = new DOMParser();
        const doc = parser.parseFromString(html, 'text/html');
        const newBlock = doc.querySelector('.matrix-table-block');
        document.querySelector('.matrix-table-block').innerHTML = newBlock.innerHTML;
        document.getElementById("generate-the-matrix-block-button-generate-anchor").click();
        load_js_handlers();
    } catch (error) {
        console.error(error.message);

    }
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



function choose_another_option_button(button_obj_id, list_elem_obj_ids) {
    list_elem_obj_ids.forEach(id => {
        const elem_obj = document.getElementById(id);
        elem_obj.addEventListener("click", () => {
            const button_obj = document.getElementById(button_obj_id);
            list_elem_obj_ids.forEach(otherId => {
                document.getElementById(otherId).classList.remove('active');
            });
            elem_obj.classList.add('active');
            if (button_obj_id != "generate-the-matrix-block-table-section-button-2") {
                if (button_obj_id == "generate-the-matrix-block-table-section-button-1") {
                    const button_obj2 = document.getElementById("generate-the-matrix-block-table-section-button-3")
                    button_obj.textContent = elem_obj.textContent
                    button_obj2.textContent = elem_obj.textContent
                } else {
                    console.log(elem_obj)
                    const button_obj2 = document.getElementById("generate-the-matrix-block-table-section-button-1")
                    button_obj.textContent = elem_obj.textContent
                    button_obj2.textContent = elem_obj.textContent
                }

            } else {
                console.log(elem_obj)
                button_obj.textContent = elem_obj.textContent
            }

        });
    });
}


load_send_matrix_table_button_event();
choose_another_option_button("generate-the-matrix-block-table-section-button-1", ["generate-the-matrix-block-table-section-button-1-option-1", "generate-the-matrix-block-table-section-button-1-option-2", "generate-the-matrix-block-table-section-button-1-option-3", "generate-the-matrix-block-table-section-button-1-option-4"])
choose_another_option_button("generate-the-matrix-block-table-section-button-2", ["generate-the-matrix-block-table-section-button-2-option-1", "generate-the-matrix-block-table-section-button-2-option-2", "generate-the-matrix-block-table-section-button-2-option-3", "generate-the-matrix-block-table-section-button-2-option-4"])


