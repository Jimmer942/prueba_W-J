function login(){
    const loginform = document.getElementById("loginform");
    console.log("Form testing");
    loginform.addEventListener("sumbit", (e) => {
        e.preventDefault();
        console.log("Form testing");
    })
}