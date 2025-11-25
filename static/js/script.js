document.addEventListener('DOMContentLoaded', () => {
    // Cerrar automáticamente alertas de Bootstrap
    document.querySelectorAll('.alert').forEach(alert => {
        setTimeout(() => new bootstrap.Alert(alert).close(), 5000);
    });

    // Código de la escena solo si existe
    const svg = document.getElementById('escena');
    if (!svg) return;

    // Añadir gradientes
    const defs = document.createElementNS("http://www.w3.org/2000/svg", "defs");
    defs.innerHTML = `
        <linearGradient id="amanecer" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#FFD580"/>
            <stop offset="100%" stop-color="#FFFAE3"/>
        </linearGradient>
        <linearGradient id="dia" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#87CEEB"/>
            <stop offset="100%" stop-color="#ffffff"/>
        </linearGradient>
        <linearGradient id="atardecer" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#FF8C00"/>
            <stop offset="100%" stop-color="#FFD580"/>
        </linearGradient>
        <linearGradient id="noche" x1="0" y1="0" x2="0" y2="1">
            <stop offset="0%" stop-color="#001848"/>
            <stop offset="100%" stop-color="#0A043C"/>
        </linearGradient>
    `;
    svg.prepend(defs);

    // Función para actualizar color de las ventanas
    const actualizarCielo = () => {
        const hora = new Date().getHours();
        const color = (hora >= 6 && hora < 9) ? 'url(#amanecer)' :
                      (hora >= 9 && hora < 17) ? 'url(#dia)' :
                      (hora >= 17 && hora < 20) ? 'url(#atardecer)' :
                      'url(#noche)';

        svg.querySelectorAll('.ventana').forEach(v => v.setAttribute('fill', color));
    };

    actualizarCielo();
    setInterval(actualizarCielo, 60000);
});