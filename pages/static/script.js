function toggleTheme(theme) {
    //get the link to the sylesheet using its id
    let themeLink = document.getElementById('theme');
    //update the link to the stylesheet by having the href link go into the static folder and then find the theme
    //the theme is passed when we call the function in base.html
    themeLink.href = "/static/" + theme
}
