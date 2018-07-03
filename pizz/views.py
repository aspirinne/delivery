from django.shortcuts import get_object_or_404
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework.response import Response
from .serializers import OrderSerializer, PizzaSerializer, CustomerSerializer
from .models import Order, Pizza, Customer


# Create your views here.
@api_view(['GET'])
def api_root(request):
    """The entry endpoint of API."""
    return Response({
        'orders': reverse('order-list', request=request),
        'pizzas': reverse('pizza-list', request=request),
        'customers': reverse('customer-list', request=request),
    })


class OrderList(generics.ListCreateAPIView):
    """API endpoint that represents a list of Orders."""
    model = Order
    serializer_class = OrderSerializer

    def get_queryset(self):
        """
        Function which define filter for queryset.
        :return: queryset of orders.
        """
        queryset = Order.objects.select_related().all()
        customer_filter = self.request.query_params.get('customer_name')

        if customer_filter:
            queryset = queryset.filter(customer__name=customer_filter)

        return queryset


class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that represent a single order."""
    model = Order
    serializer_class = OrderSerializer
    lookup_field = 'id'

    def get_object(self):
        """
        Overriding the get_object function.
        :return: object with id=pk.
        """
        obj = get_object_or_404(Order, id=self.kwargs['pk'])
        return obj


class PizzaList(generics.ListCreateAPIView):
    """API endpoint that represents a list of Pizzas."""
    model = Pizza
    serializer_class = PizzaSerializer

    def get_queryset(self):
        """
        Function which define filter for queryset.
        :return: queryset of pizzas.
        """
        queryset = Pizza.objects.all()
        return queryset


class PizzaDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API endpoint that represent a single pizza.
    """
    model = Pizza
    serializer_class = PizzaSerializer

    def get_object(self):
        """
        Overriding the get_object function.
        :return: Pizza.object with id=pk.
        """
        obj = get_object_or_404(Pizza, id=self.kwargs['pk'])
        return obj


class CustomerList(generics.ListCreateAPIView):
    """API endpoint that represents a list of Customers"""
    model = Customer
    serializer_class = CustomerSerializer

    def get_queryset(self):
        """
        Function which define filter for queryset
        :return: queryset of customers
        """
        queryset = Customer.objects.all()
        return queryset


class CustomerDetail(generics.RetrieveUpdateDestroyAPIView):
    """API endpoint that represent a single customer."""
    model = Customer
    serializer_class = CustomerSerializer

    def get_object(self):
        """
        Overriding the get_object function.
        :return: Customer.object with id=pk.
        """
        obj = get_object_or_404(Customer, id=self.kwargs['pk'])
        return obj
