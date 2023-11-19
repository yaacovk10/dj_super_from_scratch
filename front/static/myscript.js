let my_cart = []
let products = []
const MY_SERVER = "http://127.0.0.1:8000/"
// const MY_SERVER = "https://dj-supermarket.onrender.com/"
const cart_data = JSON.parse(localStorage.getItem("my_cart"))
const load_product = async () => {
  const res = await axios.get(MY_SERVER + "products")
  products = res.data
  display_products()
}
const load_cart = () => {

  if (cart_data === null) {
    console.log("cart empty")
    return
  }
  else {
    my_cart = cart_data
    console.log("cart loaded success")
    display_cart()
  }
}
const display_products = () => {
  display.innerHTML = `<div class="row row-cols-1 row-cols-md-5 g-4">` +
    products.map((prod, idx) => `<div class="col">
            <div class="card">
              <img src=${prod.img} class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">${prod.desc}</h5>
                <p class="card-text">${prod.price}</p>
                <button onclick = buy(${idx})>BUY</button>

              </div>
            </div>
          </div>`) + `</div>`
}
const buy = (idx) => {
  prod = products[idx]
  // console.log(prod)
  console.log(prod.id)
  console.log(my_cart)
  // console.log(my_cart.filter(x=>x.id === prod.id))
  if (my_cart.filter(x => x.id === prod.id).length > 0) {
    current_item = my_cart.filter(x => x.id === prod.id)[0]
    current_item.amount += 1
  }
  else {
    my_cart.push({ "description": prod.desc, "price": prod.price, "amount": 1, "image": prod.img, "id": prod.id })
  }
  //add to local storage
  localStorage.setItem("my_cart", JSON.stringify(my_cart))
  console.table(my_cart)
  display_cart()

}
const display_cart = () => {
  cart.innerHTML =  `<div class="row row-cols-1 row-cols-md-5 g-4">`+
    my_cart.map((cart, idx) => `<div class="col">
    <div class="card">
      <img src=${cart.image} class="card-img-top" alt="...">
      <div class="card-body">
        <h5 class="card-title">${cart.description}</h5>
        <p class="card-text">${cart.price}</p>
        <p class="card-text">${cart.amount}</p>
        <p class="card-text">
      </div>
    </div>
  </div>`) + `</div>`
}
// load_product()
// load_cart()