function myFunction(id) {
  var x = document.getElementById(id);
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
    x.previousElementSibling.className += " w3-theme-d1";
  } else { 
    x.className = x.className.replace("w3-show", "");
    x.previousElementSibling.className = 
    x.previousElementSibling.className.replace(" w3-theme-d1", "");
  }
}

function openNav() {
  var x = document.getElementById("navDemo");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}

function openNav1() {
  var x = document.getElementById("navDemo1");
  if (x.className.indexOf("w3-show") == -1) {
    x.className += " w3-show";
  } else { 
    x.className = x.className.replace(" w3-show", "");
  }
}

function confirmar_excluir_post(id){
  if (confirm('Tem certeza que deseja excluir esta postagem ?')){
    document.location.href = '/postagem/excluir/' + id + '/'
  }
}

function confirmBloquear(perfil){
    if (confirm('Deseja realmente bloquear este perfil?')){
      document.location.href = '/perfil/bloquear/' + perfil + '/'
    }
}
