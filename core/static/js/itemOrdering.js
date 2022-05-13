const filter = document.getElementById('orderBy');
window.addEventListener('load', function() {
    const query_params = window.location.search.split('&')
    const selected = query_params[0].split("=")[1];
    let query = "";
    try{
        query =  query_params[1].split("=")[1];
    } catch {

    }
    let query_field = document.getElementById("searchQuery")
    try {
        query_field.value = query
    } catch{

    }

    if (selected !== undefined){
        filter.value = selected;
  }
});

filter.addEventListener('change', (e) => {
    let query = "";
    try{
        query = document.getElementById("searchQuery").value;
    } catch {
        query = ""
    }
    window.location.href = `?sort=${filter.value}&query=${query}`;
});
