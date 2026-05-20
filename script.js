const track = document.getElementById('sliderTrack');
const slides = document.querySelectorAll('.slide');
const priceDisplay = document.querySelector('.ecommerce-bar .price span');
const carSections = document.querySelectorAll('.car-section');

// Cart Elements
const cartCount = document.querySelector('.cart-count');
const cartItemsContainer = document.getElementById('cartItems');
const cartTotalElement = document.getElementById('cartTotal');
const cartSidebar = document.getElementById('cartSidebar');
const checkoutModal = document.getElementById('checkoutModal');

let currentIndex = 0;
let cart = [];

function moveSlide(direction) {
  currentIndex += direction;
  if (currentIndex < 0) currentIndex = slides.length - 1;
  if (currentIndex >= slides.length) currentIndex = 0;
  
  updateSlider();
}

function updateSlider() {
  track.style.transform = `translateX(-${currentIndex * 100}vw)`;
  const currentSection = carSections[currentIndex];
  priceDisplay.textContent = currentSection.getAttribute('data-price');
  window.scrollTo({ top: 0, behavior: 'smooth' });
}

// Ecommerce Functions
function addToCart() {
  const currentSection = carSections[currentIndex];
  const name = currentSection.getAttribute('data-name');
  const priceStr = currentSection.getAttribute('data-price');
  const image = currentSection.getAttribute('data-image');
  
  const priceNum = parseInt(priceStr.replace(/[^0-9]/g, ''), 10);
  
  const existingItem = cart.find(item => item.name === name);
  if (existingItem) {
    existingItem.quantity += 1;
  } else {
    cart.push({ name, priceStr, priceNum, image, quantity: 1 });
  }
  
  updateCartUI();
  
  const btn = document.querySelector('.buy-btn');
  const originalText = btn.textContent;
  btn.textContent = "Ditambahkan ✓";
  btn.style.background = "#28a745";
  setTimeout(() => {
    btn.textContent = "Masukkan Keranjang";
    btn.style.background = "";
  }, 1500);
  
  // Auto open cart
  if(!cartSidebar.classList.contains('active')){
     toggleCart();
  }
}

function updateCartUI() {
  cartCount.textContent = cart.reduce((total, item) => total + item.quantity, 0);
  
  cartItemsContainer.innerHTML = '';
  let totalNum = 0;
  
  if (cart.length === 0) {
    cartItemsContainer.innerHTML = '<p style="text-align:center; color:#888; margin-top:40px;">Keranjang kosong.</p>';
  } else {
    cart.forEach((item, index) => {
      totalNum += item.priceNum * item.quantity;
      const formatPrice = new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', minimumFractionDigits: 0 }).format(item.priceNum * item.quantity);
      
      cartItemsContainer.innerHTML += `
        <div class="cart-item">
          <img src="${item.image}" alt="${item.name}">
          <div class="item-details">
            <h4 style="color:#fff; margin-bottom:5px;">${item.name}</h4>
            <p style="color:#aaa; font-size:0.9rem; margin-bottom:10px;">${formatPrice}</p>
            <div class="item-controls">
              <button onclick="changeQuantity(${index}, -1)">-</button>
              <span style="color:#fff; min-width:20px; text-align:center;">${item.quantity}</span>
              <button onclick="changeQuantity(${index}, 1)">+</button>
            </div>
          </div>
        </div>
      `;
    });
  }
  
  cartTotalElement.textContent = new Intl.NumberFormat('id-ID', { style: 'currency', currency: 'IDR', minimumFractionDigits: 0 }).format(totalNum);
}

function changeQuantity(index, delta) {
  cart[index].quantity += delta;
  if (cart[index].quantity <= 0) {
    cart.splice(index, 1);
  }
  updateCartUI();
}

function toggleCart() {
  cartSidebar.classList.toggle('active');
}

function checkout() {
  if (cart.length === 0) {
    alert('Keranjang belanja Anda kosong!');
    return;
  }
  toggleCart();
  checkoutModal.classList.add('active');
}

function closeCheckout() {
  checkoutModal.classList.remove('active');
}

function submitOrder(e) {
  e.preventDefault();
  alert('Pembayaran Berhasil! Tim pengiriman global kami akan segera menghubungi Anda untuk mengatur logistik.');
  cart = [];
  updateCartUI();
  closeCheckout();
  document.getElementById('checkoutForm').reset();
}

// Init
updateCartUI();
