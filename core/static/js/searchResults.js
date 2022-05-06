/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
async function search() {
    const search = async (q) => {
        let result = await fetch(`/search`, {
            method: "GET"
        }).then((r) => r.json())
        return result
    }
    const clearChildren = async (parent) => {
        while(parent.firstChild){
            parent.removeChild(parent.firstChild)
        }
    }
    const searchDrop = document.getElementById("myDropdown");
    await clearChildren(searchDrop)
    const searchInput = document.getElementById("myInput");
    let searchResult = await search(searchInput.value);
    for (let i = 0; i < searchResult.length; i++){
        const a = document.createElement("a");
        a.text = `${searchResult[i].title} price: ${searchResult[i].price}`
        a.href = `/items/${searchResult[i].id}`
        searchDrop.appendChild(a)
    }

}
const toggleSearchDrop = () => {
    const searchDrop = document.getElementById("myDropdown");
    searchDrop.classList.toggle("show");
}
async function filterFunction() {
      let input, filter, ul, li, a, i;
      input = document.getElementById("myInput");
      filter = input.value.toUpperCase();
      let div = document.getElementById("myDropdown");
      a = div.getElementsByTagName("a");
      for (i = 0; i < a.length; i++) {
          let txtValue = a[i].textContent || a[i].innerText;
          if (txtValue.toUpperCase().indexOf(filter) > -1) {
          a[i].style.display = "";
          } else {
            a[i].style.display = "none";
          }
      }
}
