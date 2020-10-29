from django.db import models
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.urls import reverse
from django.core.validators import RegexValidator
from django.core.validators import MaxValueValidator, MinValueValidator

'''AUTH START'''

class AccountManager(BaseUserManager):
    def create_user(self,username,password=None,**extra_fields):
        if not username:
            raise ValueError("Username is required")


        user=self.model(
            username=username,

            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, password, **extra_fields):
        # Creating superuser having all the rights
        user=self.create_user(

                    username,
                     password,
                      **extra_fields)

        user.is_admin=True
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self._db)


        return user

class Account(AbstractBaseUser,PermissionsMixin):
    email = models.EmailField(verbose_name="email", max_length=60, unique=True)
    f_name = models.CharField(max_length=20,blank=True,null=True)
    m_name = models.CharField(max_length=40,null=True,blank=True)
    l_name = models.CharField(max_length=20,blank=True,null=True)


    address_line_1=models.TextField(blank=True)
    address_line_2=models.TextField(blank=True)
    City=models.CharField(max_length=200)
    pin_code_regex = RegexValidator(regex= "^[1-9]{1}[0-9]{2}\\s{0,1}[0-9]{3}$",
                                    message = "Enter a valid pin code")
    pin_code = models.CharField(
            validators=[pin_code_regex],
            max_length=6,
            blank=False,
            null=False,
    )

    i_agree = models.BooleanField(default=False)
    date_joined = models.DateTimeField(verbose_name="date joined", auto_now_add=True)
    last_login = models.DateTimeField(verbose_name="last login", auto_now=True)

    is_active=models.BooleanField(default=True)
    is_staff=models.BooleanField(default=False)
    is_superuser=models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)

    is_customer=models.BooleanField(default=False)
    is_owner=models.BooleanField(default=False)

    USERNAME_FIELD='email'
    REQUIRED_FIELDS=[]
    objects=AccountManager()

    def __str__(self):
        return self.f_name + " " + self.l_name
    def __str__(self):
        return self.email
    def has_perm(self, perm, obj=None):
        return self.is_admin
    def has_module_perms(self, app_label):
        return True

class Customer(Account):
    profile_image = models.ImageField(
        upload_to="profile_images",
        blank=True,
        null=True,
    )

class Owner(Account):
    Registration_Number = models.IntegerField(blank=False, null=False)
    pan_no = models.CharField(max_length= 10,blank=True, null=True)
    logo=models.ImageField(
        upload_to="logo",
        blank=True,
        null=True,
    )

'''AUTH MODELS END'''


class Restaurant(models.Model):
	user= models.OneToOneField(Owner,on_delete=models.CASCADE)
	rname= models.CharField(max_length=100,blank=False)
	info= models.CharField(max_length=40,blank=False)
	min_ord= models.CharField(max_length=5,blank=False)
	location= models.CharField(max_length=40,blank=False)
	r_logo= models.FileField(blank=False)

	REST_STATE_OPEN    = "Open"
	REST_STATE_CLOSE   = "Closed"
	REST_STATE_CHOICES =(
			(REST_STATE_OPEN,REST_STATE_OPEN),
			(REST_STATE_CLOSE,REST_STATE_CLOSE)
		)
	status 	= models.CharField(max_length=50,choices=REST_STATE_CHOICES,default=REST_STATE_OPEN,blank=False)
	approved = models.BooleanField(blank=False,default=True)

	def __str__(self):
		return self.rname

class Item(models.Model):
	id= models.AutoField(primary_key=True)
	fname= models.CharField(max_length=30,blank=False)
	category= models.CharField(max_length=50,blank=False)

	def __str__(self):
		return self.fname

class Menu(models.Model):
	id= models.AutoField(primary_key=True)
	item_id= models.ForeignKey(Item,on_delete=models.CASCADE)
	r_id= models.ForeignKey(Restaurant,on_delete=models.CASCADE)
	price= models.IntegerField(blank=False)
	quantity= models.IntegerField(blank=False,default=0)

	def __str__(self):
		return self.item_id.fname+' - '+str(self.price)

class Order(models.Model):
	id = models.AutoField(primary_key=True)
	total_amount= models.IntegerField(default=0)
	timestamp= models.DateTimeField(auto_now_add=True)
	delivery_addr= models.CharField(max_length=50,blank=True)
	orderedBy= models.ForeignKey(User ,on_delete=models.CASCADE)
	r_id= models.ForeignKey(Restaurant ,on_delete=models.CASCADE)

	ORDER_STATE_WAITING= "Waiting"
	ORDER_STATE_PLACED= "Placed"
	ORDER_STATE_ACKNOWLEDGED= "Acknowledged"
	ORDER_STATE_COMPLETED= "Completed"
	ORDER_STATE_CANCELLED= "Cancelled"
	ORDER_STATE_DISPATCHED= "Dispatched"

	ORDER_STATE_CHOICES = (
		(ORDER_STATE_WAITING,ORDER_STATE_WAITING),
	    (ORDER_STATE_PLACED, ORDER_STATE_PLACED),
	    (ORDER_STATE_ACKNOWLEDGED, ORDER_STATE_ACKNOWLEDGED),
	    (ORDER_STATE_COMPLETED, ORDER_STATE_COMPLETED),
	    (ORDER_STATE_CANCELLED, ORDER_STATE_CANCELLED),
	    (ORDER_STATE_DISPATCHED, ORDER_STATE_DISPATCHED)
	)
	status = models.CharField(max_length=50,choices=ORDER_STATE_CHOICES,default=ORDER_STATE_WAITING)

	def __str__(self):
		return str(self.id) +' '+self.status

class orderItem(models.Model):
	id= models.AutoField(primary_key=True)
	item_id= models.ForeignKey(Menu ,on_delete=models.CASCADE)
	ord_id= models.ForeignKey(Order,on_delete=models.CASCADE)
	quantity= models.IntegerField(default=0)

	def __str__(self):
		return str(self.id)
