import stripe
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponse
from django.contrib import messages
from django.core.paginator import Paginator
from .models import Order, Product, Category, Cart, CartItem

# Stripe API key
stripe.api_key = settings.STRIPE_SECRET_KEY


# Home view
def home(request):
    categories = Category.objects.all()
    products = Product.objects.all()
    return render(request, 'shop/home.html', {'products': products, 'categories': categories})


# Product detail view
def product_detail(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    return render(request, 'shop/product_detail.html', {'product': product})


# Add product to cart
def add_to_cart(request, product_id):
    try:
        product = Product.objects.get(id=product_id)
    except Product.DoesNotExist:
        messages.error(request, "The product does not exist.")
        return redirect('home')

    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)

        cart_item.quantity = cart_item.quantity + 1 if not created else 1
        cart_item.save()

        messages.success(request, f"{product.name} added to cart.")
        return redirect('cart')
    # else:
    #     messages.error(request, "You need to be logged in to add items to the cart.")
    #     return redirect('login')


# Cart page
def cart_page(request):
    if request.user.is_authenticated:
        cart, created = Cart.objects.get_or_create(user=request.user)
        cart_items = CartItem.objects.filter(cart=cart)
        total = sum(item.product.price * item.quantity for item in cart_items)

        if request.method == "POST" and request.POST.get("action") == "place_order":
            if cart_items.exists():
                for item in cart_items:
                    Order.objects.create(
                        user=request.user,
                        product=item.product,
                        quantity=item.quantity,
                        status="Pending"
                    )
                cart_items.delete()
                messages.success(request, "Your order has been placed successfully!")
                return redirect('order_confirmation')
            else:
                messages.error(request, "Your cart is empty!")

        return render(request, 'shop/cart.html', {'cart_items': cart_items, 'total': total})
    else:
        messages.error(request, "You need to be logged in to view your cart.")
        return redirect('login')


# Order confirmation view
def order_confirmation(request):
    return render(request, 'shop/order_confirmation.html')


# Remove product from cart
def remove_from_cart(request, product_id):
    if request.user.is_authenticated:
        try:
            cart = Cart.objects.get(user=request.user)
            cart_item = CartItem.objects.get(cart=cart, product_id=product_id)
            cart_item.delete()
            messages.success(request, "Item removed from cart.")
        except CartItem.DoesNotExist:
            messages.error(request, "This item is not in your cart.")

        return redirect('cart')
    else:
        messages.error(request, "You need to be logged in to remove items from the cart.")
        return redirect('login')


# Search view
def search(request):
    query = request.GET.get('q')
    if not query:
        message = "Please enter a search term."
        return render(request, 'shop/search_results.html', {'message': message})

    products = Product.objects.filter(name__icontains=query)
    if not products.exists():
        message = "No products match your search query."
        return render(request, 'shop/search_results.html', {'message': message})

    paginator = Paginator(products, 9)  # 9 products per page
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    return render(request, 'shop/search_results.html', {'page_obj': page_obj})


# Category view
def category_view(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    products_in_category = Product.objects.filter(category=category)
    return render(request, 'shop/category_page.html', {
        'category': category,
        'products': products_in_category
    })


# Update cart quantity
def update_cart_quantity(request, item_id):
    if request.method == 'POST':
        new_quantity = int(request.POST.get('quantity'))
        item = get_object_or_404(CartItem, id=item_id)
        item.quantity = new_quantity
        item.save()
        return redirect('cart')
