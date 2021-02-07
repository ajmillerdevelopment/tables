//Materialize Functionality
M.AutoInit();

document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.modal');
    var instances = M.Modal.init(elems, options);
  });
  
  document.addEventListener('DOMContentLoaded', function() {
    var elems = document.querySelectorAll('.collapsible');
    var instances = M.Collapsible.init(elems, options);
  });

// Event listener on modal buttons to trigger script
// Grab order ID and append 'modal'
// Grab Seat Number
// Grab IDs of selected items and append 'select-options-1615d5d2-47d1-9efd-7c5a-94ca1cfb399e'
// Select Seat Input and change 'name' to Seat Number
// Select IDs of selected items and add class 'selected'
const buttons = document.querySelectorAll('.order-modal')
for (let button of buttons) {
  button.addEventListener("click", ()=> {
    const orderID = button.id
    const seatID = document.querySelector(`.seat${orderID}`).innerHTML
    const items = document.querySelectorAll(`.item${orderID}`)
    const itemIDs = []
    const seat = document.querySelector(`#form${orderID} p #id_seat`)
    const prefix = document.querySelector(`#form${orderID} p div ul`).id
    for (let item of items) {
      itemIDs.push(prefix + (item.id - 1))
    }
    seat.setAttribute("value", `${seatID}`)
    for (let itemID of itemIDs) {
      let toSelect = document.querySelector(`#form${orderID} p div ul #${itemID}`)
      toSelect.setAttribute("class", "selected")
    }
  })
}