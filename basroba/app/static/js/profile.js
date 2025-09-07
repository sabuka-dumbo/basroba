const main_part1 = document.getElementById("main-part1");
const main_part2 = document.getElementById("main-part2");
const main_part3 = document.getElementById("main-part3");

function open_part1() {
    main_part1.style.display = "block";
    main_part2.style.display = "none";
    main_part3.style.display = "none";
}

function open_part2() {
    main_part1.style.display = "none";
    main_part2.style.display = "block";
    main_part3.style.display = "none";
}

function open_part3() {
    main_part1.style.display = "none";
    main_part2.style.display = "none";
    main_part3.style.display = "block";
}

addEventListener("DOMContentLoaded", function() {
    open_part1()
})

function save_user_info() {
    const first_name = document.getElementById("first_name").value;
    const middle_name = document.getElementById("middle_name").value;
    const last_name = document.getElementById("last_name").value;
    const id_number = document.getElementById("id_number").value;
    const email_address = document.getElementById("email_address").value;
    const phone_number = document.getElementById("phone_number").value;

    fetch("/api/save_user/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            first_name: first_name,
            middle_name: middle_name,
            last_name: last_name,
            id_number: id_number,
            email_address: email_address,
            phone_number: phone_number
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
        } else if (data.error) {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}