function bringInForm(){
    //commonly accessed elements
    blackFade = document.getElementById("blackFade");
    popupForm = document.getElementById("popup");
    popupForm.style.display="block";
    blackFade.style.display="block";
}

function hideForms(){
    //commonly accessed elements
    blackFade = document.getElementById("blackFade");
    popupForm = document.getElementById("popup");
    signUpPopupForm = document.getElementById("signUpPopup");
    popupForm.style.display="none";
    blackFade.style.display="none";
}

function signInFormValidation(){
    return true;

}

function signUpFormValidation(){ 
    unameField = document.forms["signUpForm"]["uname"].value;
    emailField = document.forms["signUpForm"]["email"].value;
    pwordField = document.forms["signUpForm"]["pword1"].value;
    verifyField = document.forms["signUpForm"]["pword2"].value;
    errorField = document.getElementById("errorMessage");
    console.log(unameField.innerHTML);
    if(emailField.indexOf("@") == -1 || emailField.indexOf(".") == -1){
        errorField.innerHTML = "Please enter a valid email address!"
        return false;
    }
   //Todo password validation
   else if(pwordField != verifyField){
        errorField.innerHTML = "Make sure that the passwords match!"
       return false;
   }
    return true;
}