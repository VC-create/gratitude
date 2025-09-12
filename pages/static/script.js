switches = document.getElementsByClassName("swtich");

//loops through switches
for(i of switches){
    //this adds event listener to each of the switches
    i.addEventListener("click", () => {
        theme = i.dataset.theme;
        setTheme(theme)
    })
}

function setTheme(theme){
    switch(theme){
        case "summer": document.getElementById("switcher-id").href = "/static/summer.css"
        return;
        case "fall": document.getElementById("switcher-id").href = ".static/fall.css"
        return;
        case "winter": document.getElementById("switcher-id").href = ".static/winter.css"
        return;
        case "spring": document.getElementById("switcher-id").href = ".static/spring.css"
        return;
    }
}