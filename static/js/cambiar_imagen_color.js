  document.querySelectorAll('.color-options .color').forEach(span => {
    span.addEventListener('click', () => {
      const idObjetivo = span.dataset.target;
      const imagen = span.dataset.img;
      const divObjetivo = document.querySelector(`#${idObjetivo} .product-image.default`);
      if (divObjetivo) {
        divObjetivo.style.backgroundImage = `url('${imagen}')`;
      }

      span.parentElement.querySelectorAll('.color').forEach(s => s.classList.remove('active'));
      span.classList.add('active');
    });
  });