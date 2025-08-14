const API = (base = (localStorage.getItem('apiBase') || 'http://localhost:8000')) => ({
  parseNLU: async (text) => {
    const res = await fetch(base + '/nlu/parse', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ text })
    });
    return res.json();
  },
  previewOrder: async (items) => {
    const res = await fetch(base + '/orders/preview', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(items)
    });
    return res.json();
  },
  confirmOrder: async (items) => {
    const res = await fetch(base + '/orders/confirm', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify(items)
    });
    return res.json();
  },
  getMenu: async () => {
    const res = await fetch(base + '/menu/');
    return res.json();
  }
});
window.ApiFactory = API;
