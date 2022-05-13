const filter = document.getElementById('orderBy');
window.addEventListener('load', function() {
    const query_params = window.location.search.split('&')
    const selected = query_params[0].split("=")[1];
    const query =  query_params[1].split("=")[1];
    let query_field = document.getElementById("searchQuery")
    query_field.value = query
    if (selected !== undefined){
        filter.value = selected;
  }
});

filter.addEventListener('change', (e) => {
    const query = document.getElementById("searchQuery").value;
    window.location.href = `?sort=${filter.value}&query=${query}`;
});
