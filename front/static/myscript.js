let my_cart = []
let products = []
// const MY_SERVER = "http://127.0.0.1:8000/"
const MY_SERVER = "https://dj-supermarket.onrender.com/"
        const load_product = async ()=>{
            const res = await axios.get(MY_SERVER + "products")
            products = res.data
            console.log(res.data);
            display.innerHTML= `<div class="row row-cols-1 row-cols-md-5 g-4">`+
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
        const buy = (idx) =>{
            prod = products[idx]
            console.log("product item" + prod.desc)
            my_cart.push({"description" : prod.desc , "price" : prod.price, "amount" :  1 , "image": prod.img})
            console.log(my_cart);
            cart.innerHTML =  `<div class="row row-cols-1 row-cols-md-5 g-4">`+
            my_cart.map((cart, idx) => `<div class="col">
            <div class="card">
              <img src=${cart.image} class="card-img-top" alt="...">
              <div class="card-body">
                <h5 class="card-title">${cart.description}</h5>
                <p class="card-text">${cart.price}</p>
                <p class="card-text">${cart.amount}</p>,

              </div>
            </div>
          </div>`) + `</div>`
        }
        load_product()