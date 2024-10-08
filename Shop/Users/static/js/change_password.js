newPassword = document.querySelector('#password')
repPassword = document.querySelector('#repeat-password')
regForm = document.querySelector('.form')
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

regForm.addEventListener('submit', (event)=>{
    event.preventDefault()
    if(newPassword.value == repPassword.value){
        fetch('', {
            method: "POST",
            headers: { 
                "X-CSRFToken": csrftoken,
                // to indicate explicitly that you POST data in JSON format.
                'Content-Type': 'application/json'
             },
            body: JSON.stringify({    
            'password': newPassword.value
        })
        }).then((response)=>{
            console.log(response)
            // django can not do redirect from views, next line will
            window.location.assign("/user")
        }).catch((response)=>{
            console.log(response)
        });
    }
})