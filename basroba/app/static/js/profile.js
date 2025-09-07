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
    const name = document.getElementById("name").value;
    const phone = document.getElementById("phone").value;
    const address = document.getElementById("address").value;
    const city = document.getElementById("city").value;
    const state = document.getElementById("state").value;
    const zip_code = document.getElementById("zip_code").value;

    fetch("/api/save_user/", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
            "X-CSRFToken": getCookie("csrftoken")
        },
        body: JSON.stringify({
            name: name,
            phone: phone,
            address: address,
            city: city,
            state: state,
            zip_code: zip_code
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

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }   
        }
    }
    return cookieValue;
}