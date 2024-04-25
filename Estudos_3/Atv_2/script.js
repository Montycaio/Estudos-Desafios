
function abrirAlerta() {
    swal({
        title: "Você tem certeza?",
        text: "Uma vez enviado, você não poderá modificar este formulário!",
        icon: "warning",
        buttons: true,
        dangerMode: true,
      })
      .then((willDelete) => {
        if (willDelete) {
          swal("Formulário foi enviado com sucesso!", {
            icon: "success",
          });
        } else {
          swal("Ok. Revise seu formulário antes de enviar.");
        }
      });
}