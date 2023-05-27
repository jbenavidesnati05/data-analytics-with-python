let btn = document.getElementById("btnGenerarReporte")

btn.addEventListener("click",function(evento){
    evento.preventDefault()

    let contenedor  = document.getElementById("contenedor")
    contenedor.classList.remove('d-none')

    let nombreUsuario = document.getElementById("nombre").value
    alert(nombreUsuario)

    let mensaje = document.getElementById("mensaje")

    mensaje.textContent = ` apreciado = ${nombreUsuario}`

})
