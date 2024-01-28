from django.contrib import admin
from django.urls import path, include

from ecommerce import views as ecom_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path("ecommerce/", ecom_views.ecommerce_index_view),
    path("ecommerce/item/<item_id>", ecom_views.item_view),
    path("homepage/", ecom_views.homepage_view),
    path("ecommerce/category/<category_id>", ecom_views.category_view),
    path("ecommerce/product/<product_id>", ecom_views.product_view),
    path("ecommerce/checkout/", ecom_views.checkout_view),
    path("ecommerce/contact/", ecom_views.contact_view),
]



