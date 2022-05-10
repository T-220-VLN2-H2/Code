/*
@author: Sigurður Friðriksson
 */


// Get tabs items
const tabs = document.getElementsByClassName('nav-link');

// When the tab is clicked,
// remove all active classes and give the target the active class
const clearActive = (e) => {
  for (let i = 0; i < tabs.length; i++) {
    tabs[i].classList.remove('active');
  }
  e.target.classList.add('active');
};

// Checks if the url provided has the tab names
// and sets that tab as active
const setActive = () => {
  console.log(window.location.hash);
  switch (window.location.hash) {
    case '#bids':
      const bidsTab = document.getElementById('active-bids-tab');
      bidsTab.click();
      break;
    case '#active-sales':
      console.log('active-sales');
      const activeSalesTab = document.getElementById('active-sales-tab');
      activeSalesTab.click();
      break;
    case '#sales':
      console.log('sales');
      const salesTab = document.getElementById('active-sales');
      salesTab.click();
      break;
    case '#purchases':
      console.log('purchases');
      const buyTab = document.getElementById('purchases-tab');
      buyTab.click();
      break;
  }
};
// Hack to set the correct page onload
setTimeout(() => {
  setActive();
}, 1);

// Add an eventlistener to each tab
for (let i = 0; i < tabs.length; i++) {
  tabs[i].addEventListener('click', clearActive);
}
// Add an eventListener for the hash change
window.addEventListener('hashchange', setActive);

window.onload = (e) => {
  console.log('Loaded');
  setActive();
};

