
function confirmarEliminacion(id) {
    
    Swal.fire({
        title: '¿Estas seguro que deseas eliminar tu producto publicado?',
        text: "No podras revertir esta accion",
        type: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Confirmar',
        cancelButtonText: 'Cancelar'
    }).then((resutl) => {
        if (resutl.value) {
            window.location.href = "/eliminar_producto"+id+"/";               
            
        }
    })
}