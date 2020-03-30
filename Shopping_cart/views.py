from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView, View
from .models import Item
from geekprofile.models import Profile
from details.models import Book
from .models import Order, OrderItem

class CheckoutView(View):
    model = Item
    template_name = "checkout.html"

    def get(self, *args, **kwargs):
        try:
            order = Order.objects.get(user=self.request.user, ordered=False)
            #form = CheckoutForm()
            context = {
                #'form': form,
                #'couponform': CouponForm(),
                'order': order,
                #'DISPLAY_COUPON_FORM': True
            }

            """
            shipping_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='S',
                default=True
            )
            """

            """if shipping_address_qs.exists():
                context.update(
                    {'default_shipping_address': shipping_address_qs[0]})

            billing_address_qs = Address.objects.filter(
                user=self.request.user,
                address_type='B',
                default=True
            )
            if billing_address_qs.exists():
                context.update(
                    {'default_billing_address': billing_address_qs[0]})"""

            return render(self.request, "checkout.html", context)
        except ObjectDoesNotExist:
            messages.info(self.request, "You do not have an active order")
            return redirect("checkout")


def item_list(request):
    context = {
        'items' : Book.objects.all()
    }
    #return render(request, "checkout-page.html", context)
    return render(request, "checkout.html", context)

def add_to_cart(request, slug):
    item = get_object_or_404(Book, slug=Book.slug)









    


