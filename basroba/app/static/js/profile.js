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
    const first_name = document.getElementById("first_name1").value;
    const middle_name = document.getElementById("middle_name1").value;
    const last_name = document.getElementById("last_name1").value;
    const id_number = document.getElementById("id_number1").value;
    const email_address = document.getElementById("email_address1").value;
    const phone_number = document.getElementById("phone_number1").value;

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

function delete_address(address_id) {
    fetch("/api/delete_address/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            address_id: address_id
        })
    })
    .then(response => response.json())
    .then(data => {
        if (data.message) {
            alert(data.message);
            document.getElementById(`address-${address_id}`).remove();
        } else if (data.error) {
            alert(data.error);
        }
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

function add_address() {
    fetch("/api/add_address/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            first_name: document.getElementById("first_name22").value,
            last_name: document.getElementById("last_name22").value,
            phone_number: document.getElementById("phone_number22").value,
            street_address1: document.getElementById("street_address122").value,
            street_address2: document.getElementById("street_address222").value,
            city: document.getElementById("city22").value,
            state_region: document.getElementById("state_region22").value,
            zip_code: document.getElementById("zip_code22").value,
            country: document.getElementById("country22").value,
            phone_code: document.getElementById("phone_code22").value
        })
    })
    .then(response => response.json())
    .then(data => {
    })
    .catch(error => {
        console.error("Error:", error);
    });
}

document.getElementById("address-form-back").addEventListener("click", function() {
    document.getElementById("address-form").style.display = "none"; 
    document.getElementById("main-part2").style.display = "flex";
    document.getElementById("address-form").reset();
});

function open_address_form() {
    document.getElementById("address-form").style.display = "flex"; 
    document.getElementById("main-part2").style.display = "none";
    document.getElementById("add-address-button").style.display = "none";
}