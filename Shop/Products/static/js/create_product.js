const name = document.querySelector('#name');
const price = document.querySelector('#price');
const description = document.querySelector('#description');
const image = document.querySelector('#image');
const categorySelect= document.querySelector('#category')
const productForm = document.querySelector('.form');
const csrftoken = document.querySelector("[name=csrfmiddlewaretoken]").value;


productForm.addEventListener('submit', (event)=>{
    event.preventDefault()
    fetch('', {
        method: "POST",
        headers: { 
            "X-CSRFToken": csrftoken,
            // to indicate explicitly that you POST data in JSON format.
            'Content-Type': 'application/json'
            },
        body: JSON.stringify({    
        'name': name.value,
        'price': price.value,
        'description': description.value,
        'image': image.value,
        'category': categorySelect.options[categorySelect.selectedIndex].value
    })

    }).then((response)=>{
        console.log(response)
    }).catch((response)=>{
        console.log(response)
    })
})