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
    const street_address1 = prompt("Enter Street Address 1:");
    const street_address2 = prompt("Enter Street Address 2 (optional):");
    const city = prompt("Enter City:");
    const state_region = prompt("Enter State/Region:");
    const zip_code = prompt("Enter ZIP Code:");
    const country = prompt("Enter Country:");
    const phone_code = prompt("Enter Phone Code:");
    const phone_number = prompt("Enter Phone Number:");
    if (!street_address1 || !city || !state_region || !zip_code || !country || !phone_code || !phone_number) {
        alert("All fields except Street Address 2 are required.");
        return;
    }
    fetch("/api/add_address/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            street_address1: street_address1,
            street_address2: street_address2,
            city: city,
            state_region: state_region,
            zip_code: zip_code,
            country: country,
            phone_code: phone_code,
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