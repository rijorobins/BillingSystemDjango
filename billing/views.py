from django.shortcuts import render,redirect
from billing.models import Product,Purchase
from billing.forms import AddProductForm,AddPurchaseForm
from django.views.generic import TemplateView
# Create your views here.

class AddProductView(TemplateView):
    model = Product
    template_name = "billing/add_products.html"
    context = {}
    def get(self, request, *args, **kwargs):
        form = AddProductForm()
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = AddProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            self.context["form"] = form
            return render(request,self.template_name,self.context)
class ProductListView(TemplateView):
    model = Product
    template_name = "billing/product_list.html"
    context = {}
    def get(self, request, *args, **kwargs):
        products = self.model.objects.all()
        self.context["products"] = products
        return render(request,self.template_name,self.context)
class EditProductView(TemplateView):
    model = Product
    template_name = "billing/edit_product.html"
    context = {}
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        product = self.model.objects.get(pk=pk)
        form = AddProductForm(instance=product)
        self.context["products"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        product = self.model.objects.get(pk=pk)
        form = AddProductForm(instance=product,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("list")
        else:
            self.context["products"] = form
            return render(request,self.template_name,self.context)
class DeleteProductView(TemplateView):
    model = Product
    def get(self, request, *args, **kwargs):
        pk = self.kwargs.get("pk")
        self.model.objects.get(pk=pk).delete()
        return redirect("list")
class AddPurchaseView(TemplateView):
    model = Purchase
    template_name = "billing/add_products.html"
    context = {}
    def get(self, request, *args, **kwargs):
        form = AddPurchaseForm()
        self.context["form"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        form = AddPurchaseForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchaselist")
        else:
            self.context["form"] = form
            return render(request,self.template_name,self.context)
class PurchaseListView(TemplateView):
    model = Purchase
    template_name = "billing/purchase_list.html"
    context = {}
    def get(self, request, *args, **kwargs):
        purchase = self.model.objects.all()
        self.context["purchases"] = purchase
        return render(request,self.template_name,self.context)
class EditPurchaseView(TemplateView):
    model = Purchase
    template_name = "billing/edit_purchase.html"
    context = {}
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        purchase = self.model.objects.get(pk=pk)
        form = AddPurchaseForm(instance=purchase)
        self.context["purchases"] = form
        return render(request,self.template_name,self.context)

    def post(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        purchase = self.model.objects.get(pk=pk)
        form = AddPurchaseForm(instance=purchase,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("purchaselist")
        else:
            self.context["purchases"] = form
            return redirect(request,self.template_name,self.context)
class DeletePurchaseView(TemplateView):
    model = Purchase
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        self.model.objects.get(pk=pk).delete()
        return redirect("purchaselist")