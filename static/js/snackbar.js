function showSnackbar(snackType) {
    var x = document.getElementsByName(snackType);
    x.forEach(e => {
        e.className = "show";
        setTimeout(function(){ e.className = e.className.replace("show", ""); }, 3000);
    });
  }
  