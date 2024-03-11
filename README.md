bug - stripe webhooks failing. - Fix added missin / to the end of the webhook name

Bug - logo image not loading after heroku deployment - fix: Adjusted image src link for AWS hosting
src="https://woof-and-bean-ci-m4.s3.amazonaws.com/media/wblogo.png"

Search bar icon inside input on the right helped by Slack London community

8 products per category

singals instances create and save

set up ready signals in apps.py import signals to activate

Add items to wishlist - using add item to bag views.py code as a base?

Add a contact model custom model 2





## User Stories

### As A/An Shopper
    - **Viewing and Navigation**

        | I Want To Be Able To...                                    | So That I Can...                                                                   | 
        |------------------------------------------------------------|------------------------------------------------------------------------------------| 
        | View a list of products                                    | Select some to purchase                                                            | 
        | View individual product details                            | Identify the price, description, product rating,<br> product image and available sizes |
        | Quickly identify deals,<br> clearance items and special offers | Take advantage of special savings on products<br> I'd like to purchase |
        | Easily view the total of my purchases at any time          | Avoid spending too much |

    - **Sorting and Searching**
        
        | I Want To Be Able To...                                    | So That I Can...                                                                   | 
        |------------------------------------------------------------|------------------------------------------------------------------------------------|
        | Sort the list of available products                        | Easily identify the best rated, best priced and<br> categorically sorted products |
        | Sort a specific category or products                       | Find the best-priced or best-rated product in a<br> specific category, or sort the products in that<br> category by name |
        | Sort multiple categories of products simultaneously        | Find the best-priced or best-rated products across<br> broad categories, such as "Treats" or "Accessories" |
        | Search for a product by name or description                | Find a specific product I'd like to purchase |
        | Easily see what I've searched for and the number of<br> results | Quickly decide whether the product I want is available |

    - **Purchasing and Checkout**
        
        | I Want To Be Able To...                                    | So That I Can...                                                                   | 
        |------------------------------------------------------------|------------------------------------------------------------------------------------|
        | Easily select the size and quantity of a product<br> when purchasing it | Ensure I dont accidentally select the wrong product,<br> quantity or size |


### As A/An Site User
    - **Registration and User Accounts**

        | I Want To Be Able To...                                    | So That I Can...                                                                   | 
        |------------------------------------------------------------|------------------------------------------------------------------------------------|
        | Easily register for an account | Have a personal account and be able to view my profile |
        | Easily login or logout | Access my personal account information |
        | Easily recover my password in case I forget it | Recover access to my account |
        | Receive an email confirmation after registering | Verfify that my account registration was successful |
        | Have a personalized user profile | View my personal order history, order confirmations<br> and save my personal information |


# Product Model
    "category" - Product category ForeignKey
    "sku" - product sku
    "name" - product name
    "description" - product description
    "price" - product price
    "rating" - product rating
    "image url" - product image url
    "image" - product image

# Profiles Model
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    default_phone_number = models.CharField(max_length=20, null=True, blank=True)
    default_street_address1 = models.CharField(max_length=80, null=True, blank=True)
    default_street_address2 = models.CharField(max_length=80, null=True, blank=True)
    default_town_or_city = models.CharField(max_length=40, null=True, blank=True)
    default_county = models.CharField(max_length=80, null=True, blank=True)
    default_postcode = models.CharField(max_length=20, null=True, blank=True)
    default_country = CountryField(blank_label='Country', null=True, blank=True)

# Category Model
    "name" - category name PrimaryKey
    "friendly_name" - friendly name for front end

# wishlist Model
    "User" - One to One field - User
    "products" - Many to Many field - Product
    "created" - date time field

# rating Model
    star choices 1,1 - 2,2 - 3,3 - 4,4 - 5,5
    "User" - foreignkey
    "product" - foreignkey
    "order" - foreignkey
    "rating" - charfield - 1-5 stars

# Order checkout Model
     order_number = models.CharField(max_length=32, null=False, editable=False)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.SET_NULL,
                                     null=True, blank=True, related_name='orders')
    full_name = models.CharField(max_length=50, null=False, blank=False)
    email = models.EmailField(max_length=254, null=False, blank=False)
    phone_number = models.CharField(max_length=20, null=False, blank=False)
    country = CountryField(blank_label='Country *', null=False, blank=False)
    postcode = models.CharField(max_length=20, null=True, blank=True)
    town_or_city = models.CharField(max_length=40, null=False, blank=False)
    street_address1 = models.CharField(max_length=80, null=False, blank=False)
    street_address2 = models.CharField(max_length=80, null=True, blank=True)
    county = models.CharField(max_length=80, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    delivery_cost = models.DecimalField(max_digits=6, decimal_places=2, null=False, default=0)
    order_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    grand_total = models.DecimalField(max_digits=10, decimal_places=2, null=False, default=0)
    original_bag = models.TextField(null=False, blank=False, default='')
    stripe_pid = models.CharField(max_length=254, null=False, blank=False, default='')



# Font/Typeface
    Poppins - Googlefonts
