from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import AbstractUser
from django.db import models


class Users(AbstractUser):
    UserID = models.AutoField(primary_key=True)
    Phone = models.CharField(max_length=10)
    Address = models.CharField(max_length=255)
    UserType = models.CharField(
        max_length=20,
        choices=[
            ("Customer", "Customer"),
            ("Restaurant Owner", "Restaurant Owner"),
            ("Admin", "Admin"),
        ],
    )

    # Required fields for authentication
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email", "Phone", "Address", "UserType"]

    def __str__(self):
        return self.username


class Restaurants(models.Model):
    RestaurantID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Address = models.CharField(max_length=255)
    Phone = models.CharField(max_length=20)
    Email = models.EmailField(max_length=255)
    Website = models.CharField(max_length=255)
    OpeningHours = models.CharField(max_length=255)
    DeliveryAreas = models.TextField()
    DeliveryFee = models.DecimalField(max_digits=10, decimal_places=2)
    MinimumOrderAmount = models.DecimalField(max_digits=10, decimal_places=2)
    Rating = models.FloatField()
    TotalReviews = models.IntegerField()

    def __str__(self):
        return self.Name


class MenuCategories(models.Model):
    CategoryID = models.AutoField(primary_key=True)
    CategoryName = models.CharField(max_length=255)
    Description = models.TextField()

    def __str__(self):
        return self.CategoryName


class MenuItems(models.Model):
    MenuItemID = models.AutoField(primary_key=True)
    RestaurantID = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    CategoryID = models.ForeignKey(MenuCategories, on_delete=models.CASCADE)
    Name = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    ImageURL = models.ImageField(upload_to="MenuImages/")
    Availability = models.BooleanField()

    def __str__(self) -> str:
        return self.Name


class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    RestaurantID = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    OrderDate = models.DateField()
    DeliveryDate = models.DateField()
    Status = models.CharField(max_length=255)
    TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)
    DeliveryAddress = models.CharField(max_length=255)
    PaymentMethod = models.CharField(max_length=255)
    PaymentStatus = models.CharField(max_length=255)


class OrderItems(models.Model):
    OrderItemID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    MenuItemID = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)


class Reviews(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    UserID = models.ForeignKey(Users, on_delete=models.CASCADE)
    RestaurantID = models.ForeignKey(Restaurants, on_delete=models.CASCADE)
    Rating = models.IntegerField()
    Comment = models.TextField()
    Date = models.DateField()


class Payments(models.Model):
    PaymentID = models.AutoField(primary_key=True)
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    Amount = models.DecimalField(max_digits=10, decimal_places=2)
    PaymentDate = models.DateField()
    PaymentMethod = models.CharField(max_length=255)
    TransactionID = models.CharField(max_length=255)
    PaymentStatus = models.CharField(max_length=255)


class CartItem(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    item = models.ForeignKey(MenuItems, on_delete=models.CASCADE)
    quantity = models.IntegerField(default=1)

    def subtotal(self):
        return self.quantity * self.item.Price
