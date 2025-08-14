const api = ApiFactory();

const speechEl = document.getElementById('speech');
const nluOut = document.getElementById('nluOut');
const orderPreview = document.getElementById('orderPreview');
const orderResult = document.getElementById('orderResult');

let items = [];

document.getElementById('btnParse').onclick = async () => {
  const txt = speechEl.value || "i'll have one cheeseburger no pickles and a large coke";
  const nlu = await api.parseNLU(txt);
  nluOut.textContent = JSON.stringify(nlu, null, 2);

  // naive auto-add: if menu_item found, push items
  const entityItem = nlu.entities.find(e => e.type === 'menu_item');
  const size = (nlu.entities.find(e => e.type === 'size') || {}).value;
  const qty = (nlu.entities.find(e => e.type === 'quantity') || { value: 1}).value;
  const mod = (nlu.entities.find(e => e.type === 'modifier') || {}).value;

  if (entityItem) {
    items.push({ item_id: entityItem.value, qty: qty, size: size, mods: mod ? [mod] : [] });
    orderPreview.textContent = JSON.stringify(items, null, 2);
  }
};

// quick add buttons
document.getElementById('btnAddBurger').onclick = () => {
  items.push({ item_id: 'burger_cheese', qty: 1 });
  orderPreview.textContent = JSON.stringify(items, null, 2);
};
document.getElementById('btnAddFries').onclick = () => {
  items.push({ item_id: 'fries', qty: 1, size: 'medium' });
  orderPreview.textContent = JSON.stringify(items, null, 2);
};
document.getElementById('btnAddCola').onclick = () => {
  items.push({ item_id: 'cola', qty: 1, size: 'large' });
  orderPreview.textContent = JSON.stringify(items, null, 2);
};

document.getElementById('btnPreview').onclick = async () => {
  const res = await api.previewOrder(items);
  orderResult.textContent = JSON.stringify(res, null, 2);
};

document.getElementById('btnConfirm').onclick = async () => {
  const res = await api.confirmOrder(items);
  orderResult.textContent = JSON.stringify(res, null, 2);
  items = [];
  orderPreview.textContent = "[]";
};
