document.addEventListener('DOMContentLoaded', () => {
    const alerts = document.querySelectorAll('.alert');
    alerts.forEach(alert => {
        setTimeout(() => {
            const bsAlert = new bootstrap.Alert(alert);
            bsAlert.close();
        }, 5000); // 5 segundos
    });
});


//Ventana en escritorio
function actualizarCielo() {
  const hora = new Date().getHours();
  const ventanas = document.querySelectorAll('.ventana');
  let color;

  if (hora >= 6 && hora < 9) color = 'url(#amanecer)';
  else if (hora >= 9 && hora < 17) color = 'url(#dia)';
  else if (hora >= 17 && hora < 20) color = 'url(#atardecer)';
  else color = 'url(#noche)';

  ventanas.forEach(v => v.setAttribute('fill', color));
}

// Añadimos gradientes al SVG
const svg = document.getElementById('escena');
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

actualizarCielo();
setInterval(actualizarCielo, 60000);