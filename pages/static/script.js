function toggleTheme(theme) {
    //get the link to the sylesheet using its id
    let themeLink = document.getElementById('theme');
    //update the link to the stylesheet by having the href link go into the static folder and then find the theme
    //the theme is passed when we call the function in base.html
    themeLink.href = "/static/" + theme;

    let musicLink = document.getElementById('music');

    if (theme == 'summer.css') {
        musicLink.src = "/static/audios/summer.mp3";
    } else if (theme == 'winter.css') {
        musicLink.src = "/static/audios/winter.mp3";
    } else if (theme =="fall.css") {
        musicLink.src = "/static/audios/fall.mp3"; 
    }
    else{
        musicLink.src = "/satic/audios/spring.mp3";
    }


    let audioLink = document.getElementById("audio");
    audioLink.load();
    audioLink.play();
}
