from django.contrib.auth.models import User
from django.test import TestCase

from store.models import (Category, Customer, Order, OrderItem, Product,
                          ShippingAddress)


class TestCustomersModel(TestCase):

    def setUp(self):
        User.objects.create(username='test1')
        self.data = Customer.objects.create(user_id=1, name='test1', email='test1@gmail.com')

    def test_customer_model_enrty(self):
        """
        Test category model data insertion/types/field attributes
        """
        data = self.data
        self.assertTrue(isinstance(data, Customer))
        self.assertEqual(str(data), 'test1')


class TestCategoriesModel(TestCase):

    def setUp(self):
        self.data = Category.objects.create(name='Home')

    def test_category_model_enrty(self):
        data = self.data
        self.assertTrue(isinstance(data, Category))
        self.assertEqual(str(data), 'Home')


class TestProductsModel(TestCase):

    def setUp(self):
        Category.objects.create(name='Home')
        User.objects.create(username='test1')
        self.data = Product.objects.create(category_id=1, created_by_id=1, name='Watch', price=456.93, digital=False, image='watch_SO29h7C.jpeg', in_stock=1, created='', updated='')

    def test_product_model_entry(self):
        data = self.data
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'Watch')


class TestOrdersModel(TestCase):

    def setUp(self):
        User.objects.create(username='test1')
        Customer.objects.create(user_id=1, name='test1', email='test1@gmail.com')
        self.data = Order.objects.create(customer_id=1, complete=True, transaction_id=23465678, date_orderd='')

    def test_order_model_enrty(self):
        data = self.data
        self.assertTrue(isinstance(data, Order))
        self.assertEqual(str(data), '1')


class TestOrderItemsModel(TestCase):

    def setUp(self):
        User.objects.create(username='test1')
        Customer.objects.create(user_id=1, name='test1', email='test1@gmail.com')
        Category.objects.create(name='Home')
        Product.objects.create(category_id=1, created_by_id=1, name='Watch', price=456.93, digital=False, image='watch_SO29h7C.jpeg', in_stock=1, created='', updated='')
        Order.objects.create(customer_id=1, complete=True, transaction_id=23465678, date_orderd='')
        self.data = OrderItem.objects.create(product_id=1, order_id=1, quantity=1, date_added='')

    def test_order_item_model_enrty(self):
        data = self.data
        self.assertTrue(isinstance(data, OrderItem))
        self.assertEqual(str(data), 'OrderItem object (1)')


class TestShippingAddressesdersModel(TestCase):

    def setUp(self):
        User.objects.create(username='test1')
        Customer.objects.create(user_id=1, name='test1', email='test1@gmail.com')
        Order.objects.create(customer_id=1, complete=True, transaction_id=23465678, date_orderd='')
        self.data = ShippingAddress.objects.create(customer_id=1, order_id=1, address='fesa', city='', zipcode='', state='')

    def test_order_model_enrty(self):
        data = self.data
        self.assertTrue(isinstance(data, ShippingAddress))
        self.assertEqual(str(data), 'fesa')
