/* When the user clicks on the button,
toggle between hiding and showing the dropdown content */
async function search() {
  const searchRequest = async (q) => {
    const result = await fetch(`/api/search`, {
      method: 'GET',
    }).then((r) => r.json());
    return result;
  };
  const clearChildren = async (parent) => {
    while (parent.firstChild) {
      parent.removeChild(parent.firstChild);
    }
  };
  const searchDrop = document.getElementById('myDropdown');
  await clearChildren(searchDrop);
  const searchInput = document.getElementById('myInput');
  const searchResult = await searchRequest(searchInput.value);
  for (let i = 0; i < searchResult.length; i++) {
    const a = document.createElement('a');
    a.text = `${searchResult[i].title} price: ${searchResult[i].price}`;
    a.href = `/items/${searchResult[i].id}`;
    searchDrop.appendChild(a);
  }
}
const toggleSearchDrop = () => {
  const searchDrop = document.getElementById('myDropdown');
  searchDrop.classList.toggle('show');
};
async function filterFunction() {
  let input; let filter; let a; let i;
  input = document.getElementById('myInput');
  filter = input.value.toUpperCase();
  const div = document.getElementById('myDropdown');
  a = div.getElementsByTagName('a');
  for (i = 0; i < a.length; i++) {
    const txtValue = a[i].textContent || a[i].innerText;
    if (txtValue.toUpperCase().indexOf(filter) > -1) {
      a[i].style.display = '';
    } else {
      a[i].style.display = 'none';
    }
  }
}

window.onload = () => {
  const searchDrop = document.getElementById('myInput');
  const searchItems = document.getElementById('myDropdown');
  searchDrop.addEventListener('focus', () => {
    toggleSearchDrop();
    search();
  });
  searchDrop.addEventListener('keyup', () => {
    filterFunction();
  });
  window.addEventListener('click', (e) => {
    if (e.target !== searchDrop) {
      toggleSearchDrop();
    }
  });
};

