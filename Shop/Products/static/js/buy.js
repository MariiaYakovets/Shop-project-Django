const button = document.querySelector('#b-button')
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;


button.addEventListener("click", (event)=>{
    event.preventDefault()
    fetch('', {
        method: "POST",
        headers: {
            "X-CSRFToken": csrftoken,
            'Content-Type': 'application/json'
        }, 
        body: JSON.stringify({
            // data-id="{{product.id}} in html
            id: button.dataset.id
        })
    }).then((response)=>{
        console.log(response)
    }).catch((response)=>{
        console.log(response)
    })})

