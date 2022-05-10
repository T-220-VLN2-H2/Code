const filter = document.getElementById('orderBy');
window.addEventListener('load', function() {
  const selected = window.location.search.split('=')[1];
  filter.value = selected;
});

filter.addEventListener('change', (e) => {
  window.location.href = `?sort=${filter.value}`;
});
