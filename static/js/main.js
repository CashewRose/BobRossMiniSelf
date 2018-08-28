console.log('test')

document.getElementById('js-clicker').addEventListener('click', () => {
    console.log("Hey dont touch me there! It's my private button square...")
    fetch('/birthdays')
    .then(function(response){
        return response.json()
    })
    .then(function(response){
        console.table(response)
        for(i = 0; i < response.length; i++){
            ul = document.createElement("ul")
            ul.innerHTML = "<h2>" + response[i].Name + "</h2>"
            li1 = document.createElement("li");
            li2 = document.createElement("li");
            li1.innerHTML += "Date: " + response[i].Date
            li2.innerHTML += "Greeting: " + response[i].Greeting
            ul.appendChild(li1)
            ul.appendChild(li2)
            document.getElementById('js-clicker').parentNode.appendChild(ul)
        }
    })
})
