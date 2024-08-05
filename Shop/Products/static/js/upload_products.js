const file = document.querySelector('#file')
const sendForm = document.querySelector('.form')
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;

sendForm.addEventListener('submit', (event)=>{
    event.preventDefault()
    const data = new FormData()
    data.append('file', file.files[0])
    console.log(file.files[0])
    fetch('', {
        method: "POST",
        headers: { 
            "X-CSRFToken": csrftoken
            },
        body: data
}).then((response)=>{
    window.location.assign('categories')
    console.log(response)
}).catch((response)=>{
    console.log(response)
})
})