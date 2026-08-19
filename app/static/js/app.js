document.querySelectorAll('[data-endpoint]').forEach((button) => {
  button.addEventListener('click', async () => {
    const output = document.querySelector('#api-output');
    try {
      const response = await fetch(button.dataset.endpoint);
      const data = await response.json();
      output.textContent = JSON.stringify(data, null, 2);
    } catch (error) {
      output.textContent = `No se pudo consultar la API: ${error.message}`;
    }
  });
});
