function formvalidate(){
    var x = document.forms["Registration"]["f_name"].value;
    var y = document.forms["Registration"]["l_name"].value;
    var z = document.forms["Registration"]["pin_code"].value;
    var a = document.forms["Registration"]["password1"].value;
    var b = document.forms["Registration"]["password2"].value;
    var pat1=/^\d{6}$/;
    var passwrd= /^(?=.*[0-9])(?=.*[!@#$%^&*])[a-zA-Z0-9!@#$%^&*]{7,15}$/;

  if (x == "" || y=="") {
    alert("Please Enter Your Full Name");
    return false;
  }

  if(!pat1.test(z))
    {
    alert("Pin code should be 6 digits ");
    return false
    }

    
	if(!a.match(passwrd))
	{
    alert("Please enter a password between 7 to 15 characters which contain at least one numeric digit and a special character");
    return false;
    }
    
    if(a!=b){
        alert("Passwords do  not match");
        return false
    }
}