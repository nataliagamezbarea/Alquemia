    // Función para mostrar el mapa cuando se hace clic en una tienda
    function mostrarmapa(tiendaCard) {
    var mapaaUrl = tiendaCard.getAttribute("data-url");

    var iframe = document.getElementById("mapa-frame");
    iframe.src = mapaaUrl;
    iframe.style.display = 'block';
    document.getElementById("mapa-message").style.display = 'none';
}

    window.onload = function() {
        var iframe = document.getElementById("mapa-frame");
        iframe.style.display = 'none'; // Asegurarse de que el iframe está oculto al inicio
        document.getElementById("mapa-message").style.display = 'block'; // Asegurarse de que el mensaje se muestra
    }
