/*
@author: Sigurður Friðriksson
 */


// Get tabs items
const tabs = document.getElementsByClassName('nav-link');

// When the tab is clicked, remove all active classes and give the target the active class
const clearActive = (e) => {
  for (let i = 0; i < tabs.length; i++) {
    tabs[i].classList.remove('active');
  }
  e.target.classList.add('active');
};

// Add an eventlistener to each tab
for (let i = 0; i < tabs.length; i++) {
  tabs[i].addEventListener('click', clearActive);
}

// Checks if the url provided has the tab names and sets that tab as active
switch (window.location.href.split('#')[1]) {
  case 'bids':
    const bidsTab = document.getElementById('active-bids-tab');
    for (let i = 0; i < tabs.length; i++) {
      tabs[i].classList.remove('active');
    }
    bidsTab.classList.add('active');
    break;
  case 'active-sales':
    console.log('active-sales');
    const activeSalesTab = document.getElementById('active-sales-tab');
    for (let i = 0; i < tabs.length; i++) {
      // tabs[i].addEventListener("click", setActive)
      tabs[i].classList.remove('active');
    }
    activeSalesTab.classList.add('active');
    break;
  case 'sales':
    console.log('sales');
    const salesTab = document.getElementById('active-sales');
    for (let i = 0; i < tabs.length; i++) {
      tabs[i].classList.remove('active');
      console.log(tabs[i].classList);
    }
    salesTab.classList.add('active');
    break;
  case 'purchases':
    console.log('purchases');
    const buyTab = document.getElementById('purchases-tab');
    for (let i = 0; i < tabs.length; i++) {
      tabs[i].classList.remove('active');
    }
    buyTab.classList.add('active');
    break;
}


