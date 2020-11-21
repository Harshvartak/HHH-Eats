function descen(){
  console.log("HI",document.getElementsByClassName("mine").length)
  var i,j;
  final=""
  for (j=0 ;j<document.getElementsByClassName("mine").length-1;j++){
    for (i=0 ;i<document.getElementsByClassName("mine").length-1;i++){
      console.log(parseInt(document.getElementsByClassName("mine")[i].getElementsByClassName("value")[1].innerText)>parseInt(document.getElementsByClassName("mine")[i+1].getElementsByClassName("value")[1].innerText));
      if (parseInt(document.getElementsByClassName("mine")[i].getElementsByClassName("value")[1].innerText)>parseInt(document.getElementsByClassName("mine")[i+1].getElementsByClassName("value")[1].innerText))
      {
        var temp=document.getElementsByClassName("mine")[i].innerHTML;
        document.getElementsByClassName("mine")[i].innerHTML=document.getElementsByClassName("mine")[i+1].innerHTML;
        document.getElementsByClassName("mine")[i+1].innerHTML=temp;

      }
    }
  }
}


function ascen(){
  console.log("HIIIII",document.getElementsByClassName("mine").length)
  var i,j;
  final=""
  for (j=0 ;j<document.getElementsByClassName("mine").length-1;j++){
    console.log("Here");
    for (j=0 ;j<document.getElementsByClassName("mine").length-1;j++){
      console.log(parseInt(document.getElementsByClassName("mine")[i].getElementsByClassName("value")[1].innerText)>parseInt(document.getElementsByClassName("mine")[i+1].getElementsByClassName("value")[1].innerText));
      if (parseInt(document.getElementsByClassName("mine")[i].getElementsByClassName("value")[1].innerText)<parseInt(document.getElementsByClassName("mine")[i+1].getElementsByClassName("value")[1].innerText))
      {
        var temp=document.getElementsByClassName("mine")[i].innerHTML;
        document.getElementsByClassName("mine")[i].innerHTML=document.getElementsByClassName("mine")[i+1].innerHTML;
        document.getElementsByClassName("mine")[i+1].innerHTML=temp;

      }
    }
  }
}
